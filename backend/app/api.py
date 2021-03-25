from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.responses import FileResponse
from fastapi_mail import FastMail
from sqlalchemy.orm import Session
from twilio.rest import Client

from app import crud, schemas, notify
from app.config import bier_settings
from app.database import get_db
from app.notify import get_fm, get_twilio_client
from app.hashing import hash_email

router = APIRouter()


@router.post('/verify/notify/', status_code=status.HTTP_200_OK)
async def verify_contact(
        verify: schemas.Verify,
        background_tasks: BackgroundTasks,
        fm: FastMail = Depends(get_fm),
        client: Client = Depends(get_twilio_client)):
    if verify.channel == 'sms':
        try:
            phone_number = client.lookups.v1.phone_numbers(verify.to).fetch()
            background_tasks.add_task(notify.verification_sms, client, phone_number.phone_number)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                # todo: format
                detail='Telefonnummer im falschen Format ###')
    if verify.channel == 'email':
        background_tasks.add_task(notify.verification_email, fm, verify.to)


@router.post('/verify/check/', status_code=status.HTTP_200_OK)
async def verify_check_contact(
        verify_check: schemas.VerifyCheck,
        fm: FastMail = Depends(get_fm),
        client: Client = Depends(get_twilio_client)):
    if not hash_email(verify_check.to) == verify_check.hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Verifizierungsnummer falsch')


@router.post('/team/', response_model=schemas.Team, status_code=status.HTTP_201_CREATED)
def create_team(
        team: schemas.Team,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
        fm: FastMail = Depends(get_fm)):

    db_team = crud.get_team_by_contact(db, team.contact)
    if db_team:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Team mit dieser Email bereits registriert.')
    new_team = crud.create_team(db, team)
    if new_team.channel == 'email':
        background_tasks.add_task(notify.registration_mail, fm, new_team)
    # todo: background task for sms
    return new_team


@router.delete('/team/{contact}/{hash}', response_model=schemas.Team, status_code=status.HTTP_200_OK)
def delete_team(
        contact: str,
        hash: str,
        db: Session = Depends(get_db)):

    db_team = crud.get_team_by_contact(db, contact)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Kein Team mit unter {contact} ist registriert.')
    if not hash_email(contact) == hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Stornonummer nicht gültig! Überprüfe die Nummer die wir dir an {db_team.contact} gesendet haben.')
    deleted_team = crud.delete_team(db, contact)
    return deleted_team


@router.get('/options/time/')
def get_time_options(db: Session = Depends(get_db)):
    time_options = []
    places_taken = crud.get_places_taken(db)
    id = 1
    for block, time in zip(bier_settings.blocks, bier_settings.times):
        places_free = bier_settings.teams_per_block
        if block in places_taken:
            places_free -= places_taken[block]
        time_options.append({
            'id': id,
            'value': block,
            'text': f'Block {block}',
            'time': time,
            'free': places_free,
        })
        id += 1
    return time_options


@router.get('/options/drink/')
def get_drink_option():
    return bier_settings.drinks


@router.get('/places/free/')
def get_free_places(db: Session = Depends(get_db)):
    places_taken = crud.get_places_taken(db)
    places_free = len(bier_settings.blocks) * bier_settings.teams_per_block - sum(places_taken.values())
    return places_free


@router.get('/registered/csv/')
def get_registered_csv(db: Session = Depends(get_db)):
    return FileResponse(crud.create_registered_csv(db), filename='registrierte_nutzer.csv')

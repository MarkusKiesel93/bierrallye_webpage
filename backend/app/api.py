from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.responses import FileResponse
from fastapi_mail import FastMail
from sqlalchemy.orm import Session

from app import crud, schemas, notify
from app.config import settings, bier_settings
from app.database import get_db
from app.notify import get_fm, TwilioClient, get_twilio_client
from app.hashing import hash_contact

router = APIRouter()


@router.post('/verify/notify/', status_code=status.HTTP_200_OK)
async def verify_contact(
        verify: schemas.Verify,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
        fm: FastMail = Depends(get_fm),
        client: TwilioClient = Depends(get_twilio_client)):

    # todo: fraud detection, notify admin

    allow_notify_time, next_try = crud.allow_notify_time(db, verify)
    if not allow_notify_time:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f'Nächster Versuch in {next_try} Sekunden.'
        )

    allow_notify_tries = crud.allow_notify_tries(db, verify)
    if not allow_notify_tries:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                f'Mehr als {settings.verify_allow_tries} Anmeldeverusche\n'
                f'Benutze eine andere Kontaktart oder melde dich unter {bier_settings.contact}'
            )
        )

    new_notify = crud.store_notification_time(db, verify)

    if verify.channel == 'sms':
        try:
            phone_number = client.lookups.v1.phone_numbers(verify.to).fetch()
            background_tasks.add_task(notify.verification_sms, client, phone_number.phone_number)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Telefonnummer im falschen Format')
    if verify.channel == 'email':
        background_tasks.add_task(notify.verification_email, fm, verify.to)
    return new_notify


@router.post('/verify/check/', status_code=status.HTTP_200_OK)
async def verify_check_contact(
        verify_check: schemas.VerifyCheck):
    if not hash_contact(verify_check.to) == verify_check.hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Verifizierungsnummer falsch')
    return verify_check


@router.post('/team/', response_model=schemas.Team, status_code=status.HTTP_201_CREATED)
def create_team(
        team: schemas.Team,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
        fm: FastMail = Depends(get_fm),
        client: TwilioClient = Depends(get_twilio_client)):

    db_team = crud.get_team_by_contact(db, team.contact)
    if db_team:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Team mit dieser Email bereits registriert.')
    new_team = crud.create_team(db, team)
    if new_team.channel == 'email':
        background_tasks.add_task(notify.registration_mail, fm, new_team)
    if new_team.channel == 'sms':
        background_tasks.add_task(notify.registration_sms, client, new_team)
    return new_team


@router.get('/team/{contact}/', response_model=schemas.Team,  status_code=status.HTTP_200_OK)
def get_team(contact: str, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_contact(db, contact)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Kein Team mit unter {contact} ist registriert.')
    return db_team


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
    if not hash_contact(contact) == hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Stornonummer nicht gültig! Überprüfe die Nummer die wir dir an {db_team.contact} gesendet haben.')
    deleted_team = crud.delete_team(db, contact)
    return deleted_team


@router.get('/options/blocks/')
def get_blocks_options(db: Session = Depends(get_db)):
    block_options = []
    places_taken = crud.get_places_taken(db)
    id = 1
    for block, time in zip(bier_settings.start_blocks, bier_settings.times):
        places_free = bier_settings.teams_per_block
        if block in places_taken:
            places_free -= places_taken[block]
        block_options.append({
            'id': id,
            'value': block,
            'text': f'Block {block}',
            'time': time,
            'free': places_free,
        })
        id += 1
    return block_options


@router.get('/options/drinks/')
def get_drink_option():
    return bier_settings.drinks


@router.get('/places/free/')
def get_free_places(db: Session = Depends(get_db)):
    places_taken = crud.get_places_taken(db)
    places_free = len(bier_settings.start_blocks) * bier_settings.teams_per_block - sum(places_taken.values())
    return places_free


@router.get('/registered/csv/')
def get_registered_csv(db: Session = Depends(get_db)):
    return FileResponse(crud.create_registered_csv(db), filename='registrierte_nutzer.csv')

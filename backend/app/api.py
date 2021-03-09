from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app import crud, schemas, mail
from app.database import get_db
from app.config import bier_settings

router = APIRouter()


@router.post('/team/', response_model=schemas.TeamCreated, status_code=status.HTTP_201_CREATED)
def create_team(team: schemas.Team, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_email(db, team.email)
    if db_team:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Team mit dieser Email bereits registriert.')
    new_team = crud.create_team(db, team)
    background_tasks.add_task(mail.verification_mail, new_team)
    return new_team


@router.post('/team/verify', response_model=schemas.Verified, status_code=status.HTTP_200_OK)
def verify_team(verify: schemas.Verify, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_email(db, verify.email)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Kein Team mit dieser Email hat sich registriert.')
    if not db_team.hash == verify.hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Verifizierungsnummer falsch')
    db_verified = crud.get_verified_by_email(db, verify.email)
    if db_verified:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Diese Email Adresse ist bereits verifiziert.')
    verify_create = crud.verify(db, verify.email)
    background_tasks.add_task(mail.registration_mail, db_team)
    return verify_create


@router.delete('/team/{email}/{hash}', response_model=schemas.Team, status_code=status.HTTP_200_OK)
def delete_team(email: str, hash: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_email(db, email)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Kein Team mit dieser Email ist registriert.')
    if not db_team.hash == hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Stornonummer nicht gültig! Überprüfe die Nummer die wir dir an {db_team.email} gesendet haben.')
    deleted_team = crud.delete_team(db, email)
    background_tasks.add_task(mail.deregistration_mail, deleted_team)
    return deleted_team


@router.get('/options/time/')
def get_time_options(db: Session = Depends(get_db)):
    time_options = []
    places_taken = crud.get_places_taken(db)
    for block, time in zip(bier_settings.blocks, bier_settings.times):
        places_free = bier_settings.teams_per_block
        if block in places_taken:
            places_free -= places_taken[block]
        time_options.append({
            'value': block,
            'text': f'Block {block}',
            'time': time,
            'free': places_free,
        })
    return time_options


@router.get('/options/drink/')
def get_drink_option(db: Session = Depends(get_db)):
    return bier_settings.drinks


@router.get('/places/free/')
def get_free_places(db: Session = Depends(get_db)):
    places_taken = crud.get_places_taken(db)
    places_free = len(bier_settings.blocks) * bier_settings.teams_per_block - sum(places_taken.values())
    return places_free


@router.get('/registered/')
def get_registered(db: Session = Depends(get_db)):
    return crud.get_teams_registered(db)


@router.get('/registered/csv/')
def get_registered_csv(db: Session = Depends(get_db)):
    return FileResponse(crud.create_registered_csv(db), filename='registrierte_nutzer.csv')

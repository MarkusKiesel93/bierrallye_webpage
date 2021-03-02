from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session

from app import crud, schemas, mail
from app.database import get_db

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


@router.get('/places/free/')
def get_places_free(db: Session = Depends(get_db)):
    return crud.get_places_free(db)

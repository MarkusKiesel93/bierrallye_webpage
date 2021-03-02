from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.mail import verification_mail, registration_mail, deregistration_mail

router = APIRouter()


@router.post('/team/', response_model=schemas.TeamCreated, status_code=status.HTTP_201_CREATED)
def create_team(team: schemas.Team, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_email(db, team.email)
    if db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Team mit dieser Email bereits registriert!')
    new_team = crud.create_team(db, team)
    background_tasks.add_task(verification_mail, new_team)
    return new_team


@router.post('/team/verify', response_model=schemas.Verified, status_code=status.HTTP_200_OK)
def verify_team(verify: schemas.Verify, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_email(db, verify.email)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Kein Team mit dieser Email ist registriert!')
    if not db_team.hash == verify.hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Hash falsch')
    verify_create = crud.verify(db, verify.email)
    background_tasks.add_task(registration_mail, db_team)
    return verify_create


@router.delete('/team/{email}/{hash}', response_model=schemas.Team, status_code=status.HTTP_200_OK)
def delete_team(email: str, hash: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_team = crud.get_team_by_email(db, email)
    if not db_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Kein Team mit dieser Email ist registriert!')
    if not db_team.hash == hash:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Stornocode ist nicht gültig! Überprüfe den Code den wir dir an {db_team.email} gesendet haben.')
    deleted_team = crud.delete_team(db, email)
    background_tasks.add_task(deregistration_mail, deleted_team)
    return deleted_team


@router.get('/places/free/')
def get_places_free(db: Session = Depends(get_db)):
    return crud.get_places_free(db)

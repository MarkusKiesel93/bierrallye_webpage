from sqlalchemy import func
from sqlalchemy.orm import Session
from datetime import date

from app import models, schemas
from app.hashing import hash_email


def create_team(db: Session, team: schemas.Team):
    hash = hash_email(team.email)
    db_team = models.Team(**team.dict(), hash=hash)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def verify(db: Session, email: str):
    reg_date = str(date.today().strftime('%d.%m.%Y'))
    db_verified = models.Verified(email=email, registration_date=reg_date)
    db.add(db_verified)
    db.commit()
    db.refresh(db_verified)
    return db_verified


def delete_team(db: Session, email: str):
    team = get_team_by_email(db, email)
    db.delete(team)
    verified = get_verifyed_by_email(db, email)
    db.delete(verified)
    db.commit()
    return team


def get_team_by_email(db: Session, email: str):
    return db.query(models.Team).filter(models.Team.email == email).first()


def get_verifyed_by_email(db: Session, email: str):
    return db.query(models.Verified).filter(models.Verified.email == email).first()


def get_places_free(db: Session):
    places_free = {
        'block1': 30,
        'block2': 30,
        'block3': 30,
        'block4': 30,
    }
    counts = db.query(models.Team.time_pref, func.count(models.Team.email)).group_by(models.Team.time_pref).all()
    for block, count in counts:
        places_free[block] -= count
    return places_free

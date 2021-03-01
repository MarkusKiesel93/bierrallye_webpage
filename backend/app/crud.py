from sqlalchemy import func
from sqlalchemy.orm import Session
from datetime import date

from app import models, schemas
from app.hashing import hash_email


def create_team(db: Session, team: schemas.Team):
    hash = hash_email(team.email)
    reg_date = str(date.today().strftime('%d.%m.%Y'))
    db_team = models.Team(**team.dict(), hash=hash, registration_date=reg_date)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def delete_team(db: Session, email: str):
    team = get_team_by_email(db, email)
    db.delete(team)
    db.commit()
    return team


def get_team_by_email(db: Session, email: str):
    return db.query(models.Team).filter(models.Team.email == email).first()


def get_places_left(db: Session):
    places_left = {
        'block_1': 30,
        'block_2': 30,
        'block_3': 30,
        'block_4': 30,
    }
    counts = db.query(models.Team.time_pref, func.count(models.Team.email)).group_by(models.Team.time_pref).all()
    for block, count in counts:
        places_left[block] -= count
    return places_left

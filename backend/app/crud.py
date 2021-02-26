from sqlalchemy.orm import Session

from app import models, schemas
from app.hashing import hash_email


def create_team(db: Session, team: schemas.Team):
    hash = hash_email(team.email)
    db_team = models.Team(**team.dict(), hash=hash)
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

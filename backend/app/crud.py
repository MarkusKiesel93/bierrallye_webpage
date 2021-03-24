from sqlalchemy import func
from sqlalchemy.orm import Session
from datetime import date
import pandas as pd
import json

from app import models, schemas
from app.hashing import hash_email
from app.config import settings


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
    verified = get_verified_by_email(db, email)
    db.delete(verified)
    db.commit()
    return team


def get_team_by_email(db: Session, email: str):
    return db.query(models.Team).filter(models.Team.email == email).first()


def get_verified_by_email(db: Session, email: str):
    return db.query(models.Verified).filter(models.Verified.email == email).first()


def get_places_taken(db: Session):
    places_taken = {}
    counts = db.query(models.Team.time_pref, func.count(models.Team.email)).group_by(models.Team.time_pref).all()
    for block, count in counts:
        places_taken[block] = count
    return places_taken


def create_registered_csv(db: Session):
    query = db.query(
        models.Team
    ).join(
        models.Verified,
        models.Team.email == models.Verified.email)
    df = pd.read_sql(query.statement, db.bind)
    df['Spieler 1'] = df['first_name_player_1'] + ' ' + df['last_name_player_1']
    df['Spieler 2'] = df['first_name_player_2'] + ' ' + df['last_name_player_2']
    df = df.rename(columns={
        'email': 'Email',
        'drink_pref_player_1': 'Getränk 1',
        'drink_pref_player_2': 'Getränk 2',
        'time_pref': 'Startblock',
    })
    df = df.drop(columns=[
        'first_name_player_1',
        'last_name_player_1',
        'first_name_player_2',
        'last_name_player_2'
    ])
    df = df.reindex(columns=['Email', 'Spieler 1', 'Getränk 1', 'Spieler 2', 'Getränk 2', 'Startblock'])
    csv_path = settings.static_path / 'registrierte_nutzer.csv'
    df.to_csv(csv_path, index=False)
    return csv_path

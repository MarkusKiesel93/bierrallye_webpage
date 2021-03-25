from datetime import date
import pandas as pd
from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models, schemas
from app.config import settings


def create_team(db: Session, team: schemas.Team):
    reg_date = str(date.today().strftime('%d.%m.%Y'))
    db_team = models.Team(**team.dict(), registration_date=reg_date)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def delete_team(db: Session, contact: str):
    team = get_team_by_contact(db, contact)
    db.delete(team)
    db.commit()
    return team


def get_team_by_contact(db: Session, contact: str):
    return db.query(models.Team).filter(models.Team.contact == contact).first()


def get_places_taken(db: Session):
    places_taken = {}
    counts = db.query(models.Team.time_pref, func.count(models.Team.contact)).group_by(models.Team.time_pref).all()
    for block, count in counts:
        places_taken[block] = count
    return places_taken


def create_registered_csv(db: Session):
    query = db.query(models.Team)
    df = pd.read_sql(query.statement, db.bind)
    df['Spieler 1'] = df['first_name_player_1'] + ' ' + df['last_name_player_1']
    df['Spieler 2'] = df['first_name_player_2'] + ' ' + df['last_name_player_2']
    df = df.rename(columns={
        'contact': 'Kontakt',
        'channel': 'Kontakt Art',
        'drink_pref_player_1': 'Getränk 1',
        'drink_pref_player_2': 'Getränk 2',
        'time_pref': 'Startblock',
        'registration_date': 'Anmeldedatum'
    })
    df = df.drop(columns=[
        'first_name_player_1',
        'last_name_player_1',
        'first_name_player_2',
        'last_name_player_2',
    ])
    df = df.reindex(columns=['Kontakt', 'Kontakt Art', 'Spieler 1', 'Getränk 1',
                             'Spieler 2', 'Getränk 2', 'Startblock'])
    csv_path = settings.static_path / 'registrierte_nutzer.csv'
    df.to_csv(csv_path, index=False)
    return csv_path

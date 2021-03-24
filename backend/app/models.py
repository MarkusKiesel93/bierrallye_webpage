from sqlalchemy import Column, String, Integer

from app.database import Base, engine


def create_models():
    Base.metadata.create_all(bind=engine)


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    first_name_player_1 = Column(String)
    last_name_player_1 = Column(String)
    drink_pref_player_1 = Column(String)
    first_name_player_2 = Column(String)
    last_name_player_2 = Column(String)
    drink_pref_player_2 = Column(String)
    time_pref = Column(String)
    hash = Column(String)


class Verified(Base):
    __tablename__ = "veriefied"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    registration_date = Column(String)

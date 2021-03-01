
from sqlalchemy import Column, String

from app.database import Base, engine


class Team(Base):
    __tablename__ = "teams"

    email = Column(String, primary_key=True, unique=True, index=True)
    first_name_player_1 = Column(String)
    last_name_player_1 = Column(String)
    drink_pref_player_1 = Column(String)
    first_name_player_2 = Column(String)
    last_name_player_2 = Column(String)
    drink_pref_player_2 = Column(String)
    time_pref = Column(String)
    hash = Column(String)
    registration_date = Column(String)


def create_models():
    Base.metadata.create_all(bind=engine)

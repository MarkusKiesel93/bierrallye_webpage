from pydantic import BaseModel, validator
from humps.camel import case

from app.config import bier_settings


def to_camel(string):
    return case(string)


class Team(BaseModel):
    email: str
    first_name_player_1: str
    last_name_player_1: str
    drink_pref_player_1: str
    first_name_player_2: str
    last_name_player_2: str
    drink_pref_player_2: str
    time_pref: str

    @validator('time_pref')
    def restrict_to_blocks(cls, time_pref):
        if time_pref not in bier_settings.blocks:
            raise ValueError(f'time_pref must be some block: {bier_settings.blocks}')
        return time_pref

    @validator('drink_pref_player_1')
    def restrict_to_drinks_1(cls, drink_pref_player_1):
        if drink_pref_player_1 not in bier_settings.drinks:
            raise ValueError(f'drink_pref must be one of: {bier_settings.blocks}')
        return drink_pref_player_1

    # todo: only use one validator for both
    @validator('drink_pref_player_2')
    def restrict_to_drinks_2(cls, drink_pref_player_2):
        if drink_pref_player_2 not in bier_settings.drinks:
            raise ValueError(f'drink_pref must be one of: {bier_settings.blocks}')
        return drink_pref_player_2

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class TeamCreated(Team):
    hash: str


class Verify(BaseModel):
    email: str
    hash: str


class Verified(BaseModel):
    email: str
    registration_date: str

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

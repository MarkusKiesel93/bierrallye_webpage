from pydantic import BaseModel, validator
from humps.camel import case


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
        if time_pref not in ['block1', 'block2', 'block3', 'block4']:
            raise ValueError('time_pref must be one of four blocks')
        return time_pref

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

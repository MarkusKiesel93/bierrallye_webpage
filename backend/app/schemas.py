from pydantic import BaseModel
from typing import Optional
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

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class TeamCreated(Team):
    hash: str

from pydantic import BaseModel
from typing import Optional
from humps.camel import case


def to_camel(string):
    return case(string)


class Team(BaseModel):
    email: str
    first_name_1: str
    last_name_1: str
    first_name_2: str
    last_name_2: str
    drink_pref: Optional[str] = None
    time_pref: Optional[str] = None

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class TeamCreated(Team):
    hash: str

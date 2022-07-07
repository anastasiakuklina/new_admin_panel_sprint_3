from typing import Optional

from pydantic import BaseModel, Field, validator

FIELD_ROLE = {
    'director': 'director',
    'actors_names': 'actor',
    'writers_names': 'writer',
    'actors': 'actor',
    'writers': 'writer',
}


class Person(BaseModel):
    id: str = Field(alias='person_id')
    name: str = Field(alias='person_name')
    role: str = Field(alias='person_role')

    class Config:
        fields = {'id': {'exclude': True}, 'role': {'exclude': True}}


def extract_person_names(persons: list[Person], field: str) -> list[str]:
    role = FIELD_ROLE[field.name]
    return list(map(lambda p: p.get('person_name', ''), filter(lambda p: p.get('person_role', '') == role, persons)))


def extract_persons(persons: list[Person], field: str) -> list[dict]:
    role = FIELD_ROLE[field.name]
    return list(map(lambda p: {'id': p['person_id'], 'name': p['person_name']}, filter(lambda p: p.get('person_role', '') == role, persons)))


class Movie(BaseModel):
    """
    Модель фильма, которая по данным из postgres бд получает данные, соответствующие ES индексу.
    """
    id: str
    imdb_rating: Optional[int] = Field(alias='rating')
    title: str
    description: Optional[str]
    genre: Optional[list[str]] = Field(alias='genres')
    director: Optional[list[dict]] = Field(alias='persons')
    actors_names: Optional[list[dict]] = Field(alias='persons')
    writers_names: Optional[list[dict]] = Field(alias='persons')
    actors: Optional[list[dict]] = Field(alias='persons')
    writers: Optional[list[dict]] = Field(alias='persons')


    # validators
    _extract_director = validator('director', allow_reuse=True)(extract_person_names)
    _extract_actors_names = validator('actors_names', allow_reuse=True)(extract_person_names)
    _extract_writers_names = validator('writers_names', allow_reuse=True)(extract_person_names)
    _extract_actors = validator('actors', allow_reuse=True)(extract_persons)
    _extract_writers = validator('writers', allow_reuse=True)(extract_persons)


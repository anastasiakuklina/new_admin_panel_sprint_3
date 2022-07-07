from postgres_to_es.sql_queries import MOVIES_SQL_BY_MODIFIED_MOVIES, MOVIES_SQL_BY_MODIFIED_GENRES, \
    MOVIES_SQL_BY_MODIFIED_PERSONS

FILMWORK_MODIFIED_KEY = 'filmwork_modified'
FILMWORK_FILMWORK_ID = 'filmwork_id'
GENRE_MODIFIED_KEY = 'genre_modified'
GENRE_FILMWORK_ID = 'genre_filmwork_id'
PERSON_MODIFIED_KEY = 'person_modified'
PERSON_FILMWORK_ID = 'person_filmwork_id'

START_TIME = '1900-01-01 00:00:00'


ENTITY_PARAMS = {
    'filmwork': {
        'sql': MOVIES_SQL_BY_MODIFIED_MOVIES,
        'modified_key': FILMWORK_MODIFIED_KEY,
        'fw_id_key': FILMWORK_FILMWORK_ID,
    },
    'genre': {
        'sql': MOVIES_SQL_BY_MODIFIED_GENRES,
        'modified_key': GENRE_MODIFIED_KEY,
        'fw_id_key': GENRE_FILMWORK_ID,
    },
    'person': {
        'sql': MOVIES_SQL_BY_MODIFIED_PERSONS,
        'modified_key': PERSON_MODIFIED_KEY,
        'fw_id_key': PERSON_FILMWORK_ID,
    }
}
from time import sleep

import backoff
import psycopg2
import requests
from psycopg2.extras import RealDictCursor

from postgres_to_es.constants import ENTITY_PARAMS, START_TIME
from postgres_to_es.postgres_loader import PostgresLoader
from settings import POSTGRES_PARAMS, FILE_STORAGE_PATH, ELASTICSEARCH_URL, ELASTICSEARCH_INDEX
from es_uploader import ElasticSearchUploader
from state import State, JsonFileStorage


@backoff.on_exception(backoff.expo, (psycopg2.InterfaceError, psycopg2.OperationalError,
                                     requests.exceptions.ConnectionError))
def main():
    """
    Основной метод обновления индекса в ES по изменениям в таблицах postgres.
    """
    try:
        with psycopg2.connect(**POSTGRES_PARAMS) as conn, conn.cursor(cursor_factory=RealDictCursor) as cursor:
            loader = PostgresLoader(cursor, 10)
            uploader = ElasticSearchUploader(ELASTICSEARCH_URL, ELASTICSEARCH_INDEX)
            for entity in ENTITY_PARAMS:
                state = State(JsonFileStorage(file_path=FILE_STORAGE_PATH))
                modified = state.get_state(ENTITY_PARAMS[entity]['modified_key'])
                filmwork_id = state.get_state(ENTITY_PARAMS[entity]['fw_id_key'])
                modified = modified if modified is not None else START_TIME
                for movies, last_modified, last_id in loader.read_movies(ENTITY_PARAMS[entity]['sql'], modified, filmwork_id):
                    uploader.upload(movies)
                    state.set_state(ENTITY_PARAMS[entity]['modified_key'], str(last_modified))
                    state.set_state(ENTITY_PARAMS[entity]['fw_id_key'], last_id)
    finally:
        conn.close()


if __name__ == '__main__':
    main()

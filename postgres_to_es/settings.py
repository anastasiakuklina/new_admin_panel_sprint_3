import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SQLITE_DB = 'db.sqlite'

POSTGRES_PARAMS = {
    'host': os.environ.get('POSTGRES_HOST'),
    'port': os.environ.get('POSTGRES_PORT'),
    'dbname': os.environ.get('POSTGRES_DB'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD')
}

PACK_SIZE = 500

BASE_DIR = Path(__file__).resolve().parent
FILE_STORAGE_PATH = os.path.join(BASE_DIR, 'app_state.json')

ELASTICSEARCH_URL = 'http://127.0.0.1:9200/'
ELASTICSEARCH_INDEX = 'movies'
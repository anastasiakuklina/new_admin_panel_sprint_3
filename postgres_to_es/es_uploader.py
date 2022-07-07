import json

import requests
from postgres_to_es.models import Movie


class ElasticSearchUploader:
    def __init__(self, url, index):
        self.url = url
        self.index = index

    def upload(self, movies: list[Movie]):
        data_list = list()
        for movie in movies:
            data_list.append(json.dumps({
                'index': {
                    '_index': self.index,
                    '_id': movie.id
                }}))
            data_list.append(movie.json())
        data = '\n'.join(data_list)
        data = data + '\n'
        r = requests.post(self.url + '_bulk', headers={'Content-Type': 'application/x-ndjson'}, data=data)

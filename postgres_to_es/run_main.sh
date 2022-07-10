#!/usr/bin/env bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

while ! nc -z $ES_HOST $ES_PORT; do
      sleep 0.1
    done

curl -v --insecure --user elastic:changeme -XPUT $ES_URL"movies" -H 'Content-Type: application/json' -d @es_index_config.json

python main.py

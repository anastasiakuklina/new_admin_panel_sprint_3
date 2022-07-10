FROM python:3.10

WORKDIR /postgres_to_es

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt requirements.txt
COPY es_index_config.json es_index_config.json

RUN  apt-get update \
     && apt install -y netcat \
     && pip install --upgrade pip \
     && pip install -r requirements.txt


COPY ./run_main.sh /
RUN chmod +x /run_main.sh
COPY . .

ENTRYPOINT ["/run_main.sh"]

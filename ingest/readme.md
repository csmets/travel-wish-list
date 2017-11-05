# Ingester

The ingester will get important data and insert it into the database to make it
fast for data retrieval.

This does take some time to build, however I have a working copy dumped in the
api directory.

## Requirements

    - Python 3.x

## Instructions

Install dependencies:

``` bash
sudo pip3 install -r requirements.txt
```

Ingest and create database

``` bash
python3 ingest-to-db.py
```

Once you want to use this for the api please copy it across.

``` bash
cp travel-wish-list.db ../api
```

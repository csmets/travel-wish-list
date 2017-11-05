#!/usr/bin/python3

import json
import falcon
from database import Database

class Country(object):

    def on_get(self, req, resp, country):

        db = Database()

        country_details = db.fetch('countries', 'name', country)

        resp.body = json.dumps(country_details)

        resp.content_type = 'application/json'

        resp.status = falcon.HTTP_200

class Countries(object):

    def on_get(self, req, resp):

        db = Database()

        countries_data = db.fetchall('countries')

        country_data = []

        for country in countries_data:

            country_record = dict()

            country_record['name'] = country['name']

            country_record['code'] = country['code']

            country_data.append(country_record)

        resp.body = json.dumps(country_data)

        resp.content_type = 'application/json'

        resp.status = falcon.HTTP_200

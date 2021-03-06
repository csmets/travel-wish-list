#!/usr/bin/python3

import json
import falcon
from database import Database

class City(object):

    def on_get(self, req, resp, country, city):

        db = Database()

        country_data = db.fetch('countries', 'name', country)

        country_code = country_data['code']

        if city.lower() == 'all':

            city_details = db.fetchall_match_column(
                'cities',
                'code',
                country_code)

            resp.body = json.dumps(city_details)

        else:

            city_details = db.fetchand(
                'cities',
                'name',
                city,
                'code',
                country_code)

            resp.body = json.dumps(city_details)

        resp.content_type = 'application/json'

        resp.status = falcon.HTTP_200

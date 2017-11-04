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

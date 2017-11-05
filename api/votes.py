#!/usr/bin/python3

import json
import falcon
from database import Database

class Vote:

    def on_post(self, req, resp):

        post = json.loads(req.stream.read().decode('utf-8'))

        if {'username', 'country', 'city'} <= set(post):

            db = Database()

            username = post['username']

            country = post['country']

            city = post['city']

            votes = db.fetch_votes(username, country, city) + 1

            db.insert_vote(username, country, city, votes)

            resp.status = falcon.HTTP_200

        else:

            resp.status = falcon.HTTP_422

#!/usr/bin/python3

import json
import falcon
from database import Database

class Travel:

    def on_post(self, req, resp):

        post = json.loads(req.stream.read().decode('utf-8'))

        if {'username', 'country', 'city'} <= set(post):

            db = Database()

            db.insert_travel(post['username'], post['country'], post['city'])

            resp.status = falcon.HTTP_200

        else:

            resp.status = falcon.HTTP_422


    def on_delete(self, req, resp):

        post = json.loads(req.stream.read().decode('utf-8'))

        if {'username', 'country', 'city'} <= set(post):

            db = Database()

            db.delete_travel(post['username'], post['country'], post['city'])

            resp.status = falcon.HTTP_200

        else:

            resp.status = falcon.HTTP_422

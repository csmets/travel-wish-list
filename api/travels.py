#!/usr/bin/python3

import json
import falcon
from database import Database

class Travels:

    def on_get(self, req, resp):

        db = Database()

        travels = db.fetchall('travel')

        resp.body = json.dumps(travels)

        resp.content_type = 'application/json'

        resp.status = falcon.HTTP_200

class Travel:

    def on_post(self, req, resp):

        post = json.loads(req.stream.read().decode('utf-8'))

        if {'username', 'country', 'city'} <= set(post):

            db = Database()

            travels = db.fetch_travels(post['username'])

            exists = False

            for travel in travels:

                if (travel['country'].lower() == post['country'].lower()
                        and travel['city'].lower() == post['city'].lower()):

                    exists = True

            if exists is False:

                db.insert_travel(
                    post['username'],
                    post['country'],
                    post['city'])

                resp.status = falcon.HTTP_200

            else:

                resp.status = falcon.HTTP_409

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

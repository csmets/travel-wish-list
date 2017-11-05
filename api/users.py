#!/usr/bin/python3

import json
import falcon
from database import Database

class User:

    def on_get(self, req, resp, query):

        db = Database()

        if query.lower() == 'all':
            user_data = db.fetch_users()

        else:
            user_data = db.fetch_user(query)

        resp.body = json.dumps(user_data)

        resp.content_type = 'application/json'

        resp.status = falcon.HTTP_200


    def on_post(self, req, resp, query):

        if query.lower() == 'add':

            post = json.loads(req.stream.read().decode('utf-8'))

            if 'username' in post and 'password' in post:

                db = Database()

                users = db.fetch_users()

                exists = False

                if users is not None:

                    for user in users:

                        if user['user'] == post['username']:

                            exists = True

                if exists is False:

                    db.insert_user(post['username'], post['password'])

                    resp.status = falcon.HTTP_200

                else:

                    resp.status = falcon.HTTP_409

            else:

                resp.status = falcon.HTTP_422

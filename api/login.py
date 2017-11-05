#!/usr/bin/python3

import json
import falcon
import bcrypt
from database import Database

class Login:

    def on_post(self, req, resp):

        post = json.loads(req.stream.read().decode('utf-8'))

        if 'username' in post and 'password' in post:

            db = Database()

            user = db.fetch_user_account(post['username'])

            user_password = user['password']

            if bcrypt.checkpw(post['password'].encode('utf-8'), user_password):

                resp.status = falcon.HTTP_200

            else:

                resp.status = falcon.HTTP_401

        else:

            resp.status = falcon.HTTP_422

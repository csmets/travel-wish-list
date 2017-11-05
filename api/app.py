#!/usr/bin/python3
"""
Travel wish list API

This api is used to fetch country and city data. It's also used to create and
update users.
"""

import falcon

from falcon_cors import CORS

from countries import Countries, Country

from cities import City

from users import User

from travels import Travels, Travel

from votes import Vote

from login import Login

cors = CORS(allow_origins_list=['http://localhost:8080'])

api = falcon.API(middleware=[cors.middleware])

api.add_route('/countries', Countries())

api.add_route('/country/{country}', Country())

api.add_route('/country/{country}/city/{city}', City())

api.add_route('/users/{query}', User())

api.add_route('/travel', Travel())

api.add_route('/travels', Travels())

api.add_route('/travel/vote', Vote())

api.add_route('/login', Login())

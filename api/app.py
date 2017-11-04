#!/usr/bin/python3
"""
Travel wish list API

This api is used to fetch country and city data. It's also used to create and
update users.
"""

import falcon

from countries import Country
from cities import City

api = falcon.API()

country = Country()
city = City()

api.add_route('/country/{country}', country)
api.add_route('/country/{country}/city/{city}', city)

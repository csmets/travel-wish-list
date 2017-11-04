#!/usr/bin/python3
"""
Create tables and ingest a bunch of data to be used for the travel wish list API
"""

from database_functions import (
    create_countries_table,
    create_cities_table,
    create_users_table,
    create_travel_table,
    insert_country,
    insert_city,
    show_records
)

from country_functions import insert_countries, insert_cities

"""
Create tables required for the travel wish list
"""
create_countries_table()

create_cities_table()

create_users_table()

create_travel_table()

"""
Insert all countries and cities into country table
"""
insert_countries(insert_country)
insert_cities(insert_city)

show_records('cities')

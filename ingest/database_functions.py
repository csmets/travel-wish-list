#!/usr/bin/python3
"""
Database function uses to build the database for the travel wish list
"""

import sqlite3

TESTING_DB = True # Use for testing; store in memory or to file

DB_FILE = 'travel-wish-list.db'

if TESTING_DB is True:
    conn = sqlite3.connect(':memory:')

else:
    conn = sqlite3.connect(DB_FILE)

c = conn.cursor()


def create_countries_table():

    with conn:

        c.execute("""
            CREATE TABLE countries (
                name text,
                code text,
                lat text,
                lng text,
                description text
                )""")


def create_cities_table():

    with conn:

        c.execute("""
            CREATE TABLE cities (
                name text,
                code text,
                country text,
                lat text,
                lng text,
                description text
                )""")


def create_users_table():

    with conn:

        c.execute("""
            CREATE TABLE users (
                user text,
                password text
                )""")


def create_travel_table():

    with conn:

        c.execute("""
            CREATE TABLE travel (
                user text,
                country text,
                city text,
                votes int
                )""")


def create_tables():

    create_countries_table()

    create_cities_table()

    create_users_table()

    create_travel_table()


def is_valid_record(record, keys):

    valid_record = True

    for key in keys:

        if key not in record:

            valid_record = False

            print('Missing ' + key + 'in parsed function argument')

    return valid_record


def insert_country(country):

    country_keys = [
        "name",
        "code",
        "lat",
        "lng",
        "description"
    ]

    if is_valid_record(country, country_keys) is True:

        with conn:

            c.execute("""
                INSERT INTO countries VALUES
                (:name, :code, :lat, :lng, :description)
                """, {
                    'name': country['name'],
                    'code': country['code'],
                    'lat': country['lat'],
                    'lng': country['lng'],
                    'description': country['description'],
                })


def insert_city(city):

    city_keys = [
        "name",
        "code",
        "country",
        "lat",
        "lng",
        "description"
    ]

    if is_valid_record(city, city_keys) is True:

        with conn:

            c.execute("""
                INSERT INTO cities VALUES
                (:name, :code, :country, :lat, :lng, :description)
                """, {
                    'name': city['name'],
                    'code': city['code'],
                    'country': city['country'],
                    'lat': city['lat'],
                    'lng': city['lng'],
                    'description': city['description'],
                })


def show_records(table_name):

    with conn:

        c.execute("""
            SELECT * FROM {name};
        """.format(name=table_name))

        print(c.fetchall())

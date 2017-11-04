#!/usr/bin/python3
"""
Bunch of country related function to help get extended data.
"""

import json
import requests

# Load country codes file and store into variable
countries_file = open('assets/country-codes.json')
countries = json.load(countries_file)
countries_file.close()

# Load country lat and long file and store into variable
country_latlng_file = open('assets/countrycode-latlong.json')
country_latlng = json.load(country_latlng_file)
country_latlng_file.close()

def get_country_latlng(cc):
    """ using country code find lat and long """

    cc_key = cc.lower()

    lat = country_latlng[cc_key]['lat']

    lng = country_latlng[cc_key]['long']

    return lat, lng


def get_country_code(country_name):
    """ with country name find the country code """

    for country in countries:

        if country['name'].lower() == country_name.lower():

            return country['code'].upper()


def get_country_name(country_code):
    """ using the country code, find the name """

    for country in countries:

        if country['code'].lower() == country_code.lower():

            return country['name'].capitalize()


def get_wikipedia_description(search):
    """ Using wikipedia api to fetch descriptions """

    """
    It's found that wikipedia's api is too slow that it takes a lot of time to
    ingest the data, for now I decided to deactivate this as I want this up and
    running quickly.

    Descriptions will have to be called via the app (front-end)
    """

    disable = True

    if disable is False:
        wiki_req = requests.get(
            'https://en.wikipedia.org/w/api.php'
            + '?format=json'
            + '&action=query'
            + '&prop=extracts'
            + '&exintro='
            + '&explaintext='
            + '&titles={query}'
            .format(query=search))

        response = wiki_req.json()

        pages = response['query']['pages']

        description = ""

        for value in pages.values():

            if 'extract' in value:

                description = value['extract']

            else:

                description = ""

            break

    else:

        description = ""

    return description


def insert_countries(db_func):

    for country in countries:

        record = dict()
        record['name'] = country['name']
        record['code'] = country['code']
        record['lat'], record['lng'] = get_country_latlng(country['code'])
        record['description'] = get_wikipedia_description(country['name'])

        db_func(record)


def insert_cities(db_func):

    with open('assets/cities.json') as cities_file:

        cities = json.load(cities_file)

        for city in cities:

            record = dict()
            record['name'] = city['name']
            record['code'] = city['country']
            record['country'] = get_country_name(city['country'])
            record['lat'] = city['lat']
            record['lng'] = city['lng']
            record['description'] = get_wikipedia_description(city['name'])

            db_func(record)

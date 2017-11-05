# API

API for Travel Wish List. Not to be used in production due to no authorization
model has been setup, so anonymous users can create and delete entries as they
please.

## Queries

``` bash
# list all countries with return name and country code
curl http://localhost:8000/countries

# Get country info
curl http://localhost:8000/country/<country name>

# Get city info
curl http://localhost:8000/country/<country name>/city/<city name>

# Get all cities
curl http://localhost:8000/country/<country name>/city/all

# Get user data that will return username and all travel items
curl http://localhost:8000/users/<username>

# Get all user data that will return usernames and all travel items
curl http://localhost:8000/users/all

# Get all travel items
curl https://localhost:8000/travels

# Create new user
curl -v -X POST -d '{"username": "<username>", "password": "<password>"}' http://localhost:8000/users/add

# Create new travel item
curl -v -X POST -d '{"username": "<username>", "country": "<country>", "city": "<city>"}' https://localhost:8000/travel

# Delete travel item
curl -v -X DELETE -d '{"username": "<username>", "country": "<country>", "city": "<city>"}' https://localhost:8000/travel

# Vote travel item
curl -v -X POST -d '{"username": "<username>", "country": "<country>", "city": "<city>"}' https://localhost:8000/travel/vote

# Login check
curl -v -X POST -d '{"username": "<username>", "password": "<password>"}' http://localhost:8000/login
```

## Local testing

Although it's best to run it through docker, you can test locally with gunicorn.
It's already in the requirements.txt file :)

```
pip3 install -r requirements.txt
```

```
gunicorn app:api
```

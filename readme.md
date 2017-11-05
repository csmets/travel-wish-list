# Travel Wish List Weekend Project

## Foreword
This project is an exercise to do over the weekend.

Goal is to create a wish list of travel places.

Looking up different data materials required, I found that loading up a lot of
json files is going to be slow. So, I thought it would be a good idea to build
up an api, that will help with speed.

However, the api did take some time to build causing a scramble to write up a
javascript app.

I am unhappy that I wasn't able to have time to write up any unit tests; due to
time. If I had the time, test-driving development would have help a lot with
writing the api.

This is by no means production worthy and will contains some bugs :) "it's a
feature, not a bug"

## Build

To build and preview it is required to have the following:

- Docker
- Docker compose

Linux

```
sudo bash build.sh
```

Mac
```
bash build.sh
```

## Project

Brief summary on each of the main directories. Each have their own readme.

### Ingest

Using the downloaded data, ingest it into a file based database to be used
for the api. If you require to rebuild the database, head over there. Repo comes
prebundled with it, so no need to worry and wait.

### API

Pretty much says what is does on the tin. This api is used to fetch, insert and
delete data.

### App

The web application of the Travel Wish List project.

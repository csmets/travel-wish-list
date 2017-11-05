# Travel Wish List Weekend Project

## Foreword
This project is an exercise to do over the weekend.

Goal is to create a wish list of travel places.

Looking up different data required for the project, I found that loading up a
lot of json files in a javascript web app was going to be slow. I thought it
would be a good idea to build up an api, that will help with speed.

However, the api did take some time to build causing a scramble to write up a
javascript app.

I am unhappy that I wasn't able to have time to write up any unit test, due to
time I couldn't do test-driving development as that would have help a lot with
writing the api.

This is by no means production worthy and may contains some bugs :) "it's a
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

Brief summary of each of the folders, each have their own readme.

### Ingest

Using the downloaded data ingest the data into a file base database to be used
for the api. If you require to rebuild the database, head over there.

### API

Pretty says what is does on the tin. This api is used to fetch, insert and
delete data.

### App

The web application of the Travel Wish List project.

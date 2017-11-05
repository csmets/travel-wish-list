#!/bin/bash

cd ./app
npm install
npm run build

cd ../
docker-compose up --build

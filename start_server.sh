#! /bin/bash

export $(cat .env | xargs)

cd src

uvicorn main:app --reload --host 0.0.0.0

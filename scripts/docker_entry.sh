#!/usr/bin/env bash

python3 ../manage.py makemigrations
python3 ../manage.py migrate

python3 ../start_model_servers.py &
python3 ../manage.py runserver

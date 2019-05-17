#!/bin/bash

sleep 20
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
python3 manage.py runserver 0.0.0.0:3000
# gunicorn --config /gunicorn.conf --log-config /logging.conf -b :8000 patient-management.wsgi

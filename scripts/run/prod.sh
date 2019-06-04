#!/bin/bash

sleep 20
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input
python3 manage.py loaddata core/fixtures/users.json
python3 manage.py loaddata core/fixtures/patients.json
python3 manage.py loaddata core/fixtures/triages.json
gunicorn -b :8000 patient-management.wsgi

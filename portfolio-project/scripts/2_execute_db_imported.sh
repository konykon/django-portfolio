#!/bin/bash

rm -R jobs/__pycache__
rm -R portfolio/__pycache__
rm -R jobs/migrations/__pycache__
rm -R jobs/migrations/0*
python manage.py makemigrations
python manage.py migrate

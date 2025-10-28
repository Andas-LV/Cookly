#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn cookly.wsgi:application --bind 0.0.0.0:$PORT

#!/usr/bin/env bash
set -o errexit

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py loaddata data.json
exec gunicorn vstep.wsgi:application

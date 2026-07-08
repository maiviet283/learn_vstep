#!/usr/bin/env bash
set -o errexit

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py loaddata data.json
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.update_or_create(id=1, defaults={'domain': 'vstep.vietdon.vn', 'name': 'VSTEP Master'})"
exec gunicorn vstep.wsgi:application

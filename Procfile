web: gunicorn dan_timefly_workshop.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
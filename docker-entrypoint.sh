#!/bin/bash
python manage.py migrate        # Apply database migrations
# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &
echo Starting nginx
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn cookie_wars.wsgi:application \
    --name cookie_wars \
    --bind unix:django_app.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log &
exec service nginx start

web: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py migrate
web: gunicorn general_elections.wsgi --log-file -
release: python manage.py makemigrations && python manage.py migrate --noinput
web: gunicorn bookhub.wsgi

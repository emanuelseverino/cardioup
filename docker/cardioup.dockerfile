FROM python:3.12.2-alpine
LABEL  authors="Emanuel Severino <emanuelsmseverino@gmail.com>"
RUN pip install --upgrade pip
COPY . /var/www
WORKDIR /var/www
RUN apk update && apk add zlib-dev jpeg-dev gcc musl-dev libxml2-dev libxslt-dev python3-dev postgresql-dev && pip install -r requirements.txt && python manage.py collectstatic --noinput
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 projeto.wsgi
EXPOSE 8000

# set base image (host OS)
FROM python:3.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
#ENV ALLOWED_HOSTS=127.0.0.1,[::1],0.0.0.0,.herokuapp.com

# set the working directory in the container
WORKDIR /app

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# copy the dependencies file to the working directory
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# run gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT
# set base image (host OS)
FROM python:3.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1
ENV PORT 8000
ENV SECRET_KEY (xanfn-ico)rsfcf((5fc*@$inret(k$2rmf(kevi%n@_pf!ca #docker image testing secret key


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

# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
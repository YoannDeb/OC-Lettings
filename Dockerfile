# set base image (host OS)
FROM python:3.10-alpine

## install dependencies
#RUN apk update && \
#    apk add --virtual build-deps gcc musl-dev && \
#    apk add postgresql-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ALLOWED_HOSTS=127.0.0.1,[::1],0.0.0.0,.herokuapp.com

# set the working directory in the container
WORKDIR /oc-lettings

# install dependencies
#RUN python -m venv venv
#RUN source venv/bin/activate
#RUN pip install --upgrade pip

# copy the dependencies file to the working directory
COPY requirements.txt /oc-lettings

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /oc-lettings

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
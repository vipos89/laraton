# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /var/www/site

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /var/www/site
WORKDIR /var/www/site/public
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "server:process_http_request"]
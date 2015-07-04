#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASEDIR=${SCRIPTPATH%/*}

# virtualenv environment name
VENV=sotmjp-website

export IS_PRODUCTION=false

# setup configurations; see local.py
DEBUG=false
DB_ENGINE=postgresql_psycopg2
DB_NAME=sotmjp2015
DB_HOST=localhost
DB_PORT=5432
DB_USER=ubuntu
DB_PASSWORD=fugafuga
SECRET_KEY=u'hogehoge'

export DEBUG DB_ENGINE DB_NAME DB_HOST DB_PORT DB_USER DB_PASSWORD SECRET_KEY

exec ${BASEDIR}/env/${VENV}/bin/gunicorn --chdir=${BASEDIR} \
      --bind=127.0.0.1:8000 \
      --workers=5 \
      --threads=1 \
      --env DJANGO_SETTINGS_MODULE="sotmjp.settings.production" \
      --pid=/var/run/gunicorn.pid \
      sotmjp.wsgi:application

#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASEDIR=${SCRIPTPATH%/*}

# virtualenv environment name
VENV=sotmjp-website

export IS_PRODUCTION=false

# setup configurations; see local.py
DEBUG=false
DB_ENGINE=postgresql_psycopg2
DB_NAME=sotmjp2015_staging
DB_HOST=localhost
DB_PORT=5432
DB_USER=ubuntu
DB_PASSWORD=osmfj
LANG=en-US.UTF-8
SECRET_KEY='hogehogefugafuga'

export DEBUG DB_ENGINE DB_NAME DB_HOST DB_PORT DB_USER DB_PASSWORD LANG SECRET_KEY

exec ${BASEDIR}/env/${VENV}/bin/gunicorn --chdir=${BASEDIR} \
      --bind=127.0.0.1:8001 \
      --workers=2 \
      --threads=1 \
      --env DJANGO_SETTINGS_MODULE="sotmjp.settings.staging" \
      --pid=/tmp/gunicorn-staging.pid \
      sotmjp.wsgi:application


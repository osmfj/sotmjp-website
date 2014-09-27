#!/bin/sh
BASEDIR=$(dirname $0)

# virtualenv environment name
VENV=sotmjp-website

export IS_PRODUCTION=false

# setup configurations; see local.py
DEBUG=false
DB_ENGINE=postgresql_psycopg2
DB_NAME=sotmjp2014_staging
DB_HOST=localhost
DB_PORT=5432
DB_USER=ubuntu
DB_PASSWORD=fugafuga
SECRET_KEY=u'hogehoge'

export DEBUG DB_ENGINE DB_NAME DB_HOST DB_PORT DB_USER DB_PASSWORD SECRET_KEY

cd $BASEDIR
${BASEDIR}/env/${VENV}/bin/uwsgi --chdir=${BASEDIR} \
  -s 127.0.0.1:3032  \
  --module=symposion.wsgi:application \
  --home ${BASEDIR}/env/${VENV} \
  --master \
  --pidfile=/var/run/staging-uwsgi-master.pid \
  --processes=2 \
  --daemonize=/var/log/staging-uwsgi.log

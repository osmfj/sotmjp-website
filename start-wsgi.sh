#!/bin/sh
BASEDIR=$(dirname $0)

export IS_PRODUCTION=false

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
${BASEDIR}/env/sotmjp/bin/uwsgi --chdir=${BASEDIR} \
  -s 127.0.0.1:3031  \
  --module=symposion.wsgi:application \
  --home ${BASEDIR}/env/sotmjp \
  --master \
  --pidfile=/tmp/uwsgi-master.pid \
  --processes=2 \
  --daemonize=/home/ubuntu/uwsgi.log



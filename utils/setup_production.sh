#!/bin/bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASEDIR=${SCRIPTPATH%/*}

# virtualenv environment name
VENV=sotmjp-website

DEBUG=false
DB_ENGINE=postgresql_psycopg2
DB_NAME=sotmjp2015
DB_HOST=localhost
DB_PORT=5432
DB_USER=ubuntu
DB_PASSWORD=osmfj
SECRET_KEY=u'hogehogefugafuga'

export DEBUG DB_ENGINE DB_NAME DB_HOST DB_PORT DB_USER DB_PASSWORD

IS_PRODUCTION=true
export IS_PRODUCTION

sudo -u postgres psql template1 << _SQL
CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
CREATE DATABASE $DB_NAME;
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME to $DB_USER;
\q
_SQL

${BASEDIR}/manage.py compress --force
${BASEDIR}/utils/build-css.sh
${BASEDIR}/manage.py collectstatic --noinput

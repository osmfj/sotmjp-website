#!/bin/bash

LOG_DIR=${LOG_DIR:-"/var/log/app"}
INSTALL_DIR=${INSTALL_DIR:-"/opt/pyapp/sotmjp-website"}
PROJECT_NAME=sotmjp

setupRedis () {
  # docker offical redis links with REDIS_PORT_6379_TCP_ADDR / _PORT
  REDIS_URL=redis://${REDIS_PORT_6379_TCP_ADDR}:${REDIS_PORT_6379_TCP_PORT}
}

setupDB () {

  DB_HOST=${DB_HOST:-}
  DB_PORT=${DB_PORT:-}
  DB_NAME=${DB_NAME:-}
  DB_USER=${DB_USER:-}
  DB_PASS=${DB_PASS:-}
  DB_POOL=${DB_POOL:-5}
  DB_TYPE=${DB_TYPE:-}

  # is a mysql or postgresql database linked?
  # requires that the mysql or postgresql containers have exposed
  # port 3306 and 5432 respectively.
  if [ -n "${MYSQL_PORT_3306_TCP_ADDR}" ]; then
    DB_TYPE=mysql
    DB_HOST=${DB_HOST:-${MYSQL_PORT_3306_TCP_ADDR}}
    DB_PORT=${DB_PORT:-${MYSQL_PORT_3306_TCP_PORT}}

    # support for linked sameersbn/mysql image
    DB_USER=${DB_USER:-${MYSQL_ENV_DB_USER}}
    DB_PASS=${DB_PASS:-${MYSQL_ENV_DB_PASS}}
    DB_NAME=${DB_NAME:-${MYSQL_ENV_DB_NAME}}

    # support for linked orchardup/mysql and centurylink/mysql image
    DB_USER=${DB_USER:-${MYSQL_ENV_MYSQL_USER}}
    DB_PASS=${DB_PASS:-${MYSQL_ENV_MYSQL_PASSWORD}}
    DB_NAME=${DB_NAME:-${MYSQL_ENV_MYSQL_DATABASE}}
  elif [ -n "${POSTGRESQL_PORT_5432_TCP_ADDR}" ]; then
    DB_TYPE=postgres
    DB_HOST=${DB_HOST:-${POSTGRESQL_PORT_5432_TCP_ADDR}}
    DB_PORT=${DB_PORT:-${POSTGRESQL_PORT_5432_TCP_PORT}}

    # support for linked official postgres image
    DB_USER=${DB_USER:-${POSTGRESQL_ENV_POSTGRES_USER}}
    DB_PASS=${DB_PASS:-${POSTGRESQL_ENV_POSTGRES_PASS}}
    DB_NAME=${DB_NAME:-${DB_USER}}

    # support for linked sameersbn/postgresql image
    DB_USER=${DB_USER:-${POSTGRESQL_ENV_DB_USER}}
    DB_PASS=${DB_PASS:-${POSTGRESQL_ENV_DB_PASS}}
    DB_NAME=${DB_NAME:-${POSTGRESQL_ENV_DB_NAME}}

    # support for linked orchardup/postgresql image
    DB_USER=${DB_USER:-${POSTGRESQL_ENV_POSTGRESQL_USER}}
    DB_PASS=${DB_PASS:-${POSTGRESQL_ENV_POSTGRESQL_PASS}}
    DB_NAME=${DB_NAME:-${POSTGRESQL_ENV_POSTGRESQL_DB}}

    # support for linked paintedfox/postgresql image
    DB_USER=${DB_USER:-${POSTGRESQL_ENV_USER}}
    DB_PASS=${DB_PASS:-${POSTGRESQL_ENV_PASS}}
    DB_NAME=${DB_NAME:-${POSTGRESQL_ENV_DB}}
  fi

  if [ -z "${DB_HOST}" ]; then
    echo "ERROR: "
    echo "  Please configure the database connection."
    echo "  Cannot continue without a database. Aborting..."
    exit 1
  fi

  # use default port number if it is still not set
  case "${DB_TYPE}" in
    mysql) DB_PORT=${DB_PORT:-3306} ;;
    postgres) DB_PORT=${DB_PORT:-5432} ;;
    *)
      echo "ERROR: "
      echo "  Please specify the database type in use via the DB_TYPE configuration option."
      echo "  Accepted values are \"postgres\" or \"mysql\". Aborting..."
      exit 1
      ;;
  esac

  # set the default user and database
  DB_NAME=${DB_NAME:-sotmjp_production}
  DB_USER=${DB_USER:-root}

  # XXX implement me - configure database
  case "${DB_TYPE}" in
    postgres)
#       cat > ${INSTALL_DIR}/${PROJECT_NAME}/settings/local.py << __EOL0__
#
#__EOL0__
       ;;
    mysql)
#       cat > ${INSTALL_DIR}/${PROJECT_NAME}/settings/local.py << __EOL1__
#
#__EOL1__
      ;;
    sqlite)
      ;;

    *)
      echo "Invalid database type: '$DB_TYPE'. Supported choices: [mysql, postgres]."
      exit 1
      ;;
  esac

  # due to the nature of docker and its use cases, we allow some time
  # for the database server to come online.
  case "${DB_TYPE}" in
    mysql)
      prog="mysqladmin -h ${DB_HOST} -P ${DB_PORT} -u ${DB_USER} ${DB_PASS:+-p$DB_PASS} status"
      ;;
    postgres)
      prog="pg_isready -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER} -d ${DB_NAME} -t 1"
      ;;
  esac

  timeout=60
  echo -n "Waiting for database server to accept connections"
  while ! ${prog} >/dev/null 2>&1
  do
    timeout=$(expr $timeout - 1)
    if [ $timeout -eq 0 ]; then
      echo -e "\nCould not connect to database server. Aborting..."
      exit 1
    fi
    echo -n "."
    sleep 1
  done
  echo

}

appStart () {
  exec /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
}

appHelp () {
  echo "Available options:"
  echo " app:start          - Starts the server (default)"
  echo " app:help           - Displays the help"
  echo " [command]          - Execute the specified linux command eg. bash."
  echo
  echo "Avalialble configurations through environment -e options"
  echo "database configurations"
  echo "-----------------------"
  echo "DB_TYPE, DB_HOST, DB_USER, DB_PASS, DB_NAME"
  echo "  It can ommit when using docker --link configuration"
  echo
  echo "DB_TYPE             - mysql or postgresql"
  echo "DB_HOST             - dbms host name"
  echo "DB_USER             - db user for app"
  echo "DB_PASS             - db password for DB_USER"
  echo "DB_NAME             - db name"
  echo
  echo "Optional configurations"
  echo "------------------------"
  echo "REDIS_URL           - Redis-brain support: redis://host:port"
}

case "$1" in
  app:start)
    setupDB
    setupRedis
    appStart
    ;;
  app:help)
    appHelp
    ;;
  *)
    if [ -x $1 ]; then
      $1
    else
      prog=$(which $1)
      if [ -n "${prog}" ] ; then
        shift 1
        $prog $@
      else
        appHelp
      fi
    fi
    ;;
esac

exit 0

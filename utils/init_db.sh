#!/bin/bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASEDIR=${SCRIPTPATH%/*}

# Create fresh db, load fixtures in an order that works

read -p "About to blow away DB - answer Y to go ahead, ^C to cancel> "
case $REPLY in
  Y*) ;;
  *)
   echo "Cancelling (try capital Y if you meant to go ahead)"
   exit 1
  ;;
esac

python ${BASEDIR}/manage.py syncdb --noinput
python ${BASEDIR}/manage.py migrate

python ${BASEDIR}/manage.py loaddata \
  ${BASEDIR}/fixtures/auth_user.json \
  ${BASEDIR}/fixtures/conference.json \
  ${BASEDIR}/fixtures/database_constance.json \
  ${BASEDIR}/fixtures/boxes.json \
  ${BASEDIR}/fixtures/proposals.json \
  ${BASEDIR}/fixtures/sitetree.json \
  ${BASEDIR}/fixtures/sotmjp.json \
  ${BASEDIR}/fixtures/sponsorship.json \
  ${BASEDIR}/fixtures/schedule.json \
  ${BASEDIR}/fixtures/teams.json \
  ${BASEDIR}/fixtures/restcms_page.json \

echo
echo
echo "Database initialized."
echo "Hint: setup an account with: ./manage.py createsuperuser"

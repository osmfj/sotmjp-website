#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASEDIR=${SCRIPTPATH%/*}
DUMP="python $BASEDIR/manage.py dumpdata --indent=4 --format=json"
OUTDIR=fixtures

APPS="auth.user conference database.constance boxes proposals restcms.page sitetree schedule sotmjp sponsorship teams"

for a in $APPS; do
  b=`echo $a |sed -e 's/\./_/g'`
  echo dump ${a} to $OUTDIR/${b}
  $DUMP $a > $OUTDIR/${b}.json 2>/dev/null
done

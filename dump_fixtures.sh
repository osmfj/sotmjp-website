#!/bin/sh
BASEDIR=$(dirname $0)
DUMP="$BASEDIR/manage.py dumpdata --indent=4 --format=json"
OUTDIR=fixtures

APPS="auth.user auth.permission conference database.constance boxes proposals restcms.page sitetree schedule sponsorship teams"

for a in $APPS; do
  b=`echo $a |sed -e 's/\./_/g'`
  echo dump ${a} to $OUTDIR/${b}
  $DUMP $a > $OUTDIR/${b}.json 2>/dev/null
done

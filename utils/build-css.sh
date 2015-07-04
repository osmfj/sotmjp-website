#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASEDIR=${SCRIPTPATH%/*}
mkdir -p ${BASEDIR}/sotmjp/static/css
lessc ${BASEDIR}/sotmjp/static/less/site.less \
 |  yui-compressor --type css > ${BASEDIR}/sotmjp/static/css/site.css
lessc ${BASEDIR}/sotmjp/static/less/responsive-site.less \
 |  yui-compressor --type css > ${BASEDIR}/sotmjp/static/css/responsive-site.css

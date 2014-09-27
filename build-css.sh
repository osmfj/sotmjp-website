#!/bin/sh
BASEDIR=$(dirname $0)
lessc ${BASEDIR}sotmjp/static/less/site.less \
  yui-compressor > ${BASEDIR}/sotmjp/static/css/site.css

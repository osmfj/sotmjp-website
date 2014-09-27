#!/bin/sh
BASEDIR=$(dirname $0)
lessc ${BASEDIR}/sotmjp/static/less/site.less \
 |  yui-compressor --type css > ${BASEDIR}/sotmjp/static/css/site.css
lessc ${BASEDIR}/sotmjp/static/less/responsive-site.less \
 |  yui-compressor --type css > ${BASEDIR}/sotmjp/static/css/responsive-site.css

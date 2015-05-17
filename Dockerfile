FROM ubuntu:14.04.2
MAINTAINER miurahr@osmf.jp

ENV LANG C.UTF-8
ENV PATH /usr/local/bin:${PATH}

RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get update && apt-get upgrade -y --no-install-recommends && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    make g++ gcc libc6-dev git curl\
    libssl-dev libyaml-dev libffi-dev \
    ca-certificates software-properties-common yui-compressor \
    nodejs npm \
    libpq5 sqlite3 libmysqlclient18 \
    libcurl3 libcurl3-nss libpcre3 libxml2 libxslt1.1 \
    libreadline5 libyaml-0-2\
    libmysqlclient-dev libsqlite3-dev libpq-dev \
    libcurl4-openssl-dev libpcre3-dev libxml2-dev libxslt-dev \
    libreadline-gplv2-dev \
    debhelper tk-dev python-all-dev  python-tk python-nose libfreetype6-dev \
    libjpeg-dev zlib1g-dev liblcms2-dev libwebp-dev
RUN ln -s /usr/bin/nodejs /usr/local/bin/node
RUN npm install -g npm

RUN locale-gen en_US && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales

# workaround
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype

RUN mkdir -p /opt/pyapp/sotmjp-website
COPY . /opt/pyapp/sotmjp-website/
WORKDIR /opt/pyapp/sotmjp-website

RUN apt-get install -y python-pip

RUN pip install -r requirements/dev.txt
RUN npm install -g less

# Environment prepared
# You can now do following:
#
#  python ./manage.py compress --force
#  ./build-css.sh
#  python ./manage.py collectstatic --noinput

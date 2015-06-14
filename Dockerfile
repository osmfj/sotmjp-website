FROM debian:jessie
MAINTAINER miurahr@osmf.jp

ENV PATH /usr/local/bin:${PATH}

## security upgrade and install dependencies
RUN apt-get update && apt-get upgrade -y --no-install-recommends && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    make g++ gcc libc6-dev git \
    curl libcurl3 libcurl3-nss \
    libssl-dev libyaml-dev libffi-dev \
    ca-certificates software-properties-common yui-compressor \
    libpq5 sqlite3 libmysqlclient18 \
    libpcre3 libxml2 libxslt1.1 \
    libreadline5 libyaml-0-2\
    libmysqlclient-dev libsqlite3-dev libpq-dev \
    libcurl4-openssl-dev libpcre3-dev libxml2-dev libxslt-dev \
    libreadline-gplv2-dev \
    debhelper tk-dev python-all-dev  python-tk python-nose libfreetype6-dev \
    libjpeg-dev zlib1g-dev liblcms2-dev libwebp-dev && \
    apt-get clean

## install pip and node/npm
RUN curl -sL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python - && \
    curl -sL https://deb.nodesource.com/setup | bash -

## workaround and update npm
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype && \
    npm install -g npm@latest && \
    npm install -g less

## install website source
RUN mkdir -p /opt/pyapp/sotmjp-website
COPY . /opt/pyapp/sotmjp-website/
WORKDIR /opt/pyapp/sotmjp-website

## install requirements
RUN mkdir -p /root/.pip && cp pip.conf /root/.pip/pip.conf
RUN pip install -r requirements/dev.txt

## next step user should
#    python ./manage.py compress --force
#    ./build-css.sh
#    python ./manage.py collectstatic --noinput

EXPOSE 8000

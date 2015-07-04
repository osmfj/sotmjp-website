#!/bin/sh

sudo -v -A
sudo apt-get update
sudo apt-get install -qq python-software-properties
sudo apt-get install -qq git aria2
cd /tmp
git clone https://github.com/ilikenwf/apt-fast.git
sudo cp apt-fast/apt-fast /usr/bin/
sudo chmod +x /usr/bin/apt-fast
sudo chown root.root /usr/bin/apt-fast
sudo cp apt-fast/apt-fast.conf /etc/
sudo cp apt-fast/completions/bash/apt-fast /etc/bash_completion.d/
sudo chown root.root /etc/bash_completion.d/apt-fast
sudo apt-fast update
sudo apt-fast install -y devscripts python-virtualenv
sudo apt-fast install -y postgresql libpq-dev postgresql-server-dev-9.3
sudo apt-fast install -y python-dev python-pysqlite2 libsqlite3-0
sudo apt-fast install -y nginx-full
sudo apt-fast install -y yui-compressor
sudo apt-fast -y build-dep python-imaging
#
# you should work around on Trusy and Qiana
# sudo ln -s /usr/include/freetype2 /usr/local/include/freetype
#
cd /srv
sudo mkdir sites
sudo chmod go+w sites
cd sites
git clone https://github.com/osmfj/sotmjp-website.git
cd sotmjp-website
virtualenv env/sotmjp-website
. env/sotmjp-website/bin/activate
pip install -r sotmjp/requirements/production.txt
./manage.py compress --force
./utils/build-css.sh
./manage.py collectstatic --noinput
echo next step is ./utils/init_db.sh


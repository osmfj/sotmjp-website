# -*- mode: ruby -*-
# vi: set ft=ruby :
#
# Vagrantfile for staging of State of the Map Japan 2014 website
#

require_relative "credential"
include Credential

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

# apt-fast 
$aptprepare = <<APTPREPARE
apt-get update
apt-get install -qq python-software-properties
apt-get install -qq git aria2
cd /tmp
git clone https://github.com/ilikenwf/apt-fast.git
cp apt-fast/apt-fast /usr/bin/
chmod +x /usr/bin/apt-fast
chown root.root /usr/bin/apt-fast
cp apt-fast/apt-fast.conf /etc/
cp apt-fast/completions/bash/apt-fast /etc/bash_completion.d/
chown root.root /etc/bash_completion.d/apt-fast
APTPREPARE

$dependency = <<DEPENDENCY
apt-fast update
apt-fast install -y devscripts python-virtualenv
apt-fast install -y postgresql libpq-dev postgresql-server-dev-9.3
apt-fast install -y python-dev python-pysqlite2 libsqlite3-0
apt-fast install -y nginx-full
apt-fast install -y yui-compressor
apt-fast build-dep -y python-imaging
apt-fast install -y exim4
DEPENDENCY

$setup = <<SETUP
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
./build-css.sh
./manage.py collectstatic --noinput
echo next step is ./init_db.sh
SETUP

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "dummy"

  config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: ".git/"

  config.vm.provider :aws do |aws, override|
    # private credentials
    aws.access_key_id = Access_key_id
    aws.secret_access_key = Secret_access_key
    aws.keypair_name = SSH_Key_pair_name
    override.ssh.private_key_path = SSH_Private_key_path

    # EC2 configuration
    aws.instance_type = "t2.micro"
    aws.region = "us-west-2"
    aws.availability_zone= "us-west-2b"
    aws.security_groups = "web-ssh-rds"
    aws.subnet_id = "subnet-a007edd7"
    aws.vpc_id = "vpc-7ead561b"
    aws.associate_public_ip = True
    aws.tags = {'Name' => 'sotmjp-website'}

    # Ubuntu 12.04.01(64bit) LTS (HVM)
    aws.ami = "ami-3d50120d"
    override.ssh.username = "ubuntu"
  end

  config.vm.provision "shell", inline: $aptprepare, privileged: true
  config.vm.provision "shell", inline: $dependency, privileged: true
  config.vm.provision "shell", inline: $setup, privileged: false

end

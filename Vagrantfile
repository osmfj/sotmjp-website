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
apt-fast install -y python-dev
DEPENDENCY

$setup = <<SETUP
git clone https://github.com/osmfj/symposion-jp.git
cd symposion-jp
virtualenv env/sotmjp
. env/sotmjp/bin/activate
pip install -r requirements/dev.txt
pip install -r sotmjp/requirements/projects.txt
echo please try ./load_fixtures.sh
echo then ./manage.py createsuperuser
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
    aws.instance_type = "t1.micro"
    aws.region = "us-west-2"
    aws.security_groups = "web-ssh"
    aws.tags = {'Name' => 'sotm-jp'}

    # Ubuntu 12.04.01(64bit) LTS
    aws.ami = "ami-8bb8c0bb"
    override.ssh.username = "ubuntu"
  end

  config.vm.provision "shell", inline: $aptprepare, privileged: true
  config.vm.provision "shell", inline: $dependency, privileged: true
  config.vm.provision "shell", inline: $setup, privileged: false

end

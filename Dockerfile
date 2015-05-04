
FROM ubuntu:14.04

MAINTAINER <miura@linux.com>

ENV LANG C.UTF-8

ADD sources.list /etc/apt/sources.list

RUN apt-get update && apt-get dist-upgrade -y --no-install-recommends

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \    
  g++ \
  gcc \
  libc6-dev \
  make \
  git \
  curl \
  wget \
  byobu \
  man \
  vim \
  unzip \
  language-pack-en \
  python-all-dev \
  libssl-dev \
  libyaml-dev \
  libffi-dev \
  python-sendfile \
  ca-certificates \
  software-properties-common

ENV PATH /usr/local/bin:${PATH}

RUN curl -k -O https://bootstrap.pypa.io/ez_setup.py && python ez_setup.py --insecure && rm -f ez_setup.py setuptools*zip
  
RUN DEBIAN_FRONTEND=noninteractive apt-get build-dep -y pillow && \
    curl -k -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm -f get-pip.py && \ 
    pip install \
    virtualenv \
    wheel \
    'cython==0.21.1' \
    'pyOpenSSL==0.14' \
    'greenlet==0.4.5' \
    'gevent==1.0.1' \
    'pyzmq==14.4.1' \
    'psutil==2.1.3' \
    'PyYAML==3.11' \
    'six==1.8.0' \
    'pycrypto==2.6.1' \
    'paramiko==1.15.1' \
    'Fabric==1.10.0' \
    'fabtools==0.19.0' \
    'Pillow==2.7.0' \
    pycares \
    requests

RUN locale-gen en_US && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales
    
ADD root/.bashrc /root/.bashrc
ADD root/.gitconfig /root/.gitconfig
ADD root/.scripts /root/.scripts

WORKDIR /code

RUN pip freeze

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["bash"]

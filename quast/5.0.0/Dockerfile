# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="2"
LABEL software="QUAST"
LABEL software.version="5.0.0"
LABEL description="Genome assembly evaluation tool"
LABEL website="https://github.com/ablab/quast"
LABEL license="https://github.com/ablab/quast/blob/master/LICENSE.txt"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y zlib1g-dev \
  pkg-config \
  libfreetype6-dev \
  libpng-dev \
  wget \
  g++ \
  make \
  perl \
  python \
  python-setuptools \
  python-matplotlib \
  python-pip \
  locales && \
  locale-gen en_US.UTF-8 && \
  apt-get clean && apt-get autoclean

RUN python -m pip install -U pip

RUN wget https://downloads.sourceforge.net/project/quast/quast-5.0.0.tar.gz && \
    tar -xzf quast-5.0.0.tar.gz && \
    rm -r quast-5.0.0.tar.gz

RUN cd /quast-5.0.0 && \
    /quast-5.0.0/setup.py install
RUN cd /quast-5.0.0 && \
    /quast-5.0.0/setup.py test && \
    mkdir /data

WORKDIR /data

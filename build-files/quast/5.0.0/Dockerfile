FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="3"
LABEL software="QUAST"
LABEL software.version="5.0.0"
LABEL description="Genome assembly evaluation tool"
LABEL website="https://github.com/ablab/quast"
LABEL license="https://github.com/ablab/quast/blob/master/LICENSE.txt"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

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
  python-simplejson \
  python-joblib \
  locales && \
  locale-gen en_US.UTF-8 && \
  apt-get clean && apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

RUN python -m pip install -U pip

RUN wget https://github.com/ablab/quast/releases/download/quast_5.0.0/quast-5.0.0.tar.gz && \
    tar -xzf quast-5.0.0.tar.gz && \
    rm -rf quast-5.0.0.tar.gz && \
    cd /quast-5.0.0 && \
    /quast-5.0.0/setup.py install && \
    mkdir /data

# singularity compatibility
ENV LC_ALL=C

WORKDIR /data

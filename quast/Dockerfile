# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="QUAST"
LABEL software.version="5.0.0"
LABEL description="Genome assembly evaluation tool"
LABEL website="https://github.com/ablab/quast"
LABEL license="https://github.com/ablab/quast/blob/master/LICENSE.txt"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

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
  python-matplotlib && apt-get clean && apt-get autoclean

RUN wget https://downloads.sourceforge.net/project/quast/quast-5.0.0.tar.gz && tar -xzf quast-5.0.0.tar.gz && rm -r quast-5.0.0.tar.gz
RUN cd /quast-5.0.0 && /quast-5.0.0/setup.py install
RUN cd /quast-5.0.0 && /quast-5.0.0/setup.py test && mkdir /data

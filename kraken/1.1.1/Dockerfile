# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Kraken"
LABEL software.version="1.1.1"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken"
LABEL license="https://github.com/DerrickWood/kraken/blob/master/LICENSE"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# install dependencies
RUN apt-get update && apt-get -y install \
  wget \
  zlib1g-dev \
  make \
  g++

# DL Jellyfish, unpack, and install
RUN wget https://github.com/gmarcais/Jellyfish/releases/download/v1.1.12/jellyfish-1.1.12.tar.gz && \
  tar -zxf jellyfish-1.1.12.tar.gz && rm -rf jellyfish-1.1.12.tar.gz
RUN cd jellyfish-1.1.12 && ./configure --prefix=/opt/ && make -j 4 && make install

# DL Kraken v1.0, unpack, and install
RUN wget https://github.com/DerrickWood/kraken/archive/v1.1.1.tar.gz && \
  tar -xzf v1.1.1.tar.gz && \
  rm -rf v1.1.1.tar.gz && \
  cd kraken-1.1.1 && \
  mkdir /opt/kraken && \
  ./install_kraken.sh /opt/kraken/

# DL MiniKraken database
RUN mkdir /kraken-database && \
  cd /kraken-database && \
  wget https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz && \
  tar -zxf minikraken_20171019_4GB.tgz && \
  rm -rf minikraken_20171019_4GB.tgz && mkdir /data

ENV PATH="$PATH:/opt/kraken:/opt/jellyfish/bin"
WORKDIR /data

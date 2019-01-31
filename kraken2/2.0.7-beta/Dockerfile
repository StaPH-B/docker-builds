# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Kraken2"
LABEL software.version="2.0.7-beta"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# install dependencies
RUN apt-get update && apt-get -y install \
  wget \
  zlib1g-dev \
  make \
  g++

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v2.0.7-beta.tar.gz && \
  tar -xzf v2.0.7-beta.tar.gz && \
  rm -rf v2.0.7-beta.tar.gz && \
  cd kraken2-2.0.7-beta && \
  ./install_kraken2.sh .

# DL MiniKraken2_v1_8GB database. Built from RefSeq bacteria, archaea, and viral libraries. No human.
RUN mkdir /kraken2-database && \
  cd /kraken2-database && \
  wget https://ccb.jhu.edu/software/kraken2/dl/minikraken2_v1_8GB.tgz && \
  tar -zxf minikraken2_v1_8GB.tgz && \
  rm -rf minikraken2_v1_8GB.tgz && \
  mkdir /data

ENV PATH="$PATH:/kraken2-2.0.7-beta"
WORKDIR /data

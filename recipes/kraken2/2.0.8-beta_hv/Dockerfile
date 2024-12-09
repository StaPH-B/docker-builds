# base image
FROM ubuntu:xenial

# Of note, most of this is taken from Curtis Kapsak's Dockerfile, with the only difference being the kraken2 database

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL dockerfile.version="1.hv"
LABEL software="Kraken2"
LABEL software.version="2.0.8-beta"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
  wget \
  zlib1g-dev \
  make \
  g++

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v2.0.8-beta.tar.gz && \
  tar -xzf v2.0.8-beta.tar.gz && \
  rm -rf v2.0.8-beta.tar.gz && \
  cd kraken2-2.0.8-beta && \
  ./install_kraken2.sh . && \
  mkdir /data

ENV PATH="$PATH:/kraken2-2.0.8-beta" \
    LC_ALL=C

WORKDIR /data

# Download kraken2 human + virus db. Details are found at https://storage.googleapis.com/sars-cov-2/kraken2_methods.txt. Contains human and viral sequence.
RUN mkdir /kraken2-db && \
  cd /kraken2-db && \
  wget https://storage.googleapis.com/sars-cov-2/kraken2_h%2Bv_20200319.tar.gz && \
  tar -zxf kraken2_h+v_20200319.tar.gz && \
  rm -rf kraken2_h+v_20200319.tar.gz

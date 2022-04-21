ARG KRAKEN2_VER="2.0.8-beta"

# base image
FROM ubuntu:xenial as app
ARG KRAKEN2_VER

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Kraken2"
LABEL software.version=$KRAKEN2_VER
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
  wget \
  zlib1g-dev \
  make \
  g++

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v$KRAKEN2_VER.tar.gz && \
  tar -xzf v$KRAKEN2_VER.tar.gz && \
  rm -rf v$KRAKEN2_VER.tar.gz && \
  cd kraken2-$KRAKEN2_VER && \
  ./install_kraken2.sh . && \
  mkdir /data

ENV PATH="$PATH:/kraken2-$KRAKEN2_VER" \
    LC_ALL=C

WORKDIR /data

# DL MiniKraken2_v1_8GB database. Built from RefSeq bacteria, archaea, and viral libraries. No human.
RUN mkdir /kraken2-db && \
  cd /kraken2-db && \
  wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_8gb_20210517.tar.gz && \
  tar -zxf k2_standard_8gb_20210517.tar.gz && \
  rm -rf k2_standard_8gb_20210517.tar.gz

FROM app as test
ARG KRAKEN2_VER

# Run test script
COPY test.sh .
RUN bash test.sh $KRAKEN2_VER
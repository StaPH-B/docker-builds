FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during build time.
ARG K2VER="2.0.9-beta"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Kraken2"
LABEL software.version="2.0.9-beta"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies and cleanup apt garbage
RUN apt-get update && apt-get -y --no-install-recommends install \
 wget \
 ca-certificates \
 zlib1g-dev \
 make \
 g++ && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v${K2VER}.tar.gz && \
 tar -xzf v${K2VER}.tar.gz && \
 rm -rf v${K2VER}.tar.gz && \
 cd kraken2-${K2VER} && \
 ./install_kraken2.sh . && \
 mkdir /data

ENV PATH="$PATH:/kraken2-${K2VER}" \
    LC_ALL=C

WORKDIR /data

# DL MiniKraken2_8GB database. Built from RefSeq bacteria, archaea, viral, and human libraries
# --strip-components=1 used so that the *.k2d files end up inside /kraken2-db and not another directory
RUN mkdir /kraken2-db && \
 cd /kraken2-db && \
 wget https://genome-idx.s3.amazonaws.com/kraken/minikraken2_v2_8GB_201904.tgz && \
 tar -zxf minikraken2_v2_8GB_201904.tgz --strip-components=1 && \
 rm -rf minikraken2_v2_8GB_201904.tgz

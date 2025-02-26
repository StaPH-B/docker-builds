FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="Kraken2"
LABEL software.version="2.0.8-beta"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies, cleanup apt garbage
RUN apt-get update && apt-get -y install \
 wget \
 zlib1g-dev \
 make \
 g++ \ 
 rsync \
 cpanminus && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# perl module required for kraken2-build
RUN cpanm Getopt::Std

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

### NO DB FOR THIS DOCKER IMAGE - USER WILL NEED TO MOUNT A VOLUME WITH THEIR PREFERRED KRAKEN DATABASE ###

# DL MiniKraken2_v1_8GB database. Built from RefSeq bacteria, archaea, and viral libraries. No human.
#RUN mkdir /kraken2-db && \
#  cd /kraken2-db && \
#  wget ftp://ftp.ccb.jhu.edu/pub/data/kraken2_dbs/minikraken2_v1_8GB_201904_UPDATE.tgz && \
#  tar -zxf minikraken2_v1_8GB_201904_UPDATE.tgz && \
#  rm -rf minikraken2_v1_8GB_201904_UPDATE.tgz

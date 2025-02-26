FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Kraken"
LABEL software.version="1.1.1"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken"
LABEL license="https://github.com/DerrickWood/kraken/blob/master/LICENSE"
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
 rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get autoclean

# this perl module and rsync required for kraken-build
RUN cpanm --force --notest Getopt::Std

# DL Jellyfish, unpack, and install
RUN wget https://github.com/gmarcais/Jellyfish/releases/download/v1.1.12/jellyfish-1.1.12.tar.gz && \
 tar -zxf jellyfish-1.1.12.tar.gz && \
 rm -rf jellyfish-1.1.12.tar.gz && \
 cd jellyfish-1.1.12 && \
 ./configure --prefix=/opt/ && \
 make -j 4 && \
 make install

# DL Kraken v1.1.1, unpack, and install
RUN wget https://github.com/DerrickWood/kraken/archive/v1.1.1.tar.gz && \
  tar -xzf v1.1.1.tar.gz && \
  rm -rf v1.1.1.tar.gz && \
  cd kraken-1.1.1 && \
  mkdir /opt/kraken && \
  ./install_kraken.sh /opt/kraken/ && \
  mkdir /data

ENV PATH="$PATH:/opt/kraken:/opt/bin" \
    LC_ALL=C
WORKDIR /data

### NO DB FOR THIS DOCKER IMAGE - USER WILL NEED TO MOUNT A VOLUME WITH THEIR PREFERRED KRAKEN DATABASE ###

# DL MiniKraken database
#RUN mkdir /kraken-database && \
#  cd /kraken-database && \
#  wget https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz && \
#  tar -zxf minikraken_20171019_4GB.tgz && \
#  rm -rf minikraken_20171019_4GB.tgz

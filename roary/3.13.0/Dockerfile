FROM ubuntu:focal

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2"
LABEL software="Roary"
LABEL software.version="3.13.0"
LABEL description="Rapid large-scale prokaryotic pan genome analysis"
LABEL website="https://github.com/sanger-pathogens/Roary"
LABEL license="https://github.com/sanger-pathogens/Roary/blob/master/GPL-LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# so apt doesn't ask questions
ARG DEBIAN_FRONTEND=noninteractive

# install roary 3.13.0 via apt; cleanup apt garbage; make /data and /kraken_db
RUN apt-get update && apt-get install -y --no-install-recommends roary \
 wget \
 zlib1g-dev \
 make \
 g++ \
 rsync \
 cpanminus && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/* && \
 mkdir /data /kraken_db

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
  ./install_kraken.sh /opt/kraken/

WORKDIR /data
# set perl locale settings and PATH
ENV LC_ALL=C.UTF-8 \
 PATH="$PATH:/opt/kraken:/opt/bin"

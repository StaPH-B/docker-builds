# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Mash"
LABEL software.version="2.1.0"
LABEL description="Fast genome and metagenome distance estimation using MinHash"
LABEL website="https://mash.readthedocs.io/en/latest/index.html"
LABEL license="https://github.com/marbl/Mash/blob/master/LICENSE.txt"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# install dependencies
RUN apt-get update && apt-get -y install wget \
    libgsl-dev \
    libgsl2 \
    autoconf \
    automake \
    git \
    g++ \
    make \
    libz-dev \
    libtool \
    curl && \
    apt-get clean

# Capn'P download and install
RUN curl -O https://capnproto.org/capnproto-c++-0.6.1.tar.gz;\
 tar -xzf capnproto-c++-0.6.1.tar.gz;\
 cd capnproto-c++-0.6.1;\
 ./configure;\
 make -j6 check;\
 make install

# make database directory, store mash db there
RUN mkdir /db && \
  cd /db && \
  wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
  gunzip RefSeqSketchesDefaults.msh.gz

RUN wget https://github.com/marbl/Mash/archive/v2.1.tar.gz && \
  tar -xvf v2.1.tar.gz;\
  rm -rf v2.1.tar.gz;\
  cd Mash-2.1/; \
  ./bootstrap.sh;\
  ./configure;\
  make;\
  make install;\
  mkdir /data

WORKDIR /data

# path to Mash RefSeq k=21 s=1000 sketches database: /db/RefSeqSketchesDefaults.msh

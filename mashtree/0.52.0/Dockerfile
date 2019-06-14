# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="mashtree"
LABEL software.version="0.52.0"
LABEL description="Create a tree using Mash distances."
LABEL website="https://github.com/lskatz/mashtree"
LABEL license="https://github.com/lskatz/mashtree/blob/master/LICENSE"

MAINTAINER Jake Garfin <jake.garfin@state.mn.us>

# install dependencies
RUN apt-get update && \
  apt-get -y install \
    perl \
    bioperl \
    build-essential \
    sqlite3 \
    libjson-perl \
    make \
    wget && \
  apt-get clean


# install mash
RUN wget https://github.com/marbl/Mash/releases/download/v2.1/mash-Linux64-v2.1.tar && \
  tar -xvf mash-Linux64-v2.1.tar && \
  rm -rf mash-Linux64-v2.1.tar

# install quicktree
RUN wget https://github.com/khowe/quicktree/archive/v2.5.tar.gz && \
  tar -xvf v2.5.tar.gz && \
  rm -rf v2.5.tar.gz && \
  cd quicktree-2.5 && \
  make quicktree

# add mash and quicktree to the path to allow mashtree to pass tests
ENV PATH="${PATH}:/mash-Linux64-v2.1:/quicktree-2.5"

# install mashtree
RUN wget https://github.com/lskatz/mashtree/archive/v0.52.tar.gz && \
  tar -xvf v0.52.tar.gz && \
  rm -rf v0.52.tar.gz && \
  cd mashtree-0.52/ && \
  perl Makefile.PL && \
  make test && \
  mkdir /data

ENV PATH="${PATH}:/mashtree-0.52/bin"

WORKDIR /data

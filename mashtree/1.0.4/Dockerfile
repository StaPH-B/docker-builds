# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="mashtree"
LABEL software.version="1.0.4"
LABEL description="Create a tree using Mash distances"
LABEL website="https://github.com/lskatz/mashtree"
LABEL license="https://github.com/lskatz/mashtree/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
  perl \
  build-essential \
  sqlite3 \
  libsqlite3-dev \
  libjson-perl \
  make \
  wget \
  cpanminus \
  libexpat1-dev && apt-get clean

# install perl modules
RUN cpanm --notest BioPerl \
  Bio::Sketch::Mash \
  DBD::SQLite \
  DBI \
  File::Which

# install mash
RUN wget https://github.com/marbl/Mash/releases/download/v2.2/mash-Linux64-v2.2.tar && \
  tar -xvf mash-Linux64-v2.2.tar && \
  rm -rf mash-Linux64-v2.2.tar

# install quicktree
RUN wget https://github.com/khowe/quicktree/archive/v2.5.tar.gz && \
  tar -xvf v2.5.tar.gz && \
  rm -rf v2.5.tar.gz && \
  cd quicktree-2.5 && \
  make quicktree

# add mash and quicktree to the path to allow mashtree to pass tests
ENV PATH="${PATH}:/mash-Linux64-v2.2:/quicktree-2.5"

# install mashtree
RUN wget https://github.com/lskatz/mashtree/archive/v1.0.4.tar.gz && \
  tar -xvf v1.0.4.tar.gz && \
  rm -rf v1.0.4.tar.gz && \
  cd mashtree-1.0.4/ && \
  perl Makefile.PL && \
  mkdir /data

ENV PATH="${PATH}:/mashtree-1.0.4/bin"

# set perl locale settings
ENV LC_ALL=C

WORKDIR /data

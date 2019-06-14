FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Samtools"
LABEL software.version="1.9"
LABEL description="Tools (written in C using htslib) for manipulating next-generation sequencing data"
LABEL website="https://github.com/samtools/samtools"
LABEL lisence="https://github.com/samtools/samtools/blob/develop/LICENSE"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y libncurses5-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  zlib1g-dev \
  libssl-dev \
  gcc \
  wget \
  make \
  perl \
  bzip2

RUN mkdir samtools &&\
  mkdir data &&\
  cd samtools &&\
  wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 &&\
  tar -xjf samtools-1.9.tar.bz2 &&\
  rm samtools-1.9.tar.bz2 &&\
  cd samtools-1.9 &&\
  ./configure &&\
  make &&\
  make install

WORKDIR /data

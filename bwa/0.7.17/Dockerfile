FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="BWA"
LABEL software.version="0.7.17"
LABEL description="Burrow-Wheeler Aligner for short-read alignment"
LABEL website="https://github.com/lh3/bwa"
LABEL lisence="https://github.com/lh3/bwa/blob/master/COPYING"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y make \
  wget \
  gcc \
  zlib1g-dev \
  bzip2

RUN mkdir bwa &&\
  mkdir /data &&\
  cd bwa &&\
  wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2 &&\
  tar -xjf bwa-0.7.17.tar.bz2 &&\
  rm bwa-0.7.17.tar.bz2 &&\
  cd bwa-0.7.17 &&\
  make

ENV PATH="${PATH}:/bwa/bwa-0.7.17"
WORKDIR /data

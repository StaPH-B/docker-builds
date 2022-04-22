ARG BWA_VER="0.7.17"

FROM ubuntu:xenial as app
ARG BWA_VER

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="BWA"
LABEL software.version=$BWA_VER
LABEL description="Burrows-Wheeler Aligner for short-read alignment"
LABEL website="https://github.com/lh3/bwa"
LABEL license="https://github.com/lh3/bwa/blob/master/COPYING"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Sarah Nadeau"
LABEL maintainer2.email="sarah.nadeau@bsse.ethz.ch"

RUN apt-get update && apt-get install -y make \
  wget \
  gcc \
  zlib1g-dev \
  bzip2

RUN mkdir bwa &&\
  mkdir /data &&\
  cd bwa &&\
  wget https://github.com/lh3/bwa/releases/download/v$BWA_VER/bwa-$BWA_VER.tar.bz2 &&\
  tar -xjf bwa-$BWA_VER.tar.bz2 &&\
  rm bwa-$BWA_VER.tar.bz2 &&\
  cd bwa-$BWA_VER &&\
  make

ENV PATH="${PATH}:/bwa/bwa-$BWA_VER"
WORKDIR /data

FROM app as test
ARG BWA_VER

# Run test script
COPY test.sh .
RUN bash test.sh $BWA_VER

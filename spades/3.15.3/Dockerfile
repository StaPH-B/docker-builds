# to make it easier to upgrade for new versions; ARG variables only persist during docker image build time
ARG SPADES_VER=3.15.3

FROM ubuntu:xenial as app
ARG SPADES_VER

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="SPAdes"
LABEL software.version=$SPADES_VER
LABEL description="de novo DBG genome assembler"
LABEL website="https://github.com/ablab/spades"
LABEL license="https://github.com/ablab/spades/blob/v3.15.3/assembler/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Sarah Nadeau"
LABEL maintainer2.email="sarah.nadeau@bsse.ethz.ch"

# install dependencies; cleanup apt garbage
# python v2.7.12 is installed here
RUN apt-get update && apt-get install -y python \
 wget && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# install SPAdes binary; make /data
RUN wget http://cab.spbu.ru/files/release${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm -r SPAdes-${SPADES_VER}-Linux.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C \
    PATH="${PATH}:/SPAdes-${SPADES_VER}-Linux/bin"

WORKDIR /data

FROM app as test
ARG SPADES_VER

# Run test script
COPY test.sh .
RUN bash test.sh $SPADES_VER

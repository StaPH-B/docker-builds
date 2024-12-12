FROM ubuntu:xenial

# to make it easier to upgrade for new versions; ARG variables only persist during docker image build time
ARG SPAdesVer=3.15.0

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="SPAdes"
LABEL software.version="3.15.0"
LABEL description="de novo DBG genome assembler"
LABEL website="https://github.com/ablab/spades"
LABEL license="https://github.com/ablab/spades/blob/v3.15.0/assembler/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y python \
 wget && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# install SPAdes binary; make /data
RUN wget http://cab.spbu.ru/files/release${SPAdesVer}/SPAdes-${SPAdesVer}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPAdesVer}-Linux.tar.gz && \
  rm -r SPAdes-${SPAdesVer}-Linux.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C \
    PATH="${PATH}:/SPAdes-${SPAdesVer}-Linux/bin"

WORKDIR /data

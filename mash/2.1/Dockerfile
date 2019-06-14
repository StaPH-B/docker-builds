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
RUN apt-get update && \
    apt-get -y install wget && \
    apt-get clean

RUN wget https://github.com/marbl/Mash/releases/download/v2.1/mash-Linux64-v2.1.tar && \
  tar -xvf mash-Linux64-v2.1.tar && \
  rm -rf mash-Linux64-v2.1.tar && \
  mkdir /data && \
  # make database directory, store mash db there
  mkdir /db && \
  cd /db && \
  wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
  gunzip RefSeqSketchesDefaults.msh.gz

ENV PATH="${PATH}:/mash-Linux64-v2.1"

WORKDIR /data

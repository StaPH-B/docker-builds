# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Mash"
LABEL software.version="2.2"
LABEL description="Fast genome and metagenome distance estimation using MinHash"
LABEL website="https://mash.readthedocs.io/en/latest/index.html"
LABEL license="https://github.com/marbl/Mash/blob/master/LICENSE.txt"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && \
    apt-get -y install wget && \
    apt-get clean

RUN wget https://github.com/marbl/Mash/releases/download/v2.2/mash-Linux64-v2.2.tar && \
    tar -xvf mash-Linux64-v2.2.tar && \
    rm -rf mash-Linux64-v2.2.tar && \
    mkdir /data

# add mash to path, and set perl locale settings
ENV PATH="${PATH}:/mash-Linux64-v2.2" \
    LC_ALL=C

WORKDIR /data

# make db dir. Store db there. Better to have db's added in the last layers
RUN mkdir /db && \
    cd /db && \
    wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
    gunzip RefSeqSketchesDefaults.msh.gz

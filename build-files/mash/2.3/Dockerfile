FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during image build time
ARG MASH_VER="2.3"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Mash"
LABEL software.version="2.3"
LABEL description="Fast genome and metagenome distance estimation using MinHash"
LABEL website="https://mash.readthedocs.io/en/latest/index.html"
LABEL license="https://github.com/marbl/Mash/blob/master/LICENSE.txt"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \ 
 wget && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# download mash binary; make /data
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
 tar -xvf mash-Linux64-v${MASH_VER}.tar && \
 rm -rf mash-Linux64-v${MASH_VER}.tar && \
 mkdir /data

# add mash to path, and set perl locale settings
ENV PATH="${PATH}:/mash-Linux64-v${MASH_VER}" \
 LC_ALL=C

WORKDIR /data

# make db dir. Store db there. Better to have db's added in the last layers
RUN mkdir /db && \
 cd /db && \
 wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
 gunzip RefSeqSketchesDefaults.msh.gz

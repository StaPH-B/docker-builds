FROM ubuntu:focal

ARG SEROTYPEFINDER_VER="2.0.1"
ARG SEROTYPEFINDER_DB_COMMIT_HASH="39c68c6e1a3d94f823143a2e333019bb3f8dddba"

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SerotypeFinder"
LABEL software.version="2.0.1"
LABEL description="Tool for identifying the serotype of E. coli from reads or assemblies"
LABEL website="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies; cleanup apt garbage 
# ncbi-blast+ v2.9.0 (ubuntu:focal), min required version is 2.8.1
# python3 v3.8.5, min required version is 3.5
RUN apt-get update && apt-get install -y \
 wget \
 git \
 ncbi-blast+ \
 python3 \
 python3-pip \
 libz-dev && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install python dependencies
RUN pip3 install biopython==1.73 tabulate==0.7.7 cgecore==1.3.2

# Install kma
# apt deps: libz-dev (for compiling) 
RUN git clone --branch 1.0.1 --depth 1 https://bitbucket.org/genomicepidemiology/kma.git && \
 cd kma && \
 make && \
 mv -v kma* /usr/local/bin/

# download serotypefinder database using a specific commit hash to aid in reproducibility
# index database w/ kma
# NOTE: files HAVE to go into '/database' since that is the default location expected by serotyperfinder.py
RUN mkdir /database && \
 git clone https://bitbucket.org/genomicepidemiology/serotypefinder_db.git /database && \
 cd /database && \
 git checkout ${SEROTYPEFINDER_DB_COMMIT_HASH} && \
 python3 INSTALL.py kma_index

# install serotypefinder; make /data
RUN git clone --branch ${SEROTYPEFINDER_VER} https://bitbucket.org/genomicepidemiology/serotypefinder.git && \
 mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="/serotypefinder:$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

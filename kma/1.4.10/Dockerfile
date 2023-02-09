# base image
FROM ubuntu:jammy as app

ARG KMAVER="1.4.10"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL container.version="2"
LABEL software="kma"
LABEL software.version="$KMAVER"
LABEL description="K-mer alignment of raw reads against a database"
LABEL website="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license.type="Apache License, V2.0"
LABEL maintainer="Eetu Eklund"
LABEL maintainer.email="eetu.eklund@maryland.gov"

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libz-dev \
  make \
  ca-certificates \
  git && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN git clone https://bitbucket.org/genomicepidemiology/kma.git && \
  cd kma && \
  git fetch && \
  git checkout $KMAVER && \
  make && \
  mkdir data

ENV PATH="$PATH:/kma" \
    LC_ALL=C

WORKDIR data

# test stage
FROM app as test 

WORKDIR test 

##### NO DATABASE INCLUDED WITH THIS DOCKER IMAGE #####
## User will need to mount a directory from their host machine that contains database files
## KMA is a mapping method designed to map raw reads directly against redundant databases
## Here is example usage of mounting volumes when running container:
## kma -ipe SRR13957123_*.fastq.gz -o test.output -t_db DB_name && \
## Here are the links to example read files:
## https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
## https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
RUN kma -h && kma -v

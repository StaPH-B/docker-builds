# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SISTR"
LABEL software.version="1.0.2"
LABEL description="Salmonella In Silico Typing Resource (SISTR)"
LABEL website="https://github.com/peterk87/sistr_cmd"
LABEL license="https://github.com/peterk87/sistr_cmd/blob/master/LICENSE"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# install dependencies using conda
RUN apt-get update && apt-get -y install \
 python-pip \
 python-dev \
 build-essential \
 ncbi-blast+ \
 mafft && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN python -m pip install wheel numpy pandas sistr_cmd && mkdir /data

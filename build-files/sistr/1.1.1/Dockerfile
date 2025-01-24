FROM ubuntu:xenial

ARG SISTR_VER="1.1.1"
ARG MASH_VER="2.2"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="SISTR"
LABEL software.version="1.1.1"
LABEL description="Salmonella In Silico Typing Resource (SISTR)"
LABEL website="https://github.com/peterk87/sistr_cmd"
LABEL license="https://github.com/peterk87/sistr_cmd/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies; cleanup apt garbage
# ncbi-blast = 2.2.31
# mafft = 7.271
RUN apt-get update && apt-get -y --no-install-recommends install \
 python-pip \
 python-dev \
 python-setuptools \
 build-essential \
 wget \
 curl \
 libssl-dev \
 libcurl4-openssl-dev \
 ncbi-blast+ \
 mafft && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install mash
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
    tar -xvf mash-Linux64-v${MASH_VER}.tar && \
    rm -rf mash-Linux64-v${MASH_VER}.tar

# upgrade pip first; install python deps and SISTR
# apt dependencies: curl libssl-dev libcurl4-openssl-dev
RUN python -m pip install --upgrade pip && \
 python -m pip install wheel numpy pandas sistr_cmd==${SISTR_VER} && \
 mkdir /data

# set working directory, PATH, and locale settings for singularity (just in case)
WORKDIR /data
ENV LC_ALL=C \
 PATH="${PATH}:/mash-Linux64-v${MASH_VER}"

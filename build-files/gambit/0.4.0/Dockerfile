FROM ubuntu:xenial

ARG GAMBIT_SOFTWARE_VERSION="0.4.0"
ARG GAMBIT_GIT_REF=v${GAMBIT_SOFTWARE_VERSION}
ARG GAMBIT_GIT_URL=github.com/hesslab-gambit/gambit@${GAMBIT_GIT_REF}
ARG GAMBIT_DB_BASE_URL=https://storage.googleapis.com/theiagen-public-files/terra/gambit_files/1.0b2
ARG GAMBIT_DB_GENOMES_URL=$GAMBIT_DB_BASE_URL/gambit-genomes-1.0b2-rev2-211116.db
ARG GAMBIT_DB_SIGNATURES_URL=$GAMBIT_DB_BASE_URL/gambit-signatures-1.0b1-210719.h5
ARG MINICONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ARG PYTHON_VERSION=3.9

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="3"
LABEL software="GAMBIT"
LABEL software.version=${GAMBIT_SOFTWARE_VERSION}
LABEL description="Rapid genomic-distance comparison for taxonomic identification of microbial pathogens"
LABEL website="https://github.com/hesslab-gambit/gambit"
LABEL license="https://github.com/hesslab-gambit/gambit/blob/master/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@theiagen.com"

# Environment
ENV GAMBIT_DB_PATH=/gambit-db
ENV LC_ALL=C.UTF-8

# Fetch files
ADD $MINICONDA_URL miniconda.sh
RUN mkdir $GAMBIT_DB_PATH
ADD $GAMBIT_DB_GENOMES_URL $GAMBIT_DB_PATH/
ADD $GAMBIT_DB_SIGNATURES_URL $GAMBIT_DB_PATH/
RUN chmod -R a+rx $GAMBIT_DB_PATH

# install c compiler & needed software for conda install; cleanup apt garbage
RUN apt-get update && \
  apt-get install -y \
    wget \
    gcc \
    git \
    build-essential \
    && \
  apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

# Install miniconda
RUN bash ./miniconda.sh -p /miniconda -b && \
  rm miniconda.sh

# Create conda environment and add to PATH
RUN /miniconda/bin/conda create -n gambit python=$PYTHON_VERSION numpy Cython
ENV PATH="/miniconda/envs/gambit/bin:/miniconda/bin:$PATH"

# Install GAMBIT package
RUN pip install git+https://${GAMBIT_GIT_URL} && \
  conda clean -a -y

# Working directory
RUN mkdir /data
WORKDIR /data

FROM ubuntu:xenial

# Version arguments
ARG GAMBIT_SOFTWARE_VERSION="0.3.0"
ARG GAMBIT_DB_VERSION="1.0b1-210719"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
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
ADD https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh miniconda.sh
RUN mkdir $GAMBIT_DB_PATH
ADD https://storage.googleapis.com/hesslab-gambit-public/databases/refseq-curated/1.0-beta/gambit-genomes-${GAMBIT_DB_VERSION}.db $GAMBIT_DB_PATH/
ADD https://storage.googleapis.com/hesslab-gambit-public/databases/refseq-curated/1.0-beta/gambit-signatures-${GAMBIT_DB_VERSION}.h5 $GAMBIT_DB_PATH/

# install c compiler & needed software for conda install
RUN apt-get update && apt-get install -y \
  wget \
  gcc \
  git \
  build-essential

# get miniconda
RUN bash ./miniconda.sh -p /miniconda -b  &&\
    rm miniconda.sh

# Create conda environment and add to PATH
RUN /miniconda/bin/conda create -n gambit python=3.9 numpy Cython
ENV PATH="/miniconda/envs/gambit/bin:$PATH"

# Install GABMIT package
RUN pip install git+https://github.com/hesslab-gambit/gambit@v${GAMBIT_SOFTWARE_VERSION}

# set working directory to /data
RUN mkdir /data
WORKDIR /data


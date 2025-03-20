ARG PIRANHA_VER="1.4.2"

FROM mambaorg/micromamba:2.0.5-ubuntu22.04 AS app

ARG PIRANHA_VER

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# metadata labels
LABEL base.image="mambaorg/micromamba:2.0.5-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="piranha"
LABEL software.version=${PIRANHA_VER}
LABEL description="Poliovirus Investigation Resource Automating Nanopore Haplotype Analysis"
LABEL website="https://github.com/polio-nanopore/piranha"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/polio-nanopore/piranha/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"
LABEL maintainer2="James Otieno"
LABEL maintainer2.email="james.otieno@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    build-essential && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the piranha code repo; creating conda environment using environment.yml supplied w/ Piranha code
RUN wget -q https://github.com/polio-nanopore/piranha/archive/refs/tags/${PIRANHA_VER}.tar.gz && \
    tar -xf ${PIRANHA_VER}.tar.gz && \
    micromamba create -n piranha -y -f /piranha-${PIRANHA_VER}/environment.yml && \
    /opt/conda/envs/piranha/bin/pip install ${PIRANHA_VER}.tar.gz --no-cache-dir && \
    rm ${PIRANHA_VER}.tar.gz && \
    mkdir /data 

# final working directory is /data
WORKDIR /data

# hardcode piranha executable into the PATH variable
ENV PATH="${PATH}:/opt/conda/envs/piranha/bin/" \
    LC_ALL=C.UTF-8

RUN pip install pyabpoa

CMD ["piranha" ,"--help"]

# new base image for testing
FROM app AS test

ARG PIRANHA_VER

# print help and version 
RUN piranha --help && piranha --version

# set up testing environment
WORKDIR /test

# test on test sequences supplied with Piranha code; shamelessly stolen and modified from https://github.com/polio-nanopore/piranha/blob/main/.github/workflows/piranha.yml
# first test is a subset that analyzes 2 barcodes (05 and 07)
# second test analyzes all test data supplied with Piranha code (7 barcodes)
RUN piranha -i /piranha-${PIRANHA_VER}/piranha/test/pak_run/demultiplexed --verbose -b /piranha-${PIRANHA_VER}/piranha/test/pak_run/barcodes01.csv -t 2 2>&1 | tee piranha.log && \
    piranha -i /piranha-${PIRANHA_VER}/piranha/test/pak_run/demultiplexed --verbose -b /piranha-${PIRANHA_VER}/piranha/test/pak_run/barcodes.csv -t 2 2>&1 | tee piranha_all.log

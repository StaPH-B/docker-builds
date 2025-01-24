FROM mambaorg/micromamba:0.27.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
ARG PIRANHA_VER="1.0.4"

# metadata labels
LABEL base.image="mambaorg/micromamba:0.27.0"
LABEL dockerfile.version="1"
LABEL software="piranha"
LABEL software.version=${PIRANHA_VER}
LABEL description="Poliovirus Investigation Resource Automating Nanopore Haplotype Analysis"
LABEL website="https://github.com/cov-lineages/piranha"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/polio-nanopore/piranha/blob/main/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="curtis.kapsak@theiagen.com"
LABEL maintainer2="James Otieno"
LABEL maintainer2.email="james.otieno@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 git \
 procps \
 build-essential && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the piranha code repo; creating conda environment using environment.yml supplied w/ Piranha code
RUN wget "https://github.com/polio-nanopore/piranha/archive/refs/tags/${PIRANHA_VER}.tar.gz" && \
 tar -xf ${PIRANHA_VER}.tar.gz && \
 rm ${PIRANHA_VER}.tar.gz && \
 mv -v piranha-* piranha && \
 micromamba create -n piranha -y -f /piranha/environment.yml

# set the environment; PATH unneccessary at this point, for easy changes later; LC_ALL is for singularity compatibility
ENV PATH="${PATH}" \
 LC_ALL=C.UTF-8

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="piranha"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /piranha

# run pip install step
# clean up micromamba/conda garbage
# make /data directory
RUN pip install . && \
 micromamba clean -a -y && \
 mkdir /data 

# final working directory is /data
WORKDIR /data

# hardcode piranha executable into the PATH variable
ENV PATH="${PATH}:/opt/conda/envs/piranha/bin/"

# new base image for testing
FROM app as test

# # so that mamba/conda env is active when running below commands
ENV ENV_NAME="piranha"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# print help and version 
RUN piranha --help && piranha --version

# set up testing environment
WORKDIR /piranha

# test on test sequences supplied with Piranha code; shamelessly stolen and modified from https://github.com/polio-nanopore/piranha/blob/main/.github/workflows/piranha.yml
# first test is a subset that analyzes 2 barcodes (05 and 07)
# second test analyzes all test data supplied with Piranha code (7 barcodes)
RUN piranha -i piranha/test/pak_run/demultiplexed --verbose -b piranha/test/pak_run/barcodes01.csv -t 2 2>&1 | tee piranha.log && \
 piranha -i piranha/test/pak_run/demultiplexed --verbose -b piranha/test/pak_run/barcodes.csv -t 2 2>&1 | tee piranha_all.log

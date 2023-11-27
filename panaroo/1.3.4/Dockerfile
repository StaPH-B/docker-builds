FROM mambaorg/micromamba:0.24.0 as app

# Version arguments
# ARG variables only persist during build time
# THIS ARG ONLY USED FOR A LABEL. VERSION SPECIFIED IN PANAROO-ENVIRONMENT.YML
ARG PANAROO_SOFTWARE_VERSION="1.3.4"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:0.24.0"
LABEL dockerfile.version="1"
LABEL software="Panaroo"
LABEL software.version=${PANAROO_SOFTWARE_VERSION}
LABEL description="An updated pipeline for pangenome investigation"
LABEL website="https://github.com/gtonkinhill/panaroo"
LABEL license="https://github.com/gtonkinhill/panaroo/blob/master/LICENSE"
LABEL maintainer1="Kevin Libuit"
LABEL maintainer1.email="kevin.libuit@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    git \
    pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY panaroo-environment.yml /panaroo-environment.yml

RUN micromamba install -y -n base -f /panaroo-environment.yml && \
    micromamba clean -a -y

# Install Panaroo conda environment into base environment using YML file
# clean up conda garbage
RUN micromamba install -y -n base -f /panaroo-environment.yml && \
    micromamba clean -a -y

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/base/bin:${PATH}" \
    LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Run Panaroo
RUN mkdir /data/panaroo_results && \
    panaroo --clean-mode strict -i /data/*.gff -o /data/panaroo_results/
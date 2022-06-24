FROM mambaorg/micromamba:0.22.0 as app

# Version arguments
# ARG variables only persist during build time
ARG PANAROO_SOFTWARE_VERSION="1.2.10"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:0.22.0"
LABEL dockerfile.version="1"
LABEL software="Panaroo"
LABEL software.version=$PANAROO_SOFTWARE_VERSION}
LABEL description="An updated pipeline for pangenome investigation"
LABEL website="https://github.com/gtonkinhill/panaroo"
LABEL license="https://github.com/gtonkinhill/panaroo/blob/master/LICENSE"
LABEL maintainer1="Kevin Libuit"
LABEL maintainer1.email="kevin.libuit@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Create Panaroo conda environment called panaroo-env from bioconda recipe
# clean up conda garbage
RUN micromamba create -n panaroo-env -c conda-forge -c bioconda -c defaults panaroo=${PANAROO_SOFTWARE_VERSION} && \
 micromamba clean -a -y

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/panaroo-env/bin:/opt/conda/envs/env/bin:${PATH}" \
 LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="panaroo-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Run Panaroo
RUN mkdir /data/panaroo_results && panaroo -i /data/*.gff -o /data/panaroo_results/ --clean-mode strict
# Check validity of outputs
RUN cmp /data/gene_data.csv /data/panaroo_results/gene_data.csv
RUN cmp /data/summary_statistics.txt /data/panaroo_results/summary_statistics.txt
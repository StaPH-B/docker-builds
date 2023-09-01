ARG ARTIC_VER=1.2.4

FROM mambaorg/micromamba:1.4.9 as app

ARG ARTIC_VER
ARG MEDAKA_VER=1.9.1

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="artic"
LABEL software.version="${ARTIC_VER}"
LABEL software1="medaka"
LABEL software1.version="${MEDAKA_VER}"
LABEL description="A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore"
LABEL website="https://github.com/artic-network/fieldbioinformatics"
LABEL license="https://github.com/artic-network/fieldbioinformatics/blob/master/LICENSE"
LABEL sop="https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

USER root
WORKDIR /

# Example apt-get command for commonly-missing dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    gcc \
    libcurl3-gnutls \
    libssl-dev \
    python3-dev \
    python3-pip \
    python-is-python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install medaka with pip
RUN pip install --upgrade pip setuptools==57.5.0 && \
    pip install medaka==${MEDAKA_VER} && \
    medaka --version

# install artic and make /data to use as a working directory
# WARNING : On 2023-09-01, medaka's README had this quote : "The bioconda releases lag behind the source code and PyPI releases."
# Also, the bioconda version of artic also seemed to lag behind the github release
RUN wget -q https://github.com/artic-network/fieldbioinformatics/archive/refs/tags/v${ARTIC_VER}.tar.gz && \
    tar -xzf v${ARTIC_VER}.tar.gz && \
    cat fieldbioinformatics-${ARTIC_VER}/environment.yml | grep -v medaka > /environment.yml && \
    micromamba env create -y -f /environment.yml && \
    rm v${ARTIC_VER}.tar.gz && \
    cd fieldbioinformatics-${ARTIC_VER} && \
    python setup.py install && \
    artic -v && \
    mkdir /data
    
ENV ENV_NAME="artic"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# set the environment, add base conda/micromamba bin directory into path
# set locale settings to UTF-8
ENV PATH="/opt/conda/envs/artic/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD artic --help

# set final working directory to /data
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
# new base for testing
FROM app as test
ARG ARTIC_VER

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN artic --help && \
    artic --version

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /fieldbioinformatics-${ARTIC_VER}

# test that came with artic
RUN bash ./test-runner.sh medaka && bash ./test-runner.sh nanopolish

WORKDIR /test

# using on "real" data (sample files were not sequenced with version 5.3.2 primers)
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR224/050/SRR22452250/SRR22452250_1.fastq.gz && \
    artic guppyplex --min-length 400 --max-length 700  --directory . --prefix SRR22452250_1.fastq.gz --output SRR22452250_1_filtered.fastq.gz && \
    mkdir -p directory/nCoV-2019/v5.3.2 && \
    wget https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.primer.bed      --directory-prefix directory/nCoV-2019/v5.3.2 && \
    wget https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.reference.fasta --directory-prefix directory/nCoV-2019/v5.3.2 && \
    wget https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.scheme.bed      --directory-prefix directory/nCoV-2019/v5.3.2 && \
    samtools faidx directory/nCoV-2019/v5.3.2/SARS-CoV-2.reference.fasta && \
    artic minion --normalise 200 --skip-nanopolish --medaka --medaka-model r941_min_high_g360 --threads 4 --read-file input.fastq.gz --scheme-directory directory --scheme-version 5.3.2 nCoV-2019 final && \
    ls final*


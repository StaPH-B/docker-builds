ARG ARTIC_VER=1.2.4

FROM mambaorg/micromamba:1.4.9 as app

ARG ARTIC_VER
ARG MEDAKA_VER=1.12.0

LABEL base.image="mambaorg/micromamba:1.4.9"
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

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    gcc \
    make \
    pkg-config \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    python3-dev \
    python3-pip \
    python-is-python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba create -n artic -y -c conda-forge -c bioconda -c defaults \
    artic=${ARTIC_VER} && \
    micromamba clean -a -y && \
    mkdir /data

ENV PATH="${PATH}:/opt/conda/envs/artic/bin/" \
    LC_ALL=C.UTF-8

RUN artic --help

RUN pip install medaka==${MEDAKA_VER} && \
    pip install pyabpoa && \
    medaka --version

CMD artic --help

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
    artic --version && \
    medaka --version
    
# listing available models
RUN medaka tools list\_models

WORKDIR /

# test that came with artic
RUN wget -q https://github.com/artic-network/fieldbioinformatics/archive/refs/tags/v${ARTIC_VER}.tar.gz && \
    tar -vxf v${ARTIC_VER}.tar.gz && \
    cd /fieldbioinformatics-${ARTIC_VER} && ls && \
    bash ./test-runner.sh medaka && bash ./test-runner.sh nanopolish

WORKDIR /test

# using on "real" data (sample files were not sequenced with version 5.3.2 primers)
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR224/050/SRR22452250/SRR22452250_1.fastq.gz && \
    artic guppyplex --min-length 400 --max-length 700  --directory . --prefix SRR22452250_1.fastq.gz --output SRR22452250_1_filtered.fastq.gz && \ 
    mkdir -p dir/name/V5 && \
    wget -q https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.primer.bed      -O dir/name/V5/name.primer.bed && \
    wget -q https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.reference.fasta -O dir/name/V5/name.reference.fasta  && \
    wget -q https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.scheme.bed      -O dir/name/V5/name.scheme.bed && \
    samtools faidx dir/name/V5/name.reference.fasta && \
    artic minion --normalise 200 --skip-nanopolish --medaka --medaka-model r941_min_high_g360 --threads 4 --read-file SRR22452250_1_filtered.fastq.gz --scheme-directory ./dir --scheme-version 5 name final && \
    ls final*


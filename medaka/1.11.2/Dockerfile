FROM mambaorg/micromamba:1.5.1 as app

ARG MEDAKA_VER=1.11.2
ARG PYABPOA_VER=1.2.4

LABEL base.image="mambaorg/micromamba:1.5.1"
LABEL dockerfile.version="1"
LABEL software="medaka"
LABEL software.version="${MEDAKA_VER}"
LABEL description="For polishing assemblies with nanopore reads"
LABEL website="https://github.com/nanoporetech/medaka"
LABEL license="https://github.com/nanoporetech/medaka/blob/master/LICENSE.md"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

USER root
WORKDIR /

# install dependencies (most are for pyabpoa)
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
    libssl-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# setting PATH
ENV PATH="${PATH}:/opt/conda/bin/" \
    LC_ALL=C.UTF-8

# no version here because the medaka on conda lags behind the latest release
RUN micromamba install --name base -c conda-forge -c bioconda -c defaults medaka && \
    micromamba clean -a -y && \
    mkdir /data

# this _should_ overwrite the medaka installed via micromamba
RUN /opt/conda/bin/pip install medaka==${MEDAKA_VER} && \
    /opt/conda/bin/pip install pyabpoa==${PYABPOA_VER} && \
    medaka --version

CMD medaka --help

WORKDIR /data

# A second FROM insruction creates a new stage
# new base for testing
FROM app as test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN medaka --help && \
    medaka --version
    
# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# using on real data (CRPA isolate)
RUN wget -q https://www.ebi.ac.uk/ena/browser/api/fasta/GCA_021601745.3 -O GCA_021601745.3.fasta && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR234/068/SRR23473168/SRR23473168_1.fastq.gz && \
    medaka_consensus -i SRR23473168_1.fastq.gz -d GCA_021601745.3.fasta -o testing -t 4

# listing available models
RUN medaka tools list\_models
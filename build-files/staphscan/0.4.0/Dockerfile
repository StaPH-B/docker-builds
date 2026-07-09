FROM python:3.13-slim AS app
ARG STAPHSCAN_VER="0.4.0"
ARG MASH_VER=2.3
ARG BLAST_VER=2.17.0

LABEL base.image="python:3.13-slim"
LABEL dockerfile.version="1"
LABEL software="StaphSCAN"
LABEL software.version="${STAPHSCAN_VER}"
LABEL description="A genome-based tool for Surveillance through Comprehensive Analysis and staNdardized reporting of Staphylococcus aureus."
LABEL website="https://github.com/riccabolla/StaphSCAN"
LABEL license="https://github.com/riccabolla/StaphSCAN/blob/main/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"
LABEL maintainer2="Riccardo Bollini"
LABEL maintainer2.email="bollach@virgilio.it / riccardo.bollini@hunimed.eu"

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    wget \
    ca-certificates \
    libgomp1 \
    perl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Mash installation (> 2.0)
RUN wget -q https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
    tar -xvf mash-Linux64-v${MASH_VER}.tar --no-same-owner && \
    mv mash-Linux64-v${MASH_VER}/mash /usr/local/bin/ && \
    rm mash-Linux64-v${MASH_VER}.tar && \
    rm -rf mash-Linux64-v${MASH_VER} && \
    mash --version

# BLAST installation (2.17)
RUN wget -q ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    mv ncbi-blast-${BLAST_VER}+/bin/* /usr/local/bin/ && \
    rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz &&\
    rm -rf ncbi-blast-${BLAST_VER}+ && \
    blastn -help

# StaphSCAN installation
RUN wget -q https://github.com/riccabolla/StaphSCAN/archive/refs/tags/v${STAPHSCAN_VER}.tar.gz && \
    pip install --no-cache-dir v${STAPHSCAN_VER}.tar.gz && \
    rm -rf v${STAPHSCAN_VER}.tar.gz

ENV LC_ALL=C

WORKDIR /data

CMD [ "staphscan", "--help" ]


FROM app AS test

WORKDIR /test

RUN staphscan --help && \
    staphscan --version && \
    staphscan --list-modules

# Test on S. aureus case listed in https://staphscan.readthedocs.io/en/latest/assembly/
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/013/425/GCF_000013425.1_ASM1342v1/GCF_000013425.1_ASM1342v1_genomic.fna.gz && \
    gunzip GCF_000013425.1_ASM1342v1_genomic.fna.gz && \
    staphscan -i GCF_000013425.1_ASM1342v1_genomic.fna -o staphscan_output && \
    head staphscan_output/staphscan_summary.tsv
#14 8.157 Analysis complete.

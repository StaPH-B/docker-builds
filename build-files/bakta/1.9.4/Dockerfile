FROM mambaorg/micromamba:1.5.8 as app

ARG BAKTA_VER="1.9.4"
ARG DIAMOND_VER="2.1.8"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="Bakta"
LABEL software.version="${BAKTA_VER}"
LABEL description="rapid & standardized annotation of bacterial genomes, MAGs & plasmids"
LABEL website="https://github.com/oschwengers/bakta"
LABEL license="https://github.com/oschwengers/bakta/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    procps \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda -c defaults bakta=${BAKTA_VER} diamond=${DIAMOND_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:$PATH" \
    LC_ALL=C

CMD bakta --help

WORKDIR /data

FROM app as test

WORKDIR /test

RUN bakta --help && \
    bakta_db --help && \
    bakta --version

RUN bakta_db list && \
    bakta_db download --type light 

RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/815/GCF_000195815.1_ASM19581v1/GCF_000195815.1_ASM19581v1_genomic.fna.gz && \
    gunzip GCF_000195815.1_ASM19581v1_genomic.fna.gz && \
    bakta --db /test/db-light GCF_000195815.1_ASM19581v1_genomic.fna && \
    head GCF_000195815.1_ASM19581v1_genomic.gbff

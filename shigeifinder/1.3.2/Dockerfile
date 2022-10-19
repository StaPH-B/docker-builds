ARG SHIGEIFINDER_VER="1.3.2"
ARG SAMTOOLS_VER="1.10"
ARG BWA_VER="0.7.17"

FROM ubuntu:focal as app

ARG SHIGEIFINDER_VER
ARG SAMTOOLS_VER
ARG BWA_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="ShigEiFinder"
LABEL software.version=${SHIGEIFINDER_VER}
LABEL description="Cluster informed Shigella and EIEC serotyping tool from Illumina reads and assemblies"
LABEL website="https://github.com/LanLab/ShigEiFinder"
LABEL license="https://github.com/LanLab/ShigEiFinder/blob/main/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="curtis.kapsak@theiagen.com"

# so that apt/tzdata doesn't ask for a timezone during build. Variable will not be in environment after building
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies via apt; cleanup apt garbage
# ncbi-blast+ from apt is v2.9.0 (min ver requirement for ShigEiFinder)
# python version is 
RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    gcc \
    g++ \
    python3 \
    python3-pip \
    python3-setuptools \
    zlib1g-dev \
    wget \
    ca-certificates \
    procps \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    bzip2 \
    gawk \
    gnuplot \
    ncbi-blast+ \
    unzip && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install bwa
RUN mkdir /bwa && \
    cd /bwa && \
    wget https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 && \
    tar -xjf bwa-${BWA_VER}.tar.bz2 && \
    rm bwa-${BWA_VER}.tar.bz2 && \
    cd bwa-${BWA_VER} && \
    make

# install samtools; no need to add to PATH, 'make install' does this for us
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
     tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
     rm samtools-${SAMTOOLS_VER}.tar.bz2 && \
     cd samtools-${SAMTOOLS_VER} && \
     ./configure && \
     make && \
     make install

# install ShigEiFinder; make /data
RUN wget https://github.com/LanLab/ShigEiFinder/archive/refs/tags/v${SHIGEIFINDER_VER}.tar.gz && \
    tar -xvf v${SHIGEIFINDER_VER}.tar.gz && \
    rm v${SHIGEIFINDER_VER}.tar.gz && \
    cd ShigEiFinder-${SHIGEIFINDER_VER} && \
    python3 setup.py install && \
    mkdir /data

# final working directory is /data
WORKDIR /data

# set locale settings for singularity compatibility. Set PATH to include bwa
ENV LC_ALL=C \
    PATH="${PATH}:/bwa/bwa-${BWA_VER}"

# test layer
FROM app as test

ARG SHIGEIFINDER_VER

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

RUN shigeifinder --check && \
    shigeifinder --help

# insert test here for downloading a couple of representative genomes (FASTA) and run them through ShigEiFinder
# Shigella sonnei ref genome: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_013374815.1/
ARG GENBANK_ACCESSION="GCF_013374815.1"
RUN datasets download genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
 mkdir -v ${GENBANK_ACCESSION}-download && \
 unzip ${GENBANK_ACCESSION}.zip -d ${GENBANK_ACCESSION}-download && \
 rm ${GENBANK_ACCESSION}.zip && \
 mv -v ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}*.fna ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna 

# Shigella flexneri 2a str. 301
# https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/198214/
ARG GENBANK_ACCESSION="GCF_000006925.2"
RUN datasets download genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
 mkdir -v ${GENBANK_ACCESSION}-download && \
 unzip ${GENBANK_ACCESSION}.zip -d ${GENBANK_ACCESSION}-download && \
 rm ${GENBANK_ACCESSION}.zip && \
 mv -v ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}*.fna ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna

# insert test here for downloading FASTQs for 1 sample and run through ShigEiFinder (test bwa & samtools)
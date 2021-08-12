FROM ubuntu:18.04

# for easy upgrade later. ARG variables only persist during image build
ARG SAMTOOLSVER=1.12
ARG HTSLIBVER=1.12
ARG IVARVER=1.3.1
ARG BWASVER=0.7.17
ARG VIRALRECON=2.1

LABEL base.image="ubuntu:18.04"
LABEL dockerfile.version="3"
LABEL software="iVar"
LABEL software.version="1.3.1"
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL comments="Contains iVar 1.3.1, htslib/samtools 1.12, bwa 0.7.17-r1188"
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer1="Jill Hagey"
LABEL maintainer1.email="qpk9@cdc.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"
LABEL modified.from="https://github.com/andersen-lab/ivar/blob/master/Dockerfile"
LABEL original.maintainer="Kathik G"
LABEL original.maintainer.email="gkarthik@scripps.edu"

# install dependencies, cleanup apt garbage.
# bedtools version=2.26.0
RUN apt-get update && apt-get install -y \
 build-essential \
 autoconf \
 zlib1g-dev \
 python3 \
 wget \
 libbz2-dev \
 liblzma-dev \
 libncurses-dev \
 git \
 bedtools \
 python3-pip \
 vim \
 gnuplot \
 nano && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Artic ncov2019 (most recent commit was 05/28/2020 as of 06/01/2020)
RUN git clone -n https://github.com/artic-network/artic-ncov2019.git &&\
    cd artic-ncov2019 &&\
    git checkout 7e359dae37d894b40ae7e35c3582f14244ef4d36

# Get gff file for reference genome
RUN mkdir /reference && \
     wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/858/895/GCF_009858895.2_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz -P /reference && \
     gunzip /reference/GCF_009858895.2_ASM985889v3_genomic.gff.gz

RUN cd root/ &&\
  wget https://github.com/samtools/htslib/releases/download/${HTSLIBVER}/htslib-${HTSLIBVER}.tar.bz2 && \
  tar xvf htslib-${HTSLIBVER}.tar.bz2 && \
  cd htslib-${HTSLIBVER}/ && \
  ./configure && \
  make && \
  make install && \
  cd ../ && \
  rm htslib-${HTSLIBVER}.tar.bz2
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH

# SAMtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
  rm samtools-${SAMTOOLSVER}.tar.bz2 && \
  cd samtools-${SAMTOOLSVER} && \
  ./configure && \
  make && \
  make install

# iVar; make /data
RUN cd root/ && \
  wget https://github.com/andersen-lab/ivar/archive/v${IVARVER}.tar.gz && \
  tar -xvf v${IVARVER}.tar.gz && \
  rm -rf v${IVARVER}.tar.gz && \
  cd ivar-${IVARVER} && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install && \
  mkdir /data

# bwa
RUN mkdir bwa &&\
    cd bwa &&\
    wget https://github.com/lh3/bwa/archive/v${BWASVER}.tar.gz &&\
    tar xvf v${BWASVER}.tar.gz &&\
    rm v${BWASVER}.tar.gz &&\
    cd bwa-${BWASVER}/ &&\
    make

#Add bwa to path
ENV PATH="/bwa/bwa-0.7.17:${PATH}"

# indexing the reference sequences
RUN for artic_version in "V1" "V2" "V3" ; do \
    bwa index /artic-ncov2019/primer_schemes/nCoV-2019/$artic_version/nCoV-2019.reference.fasta && \
    samtools faidx /artic-ncov2019/primer_schemes/nCoV-2019/$artic_version/nCoV-2019.reference.fasta ; done

# nf-core/viralrecon
RUN cd /tmp && \
  wget https://github.com/nf-core/viralrecon/archive/refs/tags/${VIRALRECON}.tar.gz && \
  tar -xzvf ${VIRALRECON}.tar.gz && \
  rm -rf ${VIRALRECON}.tar.gz && \
  chmod 755 viralrecon-${VIRALRECON}/bin/ivar_variants_to_vcf.py && \
  cp viralrecon-${VIRALRECON}/bin/ivar_variants_to_vcf.py /usr/local/bin && \
  rm -rf viralrecon-${VIRALRECON}/ && \
  update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# set /data as working directory
WORKDIR /data

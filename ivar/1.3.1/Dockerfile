FROM ubuntu:18.04

# for easy upgrade later. ARG variables only persist during image build
ARG SAMTOOLSVER=1.12
ARG HTSLIBVER=1.12
ARG IVARVER=1.3.1
ARG VIRALRECON=2.1

LABEL base.image="ubuntu:18.04"
LABEL dockerfile.version="3"
LABEL software="iVar"
LABEL software.version="1.3.1"
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL comments="Contains iVar 1.3.1 as well as htslib/samtools 1.12"
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
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
 nano && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

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

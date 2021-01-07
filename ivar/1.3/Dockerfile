FROM ubuntu:18.04

# for easy upgrade later. ARG variables only persist during image build
ARG SAMTOOLSVER=1.11
ARG HTSLIBVER=1.11
ARG IVARVER=1.3

LABEL base.image="ubuntu:18.04"
LABEL container.version="1"
LABEL software="iVar"
LABEL software.version="1.3"
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL comments="Contains iVar 1.3 as well as htslib/samtools 1.11"
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL modified.from="https://github.com/andersen-lab/ivar/blob/master/Dockerfile"
LABEL original.maintainer="Kathik G"
LABEL original.maintainer.email="gkarthik@scripps.edu"

RUN apt-get update
RUN apt-get install -y build-essential autoconf zlib1g-dev python3 wget libbz2-dev liblzma-dev libncurses-dev git bedtools python3-pip vim nano

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
  
# iVar v1.3
RUN cd root/ &&\
  wget https://github.com/andersen-lab/ivar/archive/v${IVARVER}.tar.gz && \
  tar -xvf v${IVARVER}.tar.gz && \
  rm -rf v${IVARVER}.tar.gz && \
  cd ivar-${IVARVER} && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

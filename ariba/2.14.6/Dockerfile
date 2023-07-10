FROM ubuntu:bionic as app

# for easy upgrade later. ARG variables only persist during build time
# ARIBA=2.14.6, pysam=0.15.4; pysam=0.16.0 breaks ariba 2.14.4 (June 2020)
ARG PYSAM_VER="0.15.4"
ARG ARIBA_VER="2.14.6"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL software="ARIBA"
LABEL software.version="2.14.6"
LABEL description="ARIBA: Antimicrobial Resistance Identification By Assembly"
LABEL website="https://github.com/sanger-pathogens/ariba"
LABEL license="https://github.com/sanger-pathogens/ariba/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Harry Hung"
LABEL maintainer2.email="ch31@sanger.ac.uk"

# prevents having to enter commands during apt-get install
ARG DEBIAN_FRONTEND=noninteractive

# dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
 python3-dev \
 python3-pip \
 python3-tk \
 python3-setuptools \
 python3-wheel \
 cython3 \
 zlib1g-dev \
 bowtie2 \
 mummer \
 cd-hit \
 wget \
 curl \
 gawk \
 locales-all \
 build-essential \
 libbz2-dev \
 libjpeg-dev  \
 liblzma-dev  \
 autoconf \
 automake \
 perl \
 libcurl4-gnutls-dev \
 libssl-dev && \
 rm -rf /var/lib/apt/lists/*

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en 

# SPAdes 3.15.5
# optional installation to enable the usage of SPAdes assembler
RUN wget https://github.com/ablab/spades/releases/download/v3.15.5/SPAdes-3.15.5-Linux.tar.gz && \
  tar -xzf SPAdes-3.15.5-Linux.tar.gz && \
  rm -r SPAdes-3.15.5-Linux.tar.gz && \
  mkdir /data

# needed to avoid a matplotlib error
# https://github.com/sanger-pathogens/ariba/blob/b1b524c9d9588cba9d998c9121bd74c63856526/Dockerfile#L49
ENV MPLBACKEND="agg"

RUN pip3 install pysam==${PYSAM_VER} ariba==${ARIBA_VER}

# set $PATH and locale settings for singularity compatibility
ENV PATH="$PATH:/SPAdes-3.15.5-Linux/bin" \
 LC_ALL=C

WORKDIR /data

# new base for testing
FROM app as test

# print out ARIBA version and 
RUN ariba version

# run built-in test and confirm files are successfully created
RUN ariba test out
RUN ls out/OUT/assemblies.fa.gz && \
    ls out/OUT/assembled_genes.fa.gz && \
    ls out/OUT/assembled_seqs.fa.gz && \
    ls out/OUT/log.clusters.gz && \
    ls out/OUT/report.tsv && \
    ls out/OUT/version_info.txt
FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL container.version="1.0.0"
LABEL software="Snippy"
LABEL software.version="4.5.1"
LABEL description="Rapid haploid variant calling and core genome alignment"
LABEL website="https://github.com/tseemann/snippy"
LABEL license="https://github.com/tseemann/snippy/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
# BioPerl version in ubuntu:bioinic 1.7.2 (as of March 2020)
RUN apt-get update && apt-get -y --no-install-recommends install \
 wget \ 
 gcc \ 
 libstdc++6 \ 
 libbz2-1.0 \
 cpanminus \
 autoconf \
 parallel \
 unzip \
 snp-sites \
 bzip2 \
 gzip \
 wget \
 perl \
 less \
 libdatetime-perl \
 libxml-simple-perl \
 libdigest-md5-perl \
 default-jre \
 bioperl \
 hmmer \
 zlib1g-dev \
 python \
 python3 \
 liblzma-dev \
 libbz2-dev \
 xz-utils \ 
 curl \
 g++ \
 libcurl4-openssl-dev \
 libssl-dev \
 make \
 git && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# bwa 0.7.17-r1188 - bundled

# install minimap2 and create /data
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
  tar -xvf minimap2-2.17_x64-linux.tar.bz2 && \
  rm minimap2-2.17_x64-linux.tar.bz2 && \
  mkdir /data

# samtools 1.10 - bundled

# install bedtools 2.29.0 since the debian package for ubuntu:bionic is 2.26.0
# dependencies required for bedtools: zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
  tar -zxf bedtools-2.29.0.tar.gz && \
  rm bedtools-2.29.0.tar.gz && \
  cd bedtools2 && \
  make

# bcftools 1.10.2 - bundled

# freebayes 1.3.1-dirty - bundled
# python3 required for freebayes

# vcflib - bundled

# vt 0.5772-60f436c3 - bundled
# libcurl4-openssl-dev required for vt

# SnpEff 4.3t - bundled (build 2017-11-24 10:18)

# Seqtk 1.3-r106 - bundled

# Samclip 0.2 - bundled

# snp-sites 2.3.3 - via apt-get 

# any2fasta 0.4.2 - bundled

# install wgsim for testing snippy (latest version from master branch)
RUN git clone https://github.com/lh3/wgsim.git && \
 cd /wgsim && \
 gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm

# Snippy

####TEMPORARILY COMMENTED UNTIL TORSTEN MAKES A NEW RELEASE
#RUN wget https://github.com/tseemann/snippy/archive/v4.5.1.tar.gz && \
#  tar -zxf v4.5.1.tar.gz && \
#  rm v4.5.1.tar.gz

# TEMP ROUTE TO GRAB LATEST COMMITS/BINARIES
RUN git clone https://github.com/tseemann/snippy.git

# set PATH and perl local settings
ENV PATH="${PATH}:/bedtools2/bin:\
/minimap2-2.17_x64-linux:\
/wgsim:\
/snippy/bin:\
/snippy/binaries/linux:\
/snippy/binaries/noarch" \
    LC_ALL=C

WORKDIR /data

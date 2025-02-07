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

# install bwa - bundled

# install minimap2
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
  tar -xvf minimap2-2.17_x64-linux.tar.bz2 && \
  rm minimap2-2.17_x64-linux.tar.bz2

# samtools 1.10 - bundled

# install bedtools 2.29.0 since the debian package for ubuntu:bionic is 2.26.0
# dependencies required for bedtools: zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
  tar -zxf bedtools-2.29.0.tar.gz && \
  rm bedtools-2.29.0.tar.gz && \
  cd bedtools2 && \
  make

# bcftools - bundled

# freebayes - bundled
# python3 required for freebayes

# vcflib - bundled

# install vt - libcurl4-openssl-dev required for vt
# vt is bundled w snippy, but unsure if the bundled binary works properly or not...
RUN wget https://github.com/atks/vt/archive/0.57721.tar.gz && \
  tar -xzf 0.57721.tar.gz && \
  rm 0.57721.tar.gz && \
  cd vt-0.57721 && \
  make && \
  make test

# install SnpEff v4.3t (build 2017-11-24 10:18) - unzip needed
RUN wget https://sourceforge.net/projects/snpeff/files/snpEff_v4_3t_core.zip && \
  unzip snpEff_v4_3t_core.zip

# install Seqtk 1.3
# also bundled with snippy, but unsure if bundled binary works properly or not
RUN mkdir seqtk &&\ 
  cd seqtk &&\
  wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz && \
  tar -zxf v1.3.tar.gz && \
  rm v1.3.tar.gz && \
  cd seqtk-1.3/ && \
  make && \
  make install

# Samclip (latest version from master branch)
RUN mkdir samclip && \
  cd samclip && \
  wget https://raw.githubusercontent.com/tseemann/samclip/master/samclip && \
  chmod +x samclip

# snp-sites v2.3.3 - via apt-get 

# install wgsim for testing snippy (latest version from master branch)
RUN git clone https://github.com/lh3/wgsim.git && \
 cd /wgsim && \
 gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm

# Snippy
RUN wget https://github.com/tseemann/snippy/archive/v4.5.1.tar.gz && \
  tar -zxf v4.5.1.tar.gz && \
  rm v4.5.1.tar.gz

# had to prioritize wgsim, seqtk, and vt manual installs instead of bundled binaries
# due to issues with shared objects and links and a bunch of things I don't understand fully
ENV PATH="${PATH}:/bedtools2/bin:\
/minimap2-2.17_x64-linux:\
/vt-0.57721/:\
/snpEff/scripts:\
/samclip:\
/wgsim:\
/snippy-4.5.1/bin:\
/snippy-4.5.1/binaries/linux" \
    LC_ALL=C

WORKDIR /data

FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL container.version="1.0.0"
LABEL software="Snippy"
LABEL software.version="4.6.0"
LABEL description="Rapid haploid variant calling and core genome alignment"
LABEL website="https://github.com/tseemann/snippy"
LABEL license="https://github.com/tseemann/snippy/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

### install dependencies ###
# BioPerl version in ubuntu:bioinic 1.7.2 (as of March 2020)
# snp-sites now bundled w/ snippy
# parallel now bundled w/ snippy
# cpanminus removed (no need to install additional perl modules)
# g++ and gcc removed (no compiling needed)
RUN apt-get update && apt-get -y --no-install-recommends install \
 wget \ 
 libstdc++6 \ 
 libbz2-1.0 \
 autoconf \
 unzip \
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
 libcurl4-openssl-dev \
 libssl-dev \
 make && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# bwa 0.7.17-r1188 - bundled

# minimap2 2.17-r941 - bundled

# samtools 1.10 - bundled

# bedtools 2.29.2 - bundled 
# dependencies required for bedtools (used to install via apt): 
# zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++ 
# these are probably only needed when installing from source and compiling - leaving just in case

# bcftools 1.10.2 - bundled

# freebayes 1.3.1-dirty - bundled
# python3 required for freebayes

# vcflib - bundled

# vt 0.5772-60f436c3 - bundled
# libcurl4-openssl-dev required for vt

# SnpEff 4.3t - bundled (build 2017-11-24 10:18)

# Seqtk 1.3-r106 - bundled

# Samclip 0.4 - bundled

# snp-sites 2.3.3 - via apt-get 

# any2fasta 0.4.2 - bundled

# wgsim 0.3.1-r13 - bundled for testing snippy

# Snippy 4.6.0 and make /data
RUN wget https://github.com/tseemann/snippy/archive/v4.6.0.tar.gz && \
  tar -zxf v4.6.0.tar.gz && \
  rm v4.6.0.tar.gz && \
  mkdir /data

# set PATH and perl local settings
ENV PATH="${PATH}:\
/snippy-4.6.0/bin:\
/snippy-4.6.0/binaries/linux:\
/snippy-4.6.0/binaries/noarch" \
    LC_ALL=C

WORKDIR /data

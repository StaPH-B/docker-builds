FROM ubuntu:xenial

ARG bcftoolsVer="1.10.2"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="bcftools"
LABEL software.version="1.10.2"
LABEL description="Variant calling and manipulating files in the Variant Call Format (VCF) and its binary counterpart BCF"
LABEL website="https://github.com/samtools/bcftools"
LABEL license="https://github.com/samtools/bcftools/blob/develop/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies  
RUN apt-get update && apt-get install -y \
 wget \
 perl \
 bzip2 \
 autoconf \
 automake \
 make \
 gcc \
 zlib1g-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 libssl-dev \
 libperl-dev \
 libgsl0-dev && \
 rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get autoclean

# get bcftools and make /data
RUN mkdir bcftools && \
 wget https://github.com/samtools/bcftools/releases/download/${bcftoolsVer}/bcftools-${bcftoolsVer}.tar.bz2 && \
 tar -vxjf bcftools-${bcftoolsVer}.tar.bz2 -C bcftools --strip-components 1 && \
 rm bcftools-${bcftoolsVer}.tar.bz2 && \
 cd bcftools && \
 make && \
 make install && \
 mkdir /data

# set $PATH (honestly unnecessary here, lol) and locale settings for singularity compatibility
ENV PATH="$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

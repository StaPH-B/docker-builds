FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during build time
ARG bcftoolsVer="1.13"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="bcftools"
LABEL software.version="1.13"
LABEL description="Variant calling and manipulating files in the Variant Call Format (VCF) and its binary counterpart BCF"
LABEL website="https://github.com/samtools/bcftools"
LABEL license="https://github.com/samtools/bcftools/blob/develop/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install dependencies, cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
 wget \
 ca-certificates \
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
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# get bcftools and make /data
RUN wget https://github.com/samtools/bcftools/releases/download/${bcftoolsVer}/bcftools-${bcftoolsVer}.tar.bz2 && \
 tar -vxjf bcftools-${bcftoolsVer}.tar.bz2 && \
 rm bcftools-${bcftoolsVer}.tar.bz2 && \
 cd bcftools-${bcftoolsVer} && \
 make && \
 make install && \
 mkdir /data

# set $PATH (honestly unnecessary here, lol) and locale settings for singularity compatibility
ENV PATH="$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

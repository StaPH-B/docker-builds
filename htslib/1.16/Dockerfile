# for easy upgrade later. ARG variables only persist during build time
ARG HTSLIBVER="1.16"

FROM ubuntu:focal as app

ARG HTSLIBVER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="htslib"
LABEL software.version="${HTSLIBVER}"
LABEL description="A C library for reading/writing high-throughput sequencing data"
LABEL website="https://github.com/samtools/htslib"
LABEL license="https://github.com/samtools/htslib/blob/develop/LICENSE"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install dependencies, cleanup apt garbage
# It's helpful when they're all listed on https://github.com/samtools/htslib/blob/develop/INSTALL
RUN apt-get update && apt-get install --no-install-recommends -y \
 wget \
 ca-certificates \
 make \
 bzip2 \
 autoconf \
 automake \
 make \
 gcc \
 perl \
 zlib1g-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 libssl-dev && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# get htslib and make /data
RUN wget https://github.com/samtools/htslib/releases/download/${HTSLIBVER}/htslib-${HTSLIBVER}.tar.bz2 && \
 tar -vxjf htslib-${HTSLIBVER}.tar.bz2 && \
 rm htslib-${HTSLIBVER}.tar.bz2 && \
 cd htslib-${HTSLIBVER} && \
 make && \
 make install && \
 mkdir /data

# set $PATH (honestly unnecessary here, lol) and locale settings for singularity compatibility
ENV PATH="$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

# testing
FROM app as test

ARG HTSLIBVER

WORKDIR /htslib-${HTSLIBVER}/test

RUN perl /htslib-${HTSLIBVER}/test/test.pl

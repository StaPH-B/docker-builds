# for easy upgrade later. ARG variables only persist during build time
ARG HTSLIB_VER="1.21"

FROM ubuntu:jammy as builder

ARG HTSLIB_VER

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
    libssl-dev \
    libdeflate-dev \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# get htslib, compile, install, run test suite
RUN wget -q https://github.com/samtools/htslib/releases/download/${HTSLIB_VER}/htslib-${HTSLIB_VER}.tar.bz2 && \
    tar -vxjf htslib-${HTSLIB_VER}.tar.bz2 && \
    rm -v htslib-${HTSLIB_VER}.tar.bz2 && \
    cd htslib-${HTSLIB_VER} && \
    ./configure && \
    make && \
    make install && \
    make test

### start of app stage ###
FROM ubuntu:jammy as app 

ARG HTSLIB_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="htslib"
LABEL software.version="${HTSLIB_VER}"
LABEL description="A C library for reading/writing high-throughput sequencing data"
LABEL website="https://github.com/samtools/htslib"
LABEL license="https://github.com/samtools/htslib/blob/develop/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install runtime dependencies & cleanup apt garbage
# installed as recommend here: https://github.com/samtools/htslib/blob/develop/INSTALL#L31
RUN apt-get update && apt-get install --no-install-recommends -y \
    bzip2 \
    zlib1g \
    libbz2-1.0 \
    liblzma5 \
    libcurl3-gnutls \
    libdeflate0 \
    ca-certificates \ 
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# copy in htslib executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/
COPY --from=builder /usr/local/lib/ /usr/local/lib/
COPY --from=builder /usr/local/include/ /usr/local/include/

# set locale settings for singularity compatibility
ENV LC_ALL=C

# set working directory
WORKDIR /data

# default command is to show help options
CMD ["htsfile", "--help"]

### start of test stage ###
FROM app as test

# check that these three executables are available
RUN bgzip --help && tabix --help && htsfile --help

RUN apt-get update && apt-get install --no-install-recommends -y wget

# use on actual files
RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    gunzip SRR13957123_1.fastq.gz && \
    bgzip SRR13957123_1.fastq

# FYI Test suite "make test" now performed in the builder stage since app and
# test stages do not include htslib source code.
# This is to avoid having to re-download source code simply to run test suite
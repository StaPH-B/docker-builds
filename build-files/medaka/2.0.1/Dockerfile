ARG MEDAKA_VER="2.0.1"
ARG PYABPOA_VER="1.5.3"
ARG SAMTOOLS_VER="1.21"
ARG BCFTOOLS_VER=${SAMTOOLS_VER}
ARG HTSLIB_VER=${SAMTOOLS_VER}
ARG MINIMAP2_VER="2.28"

FROM ubuntu:jammy AS builder

ARG SAMTOOLS_VER
ARG BCFTOOLS_VER
ARG HTSLIB_VER
ARG MINIMAP2_VER

# install dependencies required for compiling samtools
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    gcc \
    wget \
    make \
    perl \
    bzip2 \
    gnuplot \
    ca-certificates \
    curl \
    perl \
    bzip2 \
    autoconf \
    automake \
    make \
    gcc \
    libdeflate-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libperl-dev \
    libgsl0-dev \
    libdeflate-dev \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# download, compile, and install bcftools
RUN wget -q https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VER}/bcftools-${BCFTOOLS_VER}.tar.bz2 && \
    tar -xjf bcftools-${BCFTOOLS_VER}.tar.bz2 && \
    rm -v bcftools-${BCFTOOLS_VER}.tar.bz2 && \
    cd bcftools-${BCFTOOLS_VER} && \
    ./configure --enable-libgsl --enable-perl-filters &&\
    make && \
    make install

# download, compile, and install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install 

RUN wget -q https://github.com/samtools/htslib/releases/download/${HTSLIB_VER}/htslib-${HTSLIB_VER}.tar.bz2 && \
    tar -xjf htslib-${HTSLIB_VER}.tar.bz2 && \
    rm -v htslib-${HTSLIB_VER}.tar.bz2 && \
    cd htslib-${HTSLIB_VER} && \
    ./configure && \
    make && \
    make install 

RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner && \
    mv -v minimap2-${MINIMAP2_VER}_x64-linux/minimap2 /usr/local/bin

### start of app stage ###
FROM ubuntu:jammy AS app

ARG MEDAKA_VER
ARG PYABPOA_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version=1
LABEL container.version="1"
LABEL software="Medaka"
LABEL software.version="${MEDAKA_VER}"
LABEL description="Consensus sequence correction provided by ONT Research"
LABEL website="https://github.com/nanoporetech/medaka"
LABEL license="https://github.com/nanoporetech/medaka/blob/master/LICENSE.md"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

# install dependencies required for running samtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    zlib1g \
    libncurses5 \
    bzip2 \
    libdeflate-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    python3 \
    python3-pip \
    python-is-python3 \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libgsl-dev \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# copy in samtools, htslib, and minimap2 executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/

# install medaka via pip
RUN pip install medaka-cpu==${MEDAKA_VER} --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir && \
    pip install pyabpoa==${PYABPOA_VER} --no-cache-dir

ENV LC_ALL=C

# final working directory is /data
WORKDIR /data

# default command is to pull up help options
CMD [ "medaka", "--help" ]

### start of test stage ###
FROM app AS test

RUN apt-get update && apt-get install --no-install-recommends -y wget

# making sure dependencies are in path
RUN samtools --help && minimap2 --help && tabix --help && bgzip --help

RUN medaka --help && \
    medaka --version

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# using on real data (CRPA isolate)
RUN wget -q https://www.ebi.ac.uk/ena/browser/api/fasta/GCA_021601745.3 -O GCA_021601745.3.fasta && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR234/068/SRR23473168/SRR23473168_1.fastq.gz && \
    medaka_consensus -i SRR23473168_1.fastq.gz -d GCA_021601745.3.fasta -o testing -t 4

# listing available models
RUN medaka tools list\_models

# Use ubuntu as base image
FROM ubuntu:xenial as app

# metadata
LABEL base.image="ubuntu:xenial"
LABEL software="Canu"
LABEL software.version="2.2"
LABEL dockerfile.version="1"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/marbl/canu"
LABEL license="https://github.com/marbl/canu/blob/master/README.license.GPL"
LABEL maintainer="Thomas A. Christensen II"
LABEL maintainer.email="25492070+MillironX@users.noreply.github.com"

# version to build with
ARG CANU_VERSION=2.2

# install python
RUN apt-get update && apt-get install -y \
   perl \
   default-jre \
   gnuplot \
   libgcc-5-dev \
   libgomp1 \
   maven \
   git \
   wget \
   python3 \
   build-essential \
   cmake \
   zlib1g-dev && \
   apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
   mkdir /data

# install canu
RUN wget https://github.com/marbl/canu/releases/download/v${CANU_VERSION}/canu-${CANU_VERSION}.Linux-amd64.tar.xz && \
  tar -xvf canu-${CANU_VERSION}.Linux-amd64.tar.xz && \
  rm canu-${CANU_VERSION}.Linux-amd64.tar.xz

ENV PATH="/canu-${CANU_VERSION}/bin:${PATH}"

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

# ======== Adding a test layer ========

FROM app as test

# creating test working DIR.  
WORKDIR /test_canu

# download test input file into /test_canu/ directory
RUN wget https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz

# testing analysis RUN, canu need to know approx genome size (for coverage calculation) and sequencing platform
RUN canu \
   -p portiera -d portiera-nanopore \
   genomeSize=0.3m \
   -nanopore ERR3772599.fastq.gz \
   maxMemory=7 maxThreads=2 \
   redMemory=7 redThreads=2 \
   corMemory=7 corThreads=2 \
   oeaMemory=7 oeaThreads=2 \
   batMemory=7 batThreads=2 \
   cnsMemory=7 cnsThreads=2 


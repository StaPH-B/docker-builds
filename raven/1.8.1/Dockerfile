ARG RAVEN_VERSION=1.8.1

# base image
FROM ubuntu:focal as app

ARG RAVEN_VERSION

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="raven"
LABEL software.version="${RAVEN_VERSION}"
LABEL description="Raven is a de novo genome assembler for long uncorrected reads."
LABEL website="https://github.com/lbcb-sci/raven"
LABEL license="https://github.com/lbcb-sci/raven/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# otherwise tzdata won't install
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies via apt-get or yum if using a centos or fedora base 
RUN apt-get update && apt-get install -y \
  wget \
  git \
  clang \
  gcc \
  zlib1g-dev \
  build-essential \
  cmake \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/*

# install raven
RUN wget https://github.com/lbcb-sci/raven/archive/refs/tags/${RAVEN_VERSION}.tar.gz && \
  tar -xvf ${RAVEN_VERSION}.tar.gz && \
  rm ${RAVEN_VERSION}.tar.gz && \
  cd raven-${RAVEN_VERSION} && \
  cmake -S ./ -B ./build -DRAVEN_BUILD_EXE=1 -DCMAKE_BUILD_TYPE=Release && \
  cmake --install ./build

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/raven-${RAVEN_VERSION}/:$PATH" \
 LC_ALL=C

RUN raven --help

# set working directory
WORKDIR /data

FROM app as test

WORKDIR /test

ARG RAVEN_VERSION

RUN echo $PATH

RUN cp /raven-${RAVEN_VERSION}/RavenTest/data/ERA476754.fastq.gz . && \
  cp /raven-${RAVEN_VERSION}/RavenTest/data/NC_001416.fasta.gz . && \
  raven --graphical-fragment-assembly test1.gfa ERA476754.fastq.gz > test1.fasta && \
  raven --graphical-fragment-assembly test2.gfa NC_001416.fasta.gz > test2.fasta && \
  wc -l test*

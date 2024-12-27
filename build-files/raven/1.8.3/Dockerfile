ARG RAVEN_VERSION=1.8.3

# base image
FROM ubuntu:jammy as app

ARG RAVEN_VERSION

# metadata
LABEL base.image="ubuntu:jammy"
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
    clang \
    git \
    gcc \
    zlib1g-dev \
    build-essential \
    cmake \
    libboost-all-dev \
    doxygen \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/*

# install raven
RUN wget https://github.com/lbcb-sci/raven/archive/refs/tags/${RAVEN_VERSION}.tar.gz && \
    tar -xvf ${RAVEN_VERSION}.tar.gz && \
    rm ${RAVEN_VERSION}.tar.gz 
  
WORKDIR raven-${RAVEN_VERSION}


RUN cmake -S ./ -B ./build -DRAVEN_BUILD_EXE=1 -DCMAKE_BUILD_TYPE=Release -Wno-dev && \
    cmake --build build && \
    cmake --install ./build

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/raven-${RAVEN_VERSION}/:$PATH" \
    LC_ALL=C

# set working directory
WORKDIR /data

CMD raven --help

FROM app as test

WORKDIR /test

ARG RAVEN_VERSION

RUN raven --graphical-fragment-assembly ERA476754.gfa /raven-${RAVEN_VERSION}/RavenTest/data/ERA476754.fastq.gz > ERA476754.fasta && \
    test -f ERA476754.gfa && test -f ERA476754.fasta

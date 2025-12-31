ARG ANY2FASTA_VERSION=0.8.1

# base image
FROM ubuntu:noble AS app

# version to build with
ARG ANY2FASTA_VERSION

# metadata
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="any2fasta"
LABEL software.version="${ANY2FASTA_VERSION}"
LABEL description="Turns files into fastas."
LABEL website="https://github.com/tseemann/any2fasta"
LABEL license="https://github.com/tseemann/any2fasta/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    perl \
    zip \
    unzip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install any2fasta
RUN wget https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VERSION}.tar.gz && \
    tar -xvf v${ANY2FASTA_VERSION}.tar.gz && \
    rm v${ANY2FASTA_VERSION}.tar.gz && \
    cd any2fasta-${ANY2FASTA_VERSION} && \
    chmod +x any2fasta

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/any2fasta-${ANY2FASTA_VERSION}:$PATH" \
    LC_ALL=C

# set working directory
WORKDIR /data

#######################
##### NEXT STAGE! #####
#######################

# running a 'test' in the 'test' stage
FROM app AS test

ARG ANY2FASTA_VERSION

# check version and print help options
RUN any2fasta -v && \
    any2fasta -h && \
    any2fasta -h | grep github

WORKDIR /test

# updated to documenation
# https://github.com/tseemann/any2fasta/tree/master?tab=readme-ov-file#extensive-test
RUN apt-get update && apt-get install -y --no-install-recommends bats

RUN bats $(dirname $(which any2fasta))/test/test.sh

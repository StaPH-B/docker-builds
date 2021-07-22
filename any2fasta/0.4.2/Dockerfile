# base image
FROM ubuntu:focal

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="any2fasta"
LABEL software.version="0.4.2"
LABEL description="Turns files into fastas."
LABEL website="https://github.com/tseemann/any2fasta"
LABEL license="https://github.com/tseemann/any2fasta/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# version to build with
ARG ANY2FASTA_VERSION=0.4.2

# install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y wget perl && \
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

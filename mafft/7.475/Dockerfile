# base image
FROM ubuntu:bionic

# For easy upgrade in the future. ARG variables only persist during build time.
ARG MAFFT_VER="7.475"

# metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="MAFFT"
LABEL software.version="7.475"
LABEL description="Multiple alignment program for amino acid or nucleotide sequences"
LABEL website="https://mafft.cbrc.jp/alignment/software/"
LABEL license="https://mafft.cbrc.jp/alignment/software/license.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install wget, remove apt garbage
RUN apt-get update && apt-get install -y wget && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install mafft binary and make /data
RUN wget https://mafft.cbrc.jp/alignment/software/mafft_${MAFFT_VER}-1_amd64.deb && \
    dpkg -i mafft_${MAFFT_VER}-1_amd64.deb && \
    rm mafft_${MAFFT_VER}-1_amd64.deb && \
    mkdir /data

WORKDIR /data

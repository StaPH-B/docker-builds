# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="7.450"
LABEL software="MAFFT"
LABEL software.version="7.450"
LABEL description="Multiple alignment program for amino acid or nucleotide sequences"
LABEL website="https://mafft.cbrc.jp/alignment/software/"
LABEL license="https://mafft.cbrc.jp/alignment/software/license.txt"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@dgs.virginia.gov"

RUN apt-get update && apt-get install -y wget

# install mafft binary and make /data
RUN wget https://mafft.cbrc.jp/alignment/software/mafft_7.450-1_amd64.deb && \
    dpkg -i mafft_7.450-1_amd64.deb && \
    mkdir /data

WORKDIR /data

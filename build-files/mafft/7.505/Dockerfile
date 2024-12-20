# base image
FROM ubuntu:bionic as app

# For easy upgrade in the future. ARG variables only persist during build time.
ARG MAFFT_VER="7.505"

# metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="MAFFT"
LABEL software.version=${MAFFT_VER}
LABEL description="Multiple alignment program for amino acid or nucleotide sequences"
LABEL website="https://mafft.cbrc.jp/alignment/software/"
LABEL license="https://mafft.cbrc.jp/alignment/software/license.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install wget, remove apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install mafft binary and make /data
RUN wget https://mafft.cbrc.jp/alignment/software/mafft_${MAFFT_VER}-1_amd64.deb && \
    dpkg -i mafft_${MAFFT_VER}-1_amd64.deb && \
    rm mafft_${MAFFT_VER}-1_amd64.deb && \
    mkdir /data

WORKDIR /data

FROM staphb/ncbi-datasets:14.3.0 as datasets

WORKDIR /test

RUN datasets download virus genome accession OQ344199.1 OQ344200.1 OQ344201.1 --filename sarscov2.zip && unzip sarscov2.zip

FROM app as test

WORKDIR /test

COPY --from=datasets /test/ncbi_dataset/data/genomic.fna /test/genomic.fna

# this works, but it writes to stderr
# RUN maff --help && mafft --version 

RUN mafft --auto genomic.fna > aligned.fna && wc -l *fna

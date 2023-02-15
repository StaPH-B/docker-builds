FROM ubuntu:xenial as app

LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="BWA"
LABEL software.version="0.7.17"
LABEL description="Burrow-Wheeler Aligner for short-read alignment"
LABEL website="https://github.com/lh3/bwa"
LABEL license="https://github.com/lh3/bwa/blob/master/COPYING"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL dockerfile.version="2"

RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 make \
 gcc \
 zlib1g-dev \
 bzip2 \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN mkdir bwa &&\
  mkdir /data &&\
  cd bwa &&\
  wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2 &&\
  tar -xjf bwa-0.7.17.tar.bz2 &&\
  rm bwa-0.7.17.tar.bz2 &&\
  cd bwa-0.7.17 &&\
  make

ENV PATH="${PATH}:/bwa/bwa-0.7.17"
WORKDIR /data

FROM app as test

RUN wget "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=5&rettype=fasta" \
    -o "sequence.fasta" &&\
    bwa index "sequence.fasta"

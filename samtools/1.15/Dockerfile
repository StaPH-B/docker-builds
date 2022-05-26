FROM ubuntu:focal as app

ARG SAMTOOLSVER=1.15

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Samtools"
LABEL software.version="${SAMTOOLSVER}"
LABEL description="Tools (written in C using htslib) for manipulating next-generation sequencing data"
LABEL website="https://github.com/samtools/samtools"
LABEL license="https://github.com/samtools/samtools/blob/develop/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

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
 gawk \
 python3 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
 tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
 rm samtools-${SAMTOOLSVER}.tar.bz2 && \
 cd samtools-${SAMTOOLSVER} && \
 ./configure && \
 make && \
 make install && \
 mkdir /data

ENV LC_ALL=C

WORKDIR /data

FROM app as test

RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
  wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
  samtools stats SRR13957123.primertrim.sorted.bam && \
  samtools faidx SRR13957123.consensus.fa

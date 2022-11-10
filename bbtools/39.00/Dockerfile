FROM ubuntu:focal as app

ARG SAMTOOLSVER=1.16.1
ARG SAMBAMBAVER=0.8.2
ARG BBTOOLSVER=39.00

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="BBTools"
LABEL software.version=${BBTOOLSVER}
LABEL description="A set of tools labeled as \"Bestus Bioinformaticus\""
LABEL website="https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/"
LABEL license="https://jgi.doe.gov/disclaimer/"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Padraic Fanning"
LABEL maintainer2.email="faninnpm AT miamioh DOT edu"

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    autoconf \
    automake \
    build-essential \
    bzip2 \
    lbzip2 \
    libbz2-dev \
    libcurl4-openssl-dev \
    liblzma-dev \
    libncurses5-dev \
    libssl-dev \
    openjdk-8-jre-headless \
    pbzip2 \
    pigz \
    wget \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean

# download and install samtools
WORKDIR /opt
RUN wget --progress=dot:giga https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
    rm samtools-${SAMTOOLSVER}.tar.bz2
WORKDIR /opt/samtools-${SAMTOOLSVER}
RUN ./configure && \
    make && \
    make install
WORKDIR /opt

# download and install sambamba
RUN wget --progress=dot:giga https://github.com/biod/sambamba/releases/download/v${SAMBAMBAVER}/sambamba-${SAMBAMBAVER}-linux-amd64-static.gz && \
    gzip -d sambamba-${SAMBAMBAVER}-linux-amd64-static.gz && \
    mv /opt/sambamba-${SAMBAMBAVER}-linux-amd64-static /opt/sambamba && \
    chmod +x /opt/sambamba && \
    ln -s /opt/sambamba /usr/local/bin

# download and install bbtools
RUN wget --progress=dot:giga https://sourceforge.net/projects/bbmap/files/BBMap_${BBTOOLSVER}.tar.gz && \
    tar -xzf BBMap_${BBTOOLSVER}.tar.gz && \
    rm BBMap_${BBTOOLSVER}.tar.gz && \
    ln -s /opt/bbmap/*.sh /usr/local/bin/

WORKDIR /data

# testing
FROM app as test

# get test data and test one thing that uses samtools/sambamba
RUN wget --progress=dot:giga https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
    streamsam.sh in='SRR13957123.primertrim.sorted.bam' out='test_SRR13957123.primertrim.sorted.fastq.gz' && \
    test -f test_SRR13957123.primertrim.sorted.fastq.gz

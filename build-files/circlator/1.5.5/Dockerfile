FROM ubuntu:jammy as app

ARG CIRCLATOR_VER="1.5.5"
ARG SAMTOOLS_VER="1.16.1"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="circlator"
LABEL software.version=$CIRCLATOR_VER
LABEL description="A tool to circularize genome assemblies"
LABEL website="https://github.com/sanger-pathogens/circlator"
LABEL license="https://github.com/sanger-pathogens/circlator/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# mummer version 3.23+dfsg-7
# bwa version 0.7.17
# prodigal version 2.6.3
# canu version 2.0
# spades version 3.13.1
# spades version gives the following error: 
# WARNING: SPAdes version 3.13.1 is being used. It will work, but better results are usually obtained from Circlator using SPAdes version 3.7.1. Although 3.7.1 is not the latest version, we recommend it for Circlator.
RUN apt-get update && apt-get install -y --no-install-recommends \
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
    gawk \
    ca-certificates \
    procps \
    bwa \
    prodigal \
    mummer \
    canu \
    spades \
    python3 \
    python3-pip \
    xz-utils && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    rm samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install && \
    mkdir  /data

# install circlator
RUN pip3 install circlator==${CIRCLATOR_VER}

ENV PATH="/circlator-v${CIRCLATOR_VER}/bin:$PATH" \
    LC_ALL=C

WORKDIR /data

FROM app as test

RUN circlator --help && circlator version && circlator progcheck

RUN circlator test testdir && ls testdir

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/8b9559a4293f64b1d99c2376fe0e1b94f854e3db/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
    circlator fixstart SRR13957123.consensus.fa SRR13957123_fixstart && \
    ls && cat SRR13957123_fixstart.log



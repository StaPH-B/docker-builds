# base image
FROM ubuntu:bionic as app

# for easy upgrade later. ARG variables only persist during image build time
ARG GAMMA_VER="2.2"

# metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="GAMMA"
LABEL software.version="v2.2"
LABEL description="Gene Allele Mutation Microbial Assessment"
LABEL website="https://github.com/rastanton/GAMMA/"
LABEL license="Apache 2.0"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="jvhagey@gmail.com"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
    bc \
    rsync \
    unzip \
    tar \
    python3.8 \
    python3-pip \
    gzip \
    wget \
    git \
    curl \
    make \
    g++ \
    ncbi-blast+ \
    hmmer && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

#install biopython
RUN pip3 install biopython cgecore tabulate unidecode

# install blat
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat && \
    chmod +x blat && \
    mv blat /bin/blat && \
    mkdir /data

#install GAMMA
RUN wget https://github.com/rastanton/GAMMA/archive/refs/tags/v${GAMMA_VER}.tar.gz && \
    tar zxf v${GAMMA_VER}.tar.gz && \
    rm v${GAMMA_VER}.tar.gz && \
    mv GAMMA-${GAMMA_VER} GAMMA && \
    cd GAMMA && \
    chmod +x GAMMA.py && \
    chmod +x GAMMA-S.py

ENV PATH="${PATH}:/bin/blat:/GAMMA:/GAMMA/GAMMA.py:/GAMMA/GAMMA-S.py" LC_ALL=C

WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# Run GAMMA
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/008/632/635/GCF_008632635.1_ASM863263v1/GCF_008632635.1_ASM863263v1_genomic.fna.gz
RUN gunzip GCF_008632635.1_ASM863263v1_genomic.fna.gz
RUN GAMMA-S.py GCF_008632635.1_ASM863263v1_genomic.fna db.fasta GCF_008632635.1

# Check validity of outputs
RUN echo GCF_008632635.1.gamma
RUN cmp /data/test_GCF_008632635.1.gamma /data/GCF_008632635.1.gamma && cmp /data/test_GCF_008632635.1.psl /data/GCF_008632635.1.psl

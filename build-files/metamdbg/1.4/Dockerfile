ARG METAMDBG_VER=1.4

FROM ubuntu:noble AS builder
ARG METAMDBG_VER

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    build-essential \
    cmake \
    zlib1g-dev \
    libomp-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/GaetanBenoitDev/metaMDBG/archive/refs/tags/metaMDBG-${METAMDBG_VER}.tar.gz -O metaMDBG.tar.gz && \
    mkdir metaMDBG && \
    tar -xzf metaMDBG.tar.gz -C metaMDBG --strip-components=1 && \
    rm metaMDBG.tar.gz && \
    cd metaMDBG && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j 3 && \
    mv /opt/metaMDBG/build/bin/metaMDBG /usr/local/bin/metaMDBG


FROM ubuntu:noble AS app
ARG METAMDBG_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="metaMDBG"
LABEL software.version="${METAMDBG_VER}"
LABEL description="A fast and memory-efficient assembler designed for long and accurate metagenomics reads (e.g. PacBio HiFi, Nanopore R10)."
LABEL website="https://github.com/GaetanBenoitDev/metaMDBG"
LABEL license="https://github.com/GaetanBenoitDev/metaMDBG/blob/main/LICENSE.md"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

COPY --from=builder /usr/local/bin/metaMDBG /usr/local/bin/metaMDBG

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV LC_ALL=C

WORKDIR /data

CMD [ "metaMDBG", "--help" ]


FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# metaMDBG --help and metaMDBG --version print out the same thing.
RUN metaMDBG --help && \
    metaMDBG asm --help && \
    metaMDBG gfa --help

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/bactopia/bactopia-tests/raw/refs/heads/main/species/portiera/reads/nanopore/ERR3772599.fastq.gz && \
    metaMDBG asm --out-dir ./ERR3772599/ --in-ont ERR3772599.fastq.gz --threads 8 && \
    cd ERR3772599 && \
    gunzip contigs.fasta.gz && \
    head contigs.fasta


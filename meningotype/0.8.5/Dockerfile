ARG MENINGOTYPE_VER="0.8.5"
ARG ISPCR_VER="33"
ARG MLST_VER="2.23.0"
ARG ANY2FASTA_VER="0.4.2"

## Builder ##
FROM ubuntu:jammy AS builder

ARG ISPCR_VER
ARG MACHTYPE="x86_64-pc-linux-gnu"

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    unzip

RUN wget https://hgwdev.gi.ucsc.edu/~kent/src/isPcr${ISPCR_VER}.zip &&\
    unzip isPcr${ISPCR_VER}.zip &&\
    cd isPcrSrc &&\
    sed -i 's/-Werror//g' inc/common.mk &&\
    mkdir -p bin/$MACHTYPE &&\
    mkdir -p lib/$MACHTYPE &&\
    make HOME=$PWD MACHTYPE=${MACHTYPE} C_INCLUDE_PATH=/usr/include LIBRARY_PATH=/usr/lib CFLAGS="-fcommon" &&\
    mv bin/$MACHTYPE/* /usr/local/bin/

## App ##
FROM ubuntu:jammy AS app

ARG MENINGOTYPE_VER
ARG MLST_VER
ARG ANY2FASTA_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="meningotype"
LABEL software.version="${MENINGOTYPE_VER}"
LABEL description="In silico typing of Neisseria meningitidis"
LABEL website="https://github.com/MDU-PHL/meningotype"
LABEL license="https://github.com/MDU-PHL/meningotype?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# most of these dependencies are for mlst
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    libmoo-perl \
    liblist-moreutils-perl \
    libjson-perl \
    gzip \
    file \
    ncbi-blast+ \
    libfile-which-perl \
    curl \
    parallel \
    procps \
    python3 \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/* /usr/local/bin/

# get any2fasta; move binary to /usr/local/bin which is already in $PATH
RUN wget -q https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VER}.tar.gz && \
    tar xzf v${ANY2FASTA_VER}.tar.gz && \
    rm v${ANY2FASTA_VER}.tar.gz && \
    chmod +x any2fasta-${ANY2FASTA_VER}/any2fasta && \
    mv -v any2fasta-${ANY2FASTA_VER}/any2fasta /usr/local/bin && \
    rm -rf any2fasta-${ANY2FASTA_VER}

# get mlst
RUN wget -q https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz && \
    tar -xzf v${MLST_VER}.tar.gz && \
    rm -v v${MLST_VER}.tar.gz

# get meningotype
RUN wget -q https://github.com/MDU-PHL/meningotype/archive/refs/tags/v${MENINGOTYPE_VER}.tar.gz && \
    pip install --no-cache-dir v${MENINGOTYPE_VER}.tar.gz && \
    rm -rf v${MENINGOTYPE_VER}.tar.gz && \
    meningotype -h

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:" \
    LC_ALL=C.UTF-8

# update the database
RUN meningotype --updatedb

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "meningotype", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

## Test ##
FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN meningotype --help && \
    meningotype --version 

# Run the program's internal tests if available
RUN meningotype --test && \
    meningotype --test --finetype && \
    meningotype --test --all

# Option 2: write below common usage cases
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/022/869/645/GCA_022869645.1_ASM2286964v1/GCA_022869645.1_ASM2286964v1_genomic.fna.gz && \
    gzip -d GCA_022869645.1_ASM2286964v1_genomic.fna.gz && \
    meningotype GCA_022869645.1_ASM2286964v1_genomic.fna > results.txt && \
    head results.txt

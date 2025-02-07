# Set global variables
ARG CAT_VER="6.0.1"
ARG SAMTOOLS_VER="1.21"
ARG BWA_VER="0.7.18"
ARG DIAMOND_VER="2.1.10"


FROM ubuntu:jammy AS builder

ARG SAMTOOLS_VER
ARG BWA_VER
ARG DIAMOND_VER

# install dependencies required for compiling samtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    libdeflate-dev \
    gcc \
    wget \
    make \
    perl \
    bzip2 \
    gnuplot \
    ca-certificates

# download, compile, and install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install


RUN wget -q https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz &&\
    tar -xvf v${BWA_VER}.tar.gz &&\
    cd bwa-${BWA_VER} &&\
    make &&\
    mv bwa /usr/local/bin/

RUN wget -q https://github.com/bbuchfink/diamond/releases/download/v${DIAMOND_VER}/diamond-linux64.tar.gz &&\
    tar -C /usr/local/bin -xvf diamond-linux64.tar.gz && \
    rm diamond-linux64.tar.gz


# Application Stage
FROM ubuntu:jammy AS app
ARG CAT_VER


LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="CAT"
LABEL software.version=${CAT_VER}
LABEL description="CAT: a tool for taxonomic classification of contigs and metagenome-assembled genomes (MAGs)."
LABEL website="https://github.com/MGXlab/CAT_pack"
LABEL license.url="https://github.com/MGXlab/CAT_pack/blob/master/LICENSE.md"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    ca-certificates \
    python3 \
    python3-pip \
    prodigal && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/* /usr/local/bin/



RUN wget -q https://github.com/MGXlab/CAT_pack/archive/refs/tags/v${CAT_VER}.tar.gz && \
    tar -xvzf v${CAT_VER}.tar.gz && \
    chmod +x /CAT_pack-${CAT_VER}/CAT_pack/CAT_pack && \
    rm v${CAT_VER}.tar.gz


# Add CAT to PATH
ENV PATH="${PATH}:/CAT_pack-${CAT_VER}/CAT_pack"

CMD ["CAT_pack", "--help"]
WORKDIR /data

# Optional stage: Test data
FROM app AS test

ARG CAT_VER

WORKDIR /data/test

RUN CAT_pack --help && CAT_pack --version

RUN wget -nv --no-check-certificate \
    https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa \
    -O burk_wgs_pos_ctrl.fa &&\
    wget -nv --no-check-certificate \
    https://merenlab.org/data/refining-mags/files/GN02_MAG_IV_B_1-contigs.fa \
    -O GN02_MAG_IV_B_1-contigs.fa

# Prepare testing database
RUN mkdir -p db_tests && \
    gzip -d /CAT_pack-${CAT_VER}/tests/data/prepare/small.fa.gz && \
    CAT_pack prepare --db_fasta /CAT_pack-${CAT_VER}/tests/data/prepare/small.fa \
    --acc2tax /CAT_pack-${CAT_VER}/tests/data/prepare/prot2acc.txt \
    --names /CAT_pack-${CAT_VER}/tests/data/prepare/names.dmp \
    --nodes /CAT_pack-${CAT_VER}/tests/data/prepare/nodes.dmp \
    --db_dir db_tests/

# Running CAT on contigs
RUN CAT_pack contigs -c burk_wgs_pos_ctrl.fa \
    -d db_tests/db \
    -t db_tests/tax

# Running BAT on a set of MAGs
RUN CAT_pack bins -b GN02_MAG_IV_B_1-contigs.fa \
    -d db_tests/db \
    -t db_tests/tax

WORKDIR /data

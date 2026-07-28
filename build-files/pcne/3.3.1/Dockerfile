FROM python:3.13-slim AS app
ARG PCNE_VER="3.3.1"
ARG R_VER=4.4.3
ARG BWA_VER=0.7.18
ARG MINIMAP2_VER=2.3
ARG SAMTOOLS_VER=1.20
ARG BEDTOOLS_VER=2.31.1

LABEL base.image="python:3.13-slim"
LABEL dockerfile.version="1"
LABEL software="PCNE"
LABEL software.version="${PCNE_VER}"
LABEL description="A tool to estimate the copy numbers of plasmids detected in an assembled genome"
LABEL website="https://github.com/riccabolla/PCNE"
LABEL license="https://github.com/riccabolla/PCNE/blob/main/LICENSE"
LABEL maintainer="Riccardo Bollini"
LABEL maintainer.email="riccardo.bollini@hunimed.eu / bollach@virgilio.it"

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    wget \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libncurses5-dev \
    libcurl4-gnutls-dev \
    r-base \
    r-cran-readr \
    r-cran-dplyr \
    r-cran-ggplot2 \
    r-cran-purrr && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# BWA installation
RUN wget -q https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz && \
    tar -xzf v${BWA_VER}.tar.gz && \
    cd bwa-${BWA_VER} && \
    make && \
    mv bwa /usr/local/bin/ && \
    cd .. && \
    rm -rf bwa-${BWA_VER} v${BWA_VER}.tar.gz

# Minimap2 installation
RUN wget -q https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}.tar.bz2 && \
    tar -xjf minimap2-${MINIMAP2_VER}.tar.bz2 && \
    cd minimap2-${MINIMAP2_VER} && \
    make && \
    mv minimap2 /usr/local/bin/ && \
    cd .. && \
    rm -rf minimap2-${MINIMAP2_VER} minimap2-${MINIMAP2_VER}.tar.bz2

# Samtools installation
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf samtools-${SAMTOOLS_VER} samtools-${SAMTOOLS_VER}.tar.bz2

# Bedtools installation
RUN wget -q https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VER}/bedtools-${BEDTOOLS_VER}.tar.gz && \
    tar -xzf bedtools-${BEDTOOLS_VER}.tar.gz && \
    cd bedtools2 && \
    make && \
    mv bin/bedtools /usr/local/bin/ && \
    cd .. && \
    rm -rf bedtools2 bedtools-${BEDTOOLS_VER}.tar.gz

# PCNE installation
RUN wget -q https://github.com/riccabolla/PCNE/archive/refs/tags/v${PCNE_VER}.tar.gz && \
    tar -xzf v${PCNE_VER}.tar.gz && \
    mv PCNE-${PCNE_VER} /opt/PCNE && \
    chmod +x /opt/PCNE/bin/pcne /opt/PCNE/bin/pcne_long && \
    ln -s /opt/PCNE/bin/pcne /usr/local/bin/pcne && \
    ln -s /opt/PCNE/bin/pcne_long /usr/local/bin/pcne_long && \
    rm v${PCNE_VER}.tar.gz

ENV LC_ALL=C
ENV PATH="/opt/PCNE/bin:${PATH}"

WORKDIR /data

CMD [ "pcne", "--help" ]

FROM app AS test

WORKDIR /test

RUN pcne --help && \
    pcne --version && \
    pcne_long --help

RUN wget https://github.com/riccabolla/PCNE/releases/download/v3.3.1/pcne_test_data.tar.gz && \
    tar -xzf pcne_test_data.tar.gz && \
    pcne -c staph_B_test/CP003200.1_chrom.fasta \
         -p staph_B_test/CP003223.1_plasmid.fasta \
         -r staph_B_test/Sim_50x_1copy_R1.fastq.gz \
         -R staph_B_test/Sim_50x_1copy_R2.fastq.gz \
         -t 2 \
         -o test_output && \
    head test_output_results.tsv && \
    rm -rf pcne_test_data.tar.gz staph_B_test/ test_output*

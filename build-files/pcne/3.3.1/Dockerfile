ARG PCNE_VER=3.3.1
ARG R_VER=4.4.3
ARG BWA_VER=0.7.18
ARG MINIMAP2_VER=2.30
ARG SAMTOOLS_VER=1.20
ARG BEDTOOLS_VER=2.31.1

FROM rocker/r-ver:${R_VER} AS builder

ARG BWA_VER
ARG MINIMAP2_VER
ARG SAMTOOLS_VER
ARG BEDTOOLS_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libncurses-dev \
    python3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build

RUN wget -q https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz && \
    tar -xzf v${BWA_VER}.tar.gz && \
    cd bwa-${BWA_VER} && \
    make -j$(nproc) && \
    cp bwa /usr/local/bin/

RUN wget -q https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}.tar.bz2 && \
    tar -xjf minimap2-${MINIMAP2_VER}.tar.bz2 && \
    cd minimap2-${MINIMAP2_VER} && \
    make -j$(nproc) && \
    cp minimap2 /usr/local/bin/

RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure --prefix=/usr/local && \
    make -j$(nproc) && \
    make install

RUN wget -q https://github.com/arq5x/bedtools2/archive/refs/tags/v${BEDTOOLS_VER}.tar.gz && \
    tar -xzf v${BEDTOOLS_VER}.tar.gz && \
    cd bedtools2-${BEDTOOLS_VER} && \
    make -j$(nproc) && \
    cp bin/bedtools /usr/local/bin/

FROM rocker/r-ver:${R_VER} AS app

ARG PCNE_VER
ARG R_VER

LABEL base.image="rocker/r-ver:${R_VER}"
LABEL dockerfile.version="1"
LABEL software="PCNE"
LABEL software.version="${PCNE_VER}"
LABEL description="Plasmid Copy Number Estimator"
LABEL website="https://github.com/riccabolla/PCNE"
LABEL license="MIT"
LABEL maintainer="riccabolla"
LABEL maintainer.email="riccardo.bollini@hunimed.eu / bollach@virgilio.it"

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    wget \
    ca-certificates \
    zlib1g \
    libbz2-1.0 \
    liblzma5 \
    libcurl4 \
    libncurses6 && \
    rm -rf /var/lib/apt/lists/*

RUN install2.r --error --skipinstalled \
    readr \
    dplyr \
    ggplot2 \
    purrr

COPY --from=builder /usr/local/bin/bwa /usr/local/bin/
COPY --from=builder /usr/local/bin/minimap2 /usr/local/bin/
COPY --from=builder /usr/local/bin/samtools /usr/local/bin/
COPY --from=builder /usr/local/bin/bedtools /usr/local/bin/
COPY --from=builder /usr/local/lib/libhts* /usr/local/lib/

RUN ldconfig

WORKDIR /opt

# pcne installation
RUN wget -q https://github.com/riccabolla/PCNE/archive/refs/tags/v${PCNE_VER}.tar.gz && \
    tar -xzf v${PCNE_VER}.tar.gz && \
    mv PCNE-${PCNE_VER} PCNE && \
    chmod +x /opt/PCNE/bin/pcne /opt/PCNE/bin/pcne_long && \
    rm v${PCNE_VER}.tar.gz
ENV PATH="/opt/PCNE/bin:${PATH}" \
    LC_ALL=C

CMD ["pcne", "--help"]

WORKDIR /data

FROM app AS test

# test
WORKDIR /test

RUN pcne --help && \
    pcne --version && \
    pcne_long --help

RUN wget -q https://github.com/riccabolla/PCNE/releases/download/v${PCNE_VER}/pcne_test_data.tar.gz && \
    tar -xzf pcne_test_data.tar.gz && \
    pcne \
      -c staph_B_test/CP003200.1_chrom.fasta \
      -p staph_B_test/CP003223.1_plasmid.fasta \
      -r staph_B_test/Sim_50x_1copy_R1.fastq.gz \
      -R staph_B_test/Sim_50x_1copy_R2.fastq.gz \
      -t 2 \
      -o test_output && \
    head test_output_results.tsv && \
    rm -rf pcne_test_data.tar.gz staph_B_test/ test_output*

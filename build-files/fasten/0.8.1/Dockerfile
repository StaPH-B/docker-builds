# Heavily influenced by https://github.com/lskatz/fasten/blob/master/Dockerfile

ARG FASTEN_VER="0.8.1"

FROM rust:1.74 as builder

ARG FASTEN_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    linux-headers-amd64 \
    git \
    bc \
    libcurl4-openssl-dev \
    libseccomp-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/lskatz/fasten/archive/refs/tags/v${FASTEN_VER}.tar.gz && \
    tar -xzf v${FASTEN_VER}.tar.gz && \
    cd /fasten-${FASTEN_VER} && \
    cargo build --release

# just running some tests before moving on
RUN cd /fasten-${FASTEN_VER} && \
    cargo build && \
    for test in tests/fasten*.sh ; do bash $test ; done

FROM ubuntu:jammy as app

ARG FASTEN_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="fasten"
LABEL software.version="${FASTEN_VER}"
LABEL description="Interleaved fastq file QC and manipulation"
LABEL website="https://github.com/lskatz/fasten"
LABEL license="https://github.com/lskatz/fasten/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

COPY --from=builder /fasten-${FASTEN_VER}/target/release /usr/local/bin

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps \
    bsdmainutils \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH" LC_ALL=C

# runs --help on each tool while skipping the fasten files that end in .d
CMD for tool in $(ls /usr/local/bin/fasten* | grep -v .d$) ; do $tool --help ; done

WORKDIR /data

FROM app as test

WORKDIR /test

RUN for tool in $(ls /usr/local/bin/fasten* | grep -v .d$) ; do $tool --help ; done

# downloads some TB reads and does some basic QC on them
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_1.fastq.gz && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_2.fastq.gz && \
    zcat ERR1664619_1.fastq.gz ERR1664619_2.fastq.gz | fasten_shuffle | fasten_metrics | column -t > fasten_metrics.txt && \
    zcat ERR1664619_1.fastq.gz ERR1664619_2.fastq.gz | fasten_shuffle | fasten_clean --paired-end --min-length 2 | gzip -c > cleaned.shuffled.fastq.gz && \
    head fasten_metrics.txt && wc -l ERR1664619_1.fastq.gz ERR1664619_2.fastq.gz cleaned.shuffled.fastq.gz

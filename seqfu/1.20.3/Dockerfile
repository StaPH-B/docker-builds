# Set global variables
ARG SEQFU_VER="1.20.3"

# Stage 1: Build Dockerfile
FROM ubuntu:focal AS builder
ARG SEQFU_VER

# Metadata
LABEL base.image="ubuntu:focal" 
LABEL dockerfile.version="1" 
LABEL software="SeqFu"
LABEL software.version="${SEQFU_VER}"
LABEL description="A general-purpose program to manipulate and parse information from FASTA/FASTQ files, supporting gzipped input files."
LABEL website="https://github.com/telatin/seqfu2"
LABEL license.url="https://github.com/telatin/seqfu2?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email="ltj8@cdc.gov"

# Set non-interactive frontend and update PATH
ENV DEBIAN_FRONTEND=noninteractive \
    PATH="/root/.nimble/bin:${PATH}"

# Install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    build-essential \
    zlib1g-dev \
    curl \
    python3 \
    python3-pip \
    git \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /root

# Install Nim and SeqFu
RUN curl https://nim-lang.org/choosenim/init.sh -sSf | sh -s -- -y --ver 1.22.2 && \
    wget https://github.com/telatin/seqfu2/archive/refs/tags/v${SEQFU_VER}.tar.gz && \
    tar -xzf v${SEQFU_VER}.tar.gz && \
    rm v${SEQFU_VER}.tar.gz && \
    cd seqfu2-${SEQFU_VER} && \
    make

# Copy the built binary to a location in the PATH
RUN ls -l /root/seqfu2-${SEQFU_VER}/bin && \
    cp -R /root/seqfu2-${SEQFU_VER}/bin/* /usr/local/bin/ && \
    chmod +x /usr/local/bin/seqfu

# Stage 2: Create the final image
FROM ubuntu:focal AS app
ARG SEQFU_VER

# Copy the necessary files from the builder
COPY --from=builder /usr/local/bin /usr/local/bin

# Install minimal runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    wget && \
    rm -rf /var/lib/apt/lists/*

    


# Verify installation
RUN ls -l /usr/local/bin && \
seqfu --version && seqfu --help

# Running seqfu on test staph-b test dataset
FROM app AS test

WORKDIR /data/test

RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    seqfu check SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz > seqfu_check_test.txt && \
    seqfu count -f SRR13957123_1.fastq.gz -r SRR13957123_2.fastq.gz > seqfu_count_test.txt

WORKDIR /data

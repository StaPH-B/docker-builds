# Stage 1: Build stage
FROM ubuntu:focal AS builder

# Set global variables
ARG BINDASHTREE_VER="0.1.0"

# Update package manager and install necessary tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    build-essential \
    gcc \
    pkg-config \
    libssl-dev \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Rust and Cargo using rustup
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    export PATH="$HOME/.cargo/bin:$PATH" && \
    rustup default stable

# Ensure Rust and Cargo are available
ENV PATH="/root/.cargo/bin:$PATH"

# Download, extract, and build bindashtree
RUN wget https://github.com/jianshu93/bindashtree/archive/refs/tags/v${BINDASHTREE_VER}.tar.gz && \
    tar -xzvf v${BINDASHTREE_VER}.tar.gz && \
    cd bindashtree-${BINDASHTREE_VER} && \
    /root/.cargo/bin/cargo build --release

# Stage 2: Final image
FROM ubuntu:focal AS app
ARG BINDASHTREE_VER="0.1.0"

# Install wget for test stage compatibility
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Labels for metadata
LABEL base.image="ubuntu:focal" \
      dockerfile.version="1" \
      software="bindashtree" \
      software.version="${BINDASHTREE_VER}" \
      description="Binwise Densified MinHash and Rapid Neighbor-joining Tree Construction for microbial genomes." \
      website="https://github.com/jianshu93/bindashtree" \
      license.url="https://github.com/jianshu93/bindashtree?tab=MIT-1-ov-file#readme" \
      maintainer="Taylor K. Paisie" \
      maintainer.email="ltj8@cdc.gov"

# Copy built binaries from the builder stage
COPY --from=builder /bindashtree-${BINDASHTREE_VER}/target/release/bindashtree /usr/local/bin/

CMD ["bindashtree", "--help"]

WORKDIR /data

# Stage 3: Test stage
FROM app AS test

# Set working directory
WORKDIR /data/test

# Install wget if not installed (redundancy for safety)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Download test files
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/587/385/GCA_002587385.1_ASM258738v1/GCA_002587385.1_ASM258738v1_genomic.fna.gz && \
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/596/765/GCA_002596765.1_ASM259676v1/GCA_002596765.1_ASM259676v1_genomic.fna.gz && \
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/598/005/GCA_002598005.1_ASM259800v1/GCA_002598005.1_ASM259800v1_genomic.fna.gz

RUN ls /data/test/*.fna.gz > name.txt

#### for highly similar genomes, e.g., > 99.9% ANI, a large sketch size should be used. -s 10204 works well for ANI below 99%.
RUN bindashtree -i name.txt -k 16 -s 10240 -d 1 -t 8 --output_tree try.nwk

FROM app

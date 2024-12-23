# Set global variables
ARG BINDASHTREE_VER="0.1.0"

# Stage 1: Build stage
FROM ubuntu:focal AS builder

# Set version argument
ARG BINDASHTREE_VER

# Update package manager and install necessary tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    build-essential \
    gcc \
    pkg-config \
    libssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

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

# Set the version argument again for this stage
ARG BINDASHTREE_VER="0.1.0"

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

# Set default command
# CMD ["bindashtree", "-h"]

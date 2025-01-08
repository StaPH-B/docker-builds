# Set global variables
ARG HOCORT_VER="1.2.2"
ARG HISTAT2_VER="2.2.1"

# Base image for building
FROM ubuntu:jammy AS builder
ARG HOCORT_VER
ARG HISTAT2_VER

# Set non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential g++ unzip gcc git wget curl \
    libboost-all-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev \
    libssl-dev zlib1g-dev cmake python3.10 python3-pip \
    bowtie2 kraken2 bwa minimap2 samtools bbmap \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# BWA-MEM2 installation
RUN git clone --recursive https://github.com/bwa-mem2/bwa-mem2.git && \
    cd bwa-mem2 && \
    make -j$(nproc) && \
    cp bwa-mem2* /usr/local/bin && \
    rm -rf /bwa-mem2

# HISAT2 installation
RUN wget -q https://github.com/DaehwanKimLab/hisat2/archive/refs/tags/v${HISTAT2_VER}.tar.gz && \
    tar -xzf v${HISTAT2_VER}.tar.gz && \
    cd hisat2-${HISTAT2_VER} && make -j$(nproc) && \
    cp hisat2 hisat2-build /usr/local/bin/ && \
    cd .. && rm -rf hisat2-${HISTAT2_VER} v${HISTAT2_VER}.tar.gz

# Install sparsehash
RUN git clone --depth 1 https://github.com/sparsehash/sparsehash.git && \
    cd sparsehash && ./configure && make && make install && \
    cd .. && rm -rf sparsehash

# Install SDSL
RUN git clone --depth 1 https://github.com/simongog/sdsl-lite.git && \
    cd sdsl-lite/build && cmake .. && make && make install && \
    cd ../.. && rm -rf sdsl-lite

# Install BTL Bloom filter
RUN git clone https://github.com/bcgsc/btl_bloomfilter.git && \
    cd btl_bloomfilter && \
    chmod +x autogen.sh && \
    ./autogen.sh && \
    ./configure && \
    make && make install && \
    mkdir -p /usr/local/include/btl_bloomfilter && \
    cp -r *.hpp vendor /usr/local/include/btl_bloomfilter && \
    cd .. && rm -rf btl_bloomfilter

# Install BioBloom
RUN git clone https://github.com/bcgsc/biobloom.git && \
    cd biobloom && \
    chmod +x autogen.sh && \
    ./autogen.sh && \
    ./configure CXXFLAGS="-I/usr/local/include/btl_bloomfilter" LDFLAGS="-L/usr/local/lib" && \
    make && make install && \
    cd .. && rm -rf biobloom

# Install HoCoRT
RUN wget -q https://github.com/ignasrum/hocort/archive/refs/tags/${HOCORT_VER}.tar.gz && \
    tar -xzf ${HOCORT_VER}.tar.gz && cd hocort-${HOCORT_VER} && \
    pip3 install --no-cache-dir . && cd .. && \
    rm -rf hocort-${HOCORT_VER} ${HOCORT_VER}.tar.gz

# Final stage: Application image
FROM ubuntu:jammy AS app
ARG HOCORT_VER
ARG HISTAT2_VER

# Set up labels
LABEL base.image="ubuntu:jammy" \
      dockerfile.version="1" \
      software="HoCoRT" \
      software.version=${HOCORT_VER} \
      description="Remove specific organisms from sequencing reads." \
      website="https://github.com/ignasrum/hocort" \
      license.url="https://github.com/ignasrum/hocort?tab=MIT-1-ov-file#readme" \
      maintainer="Taylor K. Paisie" \
      maintainer.email="ltj8@cdc.gov"

# Copy runtime files
COPY --from=builder /usr/ /usr/

# Set up working directory
WORKDIR /data

# Verify installation
RUN hocort --version

# Optional: Test stage
FROM app AS test

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl && \
    mkdir test && \
    curl -L -o test/genome.fna https://raw.githubusercontent.com/ignasrum/hocort/main/tests/test_data/fasta/genome.fna && \
    hocort index bowtie2 --input test/genome.fna --output test/hocort_test && \
    rm -rf /var/lib/apt/lists/*


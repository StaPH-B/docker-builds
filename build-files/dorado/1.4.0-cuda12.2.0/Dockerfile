# Use NVIDIA CUDA image as the base image
FROM nvidia/cuda:12.2.0-base-ubuntu24.04 AS app

ARG DORADO_VER="1.4.0"

# Metadata
LABEL base.image="nvidia/cuda:12.2.0-base-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="dorado ${DORADO_VER}"
LABEL software.version="${DORADO_VER}"
LABEL description="A tool for basecalling Fast5/Pod5 files from Oxford Nanopore sequencing"
LABEL website="https://github.com/nanoporetech/dorado"
LABEL license="https://github.com/nanoporetech/dorado/blob/master/LICENSE"
LABEL original.website="https://nanoporetech.github.io/dorado/"
LABEL maintainer="Fraser Combe"
LABEL maintainer.email="fraser.combe@theiagen.com"

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    pigz && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Download and extract Dorado package
RUN wget -q https://cdn.oxfordnanoportal.com/software/analysis/dorado-${DORADO_VER}-linux-x64.tar.gz &&\
    tar --strip-components=1 -C /usr/local/ -xvf dorado-${DORADO_VER}-linux-x64.tar.gz &&\
    rm dorado-${DORADO_VER}-linux-x64.tar.gz

# Set environment variables
ENV LC_ALL=C

# Download basecalling models
RUN mkdir /dorado_models && \
    cd /dorado_models && \
    dorado download --model all

# Default command
CMD ["dorado", "-h"]

WORKDIR /data

# -----------------------------
# Test Stage
# -----------------------------
FROM app AS test

# Download the specific Pod5 test file
RUN wget https://github.com/nanoporetech/dorado/raw/release-v1.1/tests/data/pod5/dna_r10.4.1_e8.2_400bps_5khz/dna_r10.4.1_e8.2_400bps_5khz-FLO_PRO114M-SQK_LSK114_XL-5000.pod5

# Run test command (using CPU mode)
RUN dorado basecaller \
    --device cpu \
    /dorado_models/dna_r10.4.1_e8.2_400bps_sup@v5.2.0 \
    dna_r10.4.1_e8.2_400bps_5khz-FLO_PRO114M-SQK_LSK114_XL-5000.pod5 \
    --emit-moves --max-reads 10 > basecalled.sam

# Verify the output file exists and is not empty
RUN test -s basecalled.sam

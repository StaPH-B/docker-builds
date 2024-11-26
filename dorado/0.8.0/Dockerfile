# Use NVIDIA CUDA image as the base image
FROM nvidia/cuda:12.2.0-devel-ubuntu20.04 AS app

ARG DORADO_VER=0.8.0

# Metadata
LABEL base.image="nvidia/cuda:12.2.0-devel-ubuntu20.04"
LABEL dockerfile.version="1"
LABEL software="dorado ${DORADO_VER}"
LABEL software.version="${DORADO_VER}"
LABEL description="A tool for basecalling Fast5/Pod5 files from Oxford Nanopore sequencing"
LABEL website="https://github.com/nanoporetech/dorado"
LABEL license="https://github.com/nanoporetech/dorado/blob/master/LICENSE"
LABEL original.website="https://nanoporetech.github.io/dorado/"
LABEL maintainer="Fraser Combe"
LABEL maintainer.email="fraser.combe@theiagen.com"

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Download and extract Dorado package
RUN wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-${DORADO_VER}-linux-x64.tar.gz \
    && tar -xzvf dorado-${DORADO_VER}-linux-x64.tar.gz -C /opt \
    && rm dorado-${DORADO_VER}-linux-x64.tar.gz

# Set environment variables for Dorado binary
ENV PATH="/opt/dorado-${DORADO_VER}-linux-x64/bin:${PATH}"

# Download basecalling models
RUN mkdir /dorado_models && \
    cd /dorado_models && \
    dorado download --model all

# Default command
CMD ["dorado"]

# -----------------------------
# Test Stage
# -----------------------------
FROM app AS test


# Download the specific Pod5 test file
RUN wget -O /usr/src/app/dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5 \
  https://github.com/nanoporetech/dorado/raw/release-v0.7/tests/data/pod5/dna_r10.4.1_e8.2_260bps/\
dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5

# Set working directory
WORKDIR /usr/src/app

# Run test command (using CPU mode)
RUN dorado basecaller \
    --device cpu \
    /dorado_models/dna_r10.4.1_e8.2_260bps_sup@v3.5.2 \
    dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5 \
    --emit-moves --max-reads 10 > basecalled.sam

# Verify the output file exists and is not empty
RUN test -s basecalled.sam

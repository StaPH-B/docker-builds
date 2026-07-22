FROM ubuntu:noble AS app

# Set the DnaApler version
ARG DNAAPLER_VER="1.4.0"
ARG MMSEQS2_VER="18-8cc5c"

# Metadata labels
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="dnaapler"
LABEL software.version="${DNAAPLER_VER}"
LABEL description="Rotates chromosomes and more"
LABEL website="https://github.com/gbouras13/dnaapler"
LABEL license="MIT"
LABEL license.url="https://github.com/gbouras13/dnaapler/blob/main/LICENSE"
LABEL maintainer="Fraser Combe"
LABEL maintainer.email="fraser.combe@theiagen.com"

# Install dependencies; clean up APT garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/soedinglab/MMseqs2/releases/download/${MMSEQS2_VER}/mmseqs-linux-sse41.tar.gz && \
    tar -vxf mmseqs-linux-sse41.tar.gz && \
    rm mmseqs-linux-sse41.tar.gz

RUN wget https://github.com/gbouras13/dnaapler/archive/refs/tags/v1.4.0.tar.gz && \
    pip install --no-cache-dir --break-system-packages  v1.4.0.tar.gz && \
    rm v1.4.0.tar.gz

# Set PATH and LC_ALL for compatibility
ENV PATH="/mmseqs/bin:$PATH" \
    LC_ALL=C.UTF-8

# Set working directory to /data
WORKDIR /data

# Default command to display help
CMD [ "dnaapler", "--help" ]

# New stage for testing
FROM app AS test

# Set working directory to /test
WORKDIR /test

# Test the tool installation and functionality
RUN dnaapler --help && dnaapler --version

# Download test genome and run DnaApler commands
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/025/259/185/GCA_025259185.1_ASM2525918v1/GCA_025259185.1_ASM2525918v1_genomic.fna.gz && \
    gunzip GCA_025259185.1_ASM2525918v1_genomic.fna.gz && \
    grep "CP104365.1" GCA_025259185.1_ASM2525918v1_genomic.fna -A 50000 > CP104365.1.fasta && \
    dnaapler mystery --prefix mystery_test --output mystery_test -i CP104365.1.fasta && \ 
    dnaapler plasmid --prefix plasmid_test --output plasmid_test -i CP104365.1.fasta && \
    ls mystery_test plasmid_test

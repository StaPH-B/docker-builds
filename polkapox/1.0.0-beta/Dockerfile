##### Building stage #####

# Stage 1: Build Python environment with required packages
FROM python:3.8-slim as app

ARG SOFTWARENAME_VER="1.0.0-beta"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Add metadata
LABEL authors="CDC PolkaPox Team"
LABEL description="Container used in the PolkaPox pipeline by graph_reconstruct.nf module"
LABEL base.image="python:3.8-slim"
LABEL dockerfile.version="1"
LABEL software="polkapox"
LABEL software.version="${SOFTWARENAME_VER}"
LABEL website="https://github.com/CDCgov/polkapox"
LABEL license="https://github.com/CDCgov/polkapox/blob/master/LICENSE"
LABEL maintainer="CDC PolkaPox Group"
LABEL maintainer.email="yrh8@cdc.gov"

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libopenblas-dev \
    wget \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install Python packages
RUN pip install --no-cache-dir \
    biopython==1.83 \
    numpy==1.24.4 \
    mkl==2024.0.0 \
    networkx==3.1 \
    gfapy==1.2.3

# Set a work dir for the Blast+ install
WORKDIR /src

# Install NCBI BLAST+
ARG BLAST_VER=2.15.0

RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    mkdir /data

# Add blast executable to path
ENV PATH="/src/ncbi-blast-${BLAST_VER}+/bin:${PATH}" \
    LC_ALL=C

# Set the working directory
WORKDIR /data

# Set the default command
CMD echo "The polkapox container is not intended to run independently of the workflow. See https://github.com/CDCgov/polkapox"

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app as test

# Set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

###### Testing Stage ######
RUN blastn -version

# Copy and run test files
COPY LIY15561A68_2022_1748_IN.assembly.gfa.gz /test/.

RUN gunzip LIY15561A68_2022_1748_IN.assembly.gfa.gz && \
    wget -q https://raw.githubusercontent.com/CDCgov/polkapox/master/assets/MPXV-UK_P2.noN_39086_40204.fasta && \
    wget -q https://raw.githubusercontent.com/CDCgov/polkapox/master/bin/mpxv-AssemblyGraph_gfaPy.py && \
    cat LIY15561A68_2022_1748_IN.assembly.gfa | awk 'BEGIN { FS="\t" } /^S/{ if( length($3) >= 1) print ">Contig"$2"_len"substr($4,6)"_cov"substr($5,6,5)"\n"$3}' | fold > LIY15561A65_2022_1744_NE.contigs.fasta && \
    python mpxv-AssemblyGraph_gfaPy.py \
        -i /test/LIY15561A68_2022_1748_IN.assembly.gfa \
        -r /test/MPXV-UK_P2.noN_39086_40204.fasta \
        -o . && \
        head /test/LIY15561A68_2022_1748_IN.assembly.log /test/LIY15561A68_2022_1748_IN.assembly.summary && \
        wc -l LIY15561A68_2022_1748_IN.assembly_longest.fasta

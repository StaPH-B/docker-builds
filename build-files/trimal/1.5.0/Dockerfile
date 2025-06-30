ARG TRIMAL_VER="1.5.0"

##### ----- STAGE 1: app ----- #####
FROM ubuntu:jammy AS app

# Set software version
ARG TRIMAL_VER

# Metadata labels
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="TrimAl"
LABEL software.version="${TRIMAL_VER}"
LABEL description="trimAl is a tool for the automated removal of spurious sequences or poorly aligned regions from a multiple sequence alignment."
LABEL website="https://github.com/inab/trimal"
LABEL documentation="https://vicfero.github.io/trimal/"
LABEL license="https://github.com/inab/trimal/blob/trimAl/LICENSE"
LABEL maintainer="Rong Jin"
LABEL maintainer.email="jinrongshanghai@gmail.com"

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    unzip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Download and build TrimAl
RUN wget https://github.com/inab/trimal/releases/download/v${TRIMAL_VER}/trimAl_Linux_x86-64.zip && \
    unzip trimAl_Linux_x86-64.zip && \
    rm trimAl_Linux_x86-64.zip

# Set ENV variables
ENV PATH="/trimAl_Linux_x86-64:$PATH" \
    LC_ALL=C

# Default working directory and command
WORKDIR /data

CMD ["trimal", "-h"]

##### ----- STAGE 2: test ----- #####
FROM app AS test

ARG TRIMAL_VER

WORKDIR /test

# Run basic version test
RUN trimal -h && trimal --version

RUN wget https://github.com/inab/trimal/archive/refs/tags/v${TRIMAL_VER}.tar.gz && \
    tar -vxf v${TRIMAL_VER}.tar.gz

#RUN ls && ls trimal-${TRIMAL_VER}/dataset && whatever

# Functional test using the embedded example file
RUN trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -automated1 && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -strict && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -strictplus && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -gappyout && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -gt 0.5 -gw 2 && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -st 0.5 -sw 2 && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -selectseqs { 0,4 } && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -selectcols { 1-4 } && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -nogaps && \
    trimal -in trimal-${TRIMAL_VER}/dataset/example.007.AA.fasta -noallgaps



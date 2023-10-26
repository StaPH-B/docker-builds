FROM ubuntu:jammy as app

ARG POLYPOLISH_VER="0.5.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="polypolish"
LABEL software.version="${POLYPOLISH_VER}"
LABEL description="Polypolish is a tool for polishing genome assemblies with short reads."
LABEL website="https://github.com/rrwick/Polypolish"
LABEL license="https://github.com/rrwick/Polypolish/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    unzip \
    python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

# install polypolish without rust et al.
RUN wget -q https://github.com/rrwick/Polypolish/releases/download/v${POLYPOLISH_VER}/polypolish-linux-x86_64-musl-v${POLYPOLISH_VER}.tar.gz && \
    tar -xf polypolish-linux-x86_64-musl-v${POLYPOLISH_VER}.tar.gz && \
    rm polypolish-linux-x86_64-musl-v${POLYPOLISH_VER}.tar.gz 

# getting polypolish_insert_filter.py
RUN wget -q https://github.com/rrwick/Polypolish/archive/refs/tags/v${POLYPOLISH_VER}.tar.gz && \
    tar -xf v${POLYPOLISH_VER}.tar.gz && \
    cp Polypolish-0.5.0/scripts/polypolish_insert_filter.py . && \
    rm v${POLYPOLISH_VER}.tar.gz && \
    rm -rf Polypolish-0.5.0

ENV LC_ALL=C

WORKDIR /data

FROM app as test

RUN polypolish --help && polypolish --version && polypolish_insert_filter.py --help && polypolish_insert_filter.py --version

# using "toy" data
RUN wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/assembly.fasta && \
    wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/alignments.sam && \
    polypolish assembly.fasta alignments.sam > polished.fasta
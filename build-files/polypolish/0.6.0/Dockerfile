ARG POLYPOLISH_VER="0.6.0"

FROM rust:1.75 as builder

ARG POLYPOLISH_VER

RUN wget -q https://github.com/rrwick/Polypolish/archive/refs/tags/v${POLYPOLISH_VER}.tar.gz && \
    tar -vxf v${POLYPOLISH_VER}.tar.gz && \
    cd /Polypolish-${POLYPOLISH_VER} && \
    cargo build --release 

FROM ubuntu:jammy as app

ARG POLYPOLISH_VER

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

COPY --from=builder /Polypolish-${POLYPOLISH_VER}/target/release/polypolish /usr/local/bin/polypolish

ENV LC_ALL=C

CMD polypolish --help

WORKDIR /data

FROM app as test

RUN polypolish --help && polypolish --version

# using "toy" data
RUN wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/assembly.fasta && \
    wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/alignments.sam && \
    polypolish polish assembly.fasta alignments.sam > polished.fasta

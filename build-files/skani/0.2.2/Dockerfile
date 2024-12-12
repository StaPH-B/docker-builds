ARG SKANI_VER="0.2.2"

## Builder ##
FROM rust:1.80.1 AS builder

ARG SKANI_VER

RUN wget https://github.com/bluenote-1577/skani/archive/refs/tags/v${SKANI_VER}.tar.gz &&\
    tar -xvf v${SKANI_VER}.tar.gz &&\
    cd skani-${SKANI_VER} &&\
    cargo install --path . --root ~/.cargo &&\
    chmod +x /root/.cargo/bin/skani

## App ##
FROM ubuntu:jammy AS app

ARG SKANI_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="skani"
LABEL software.version=${SKANI_VER}
LABEL description="skani is a program for calculating average nucleotide identity (ANI) from DNA sequences (contigs/MAGs/genomes) for ANI > ~80%."
LABEL website="https://github.com/bluenote-1577/skani"
LABEL license="https://github.com/bluenote-1577/skani/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# copy app from builder stage
COPY --from=builder /root/.cargo/bin/skani /usr/local/bin/skani

# default run command
CMD ["skani", "-h"]

# singularity compatibility
ENV LC_ALL=C

WORKDIR /data

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y wget &&\
    wget https://github.com/bluenote-1577/skani/raw/v0.2.0/refs/e.coli-EC590.fasta &&\
    wget https://github.com/bluenote-1577/skani/raw/v0.2.0/refs/e.coli-K12.fasta

RUN skani dist e.coli-EC590.fasta e.coli-K12.fasta
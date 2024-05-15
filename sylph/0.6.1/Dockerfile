ARG SYLPH_VER="0.6.1"

## Builder ##
FROM rust:1.74 as builder

ARG SYLPH_VER

RUN apt update && \
    apt install -y cmake && \
    wget -q https://github.com/bluenote-1577/sylph/archive/refs/tags/v${SYLPH_VER}.tar.gz && \
    tar -xvf v${SYLPH_VER}.tar.gz && \
    cd sylph-${SYLPH_VER} && \
    cargo install --path . --root ~/.cargo && \
    chmod +x /root/.cargo/bin/sylph

## App ##
FROM ubuntu:jammy as app

ARG SYLPH_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="sylph"
LABEL software.version=${SYLPH_VER}
LABEL description="sylph is a program that can perform ultrafast (1) ANI querying or (2) metagenomic profiling for metagenomic shotgun samples."
LABEL website="https://github.com/bluenote-1577/sylph"
LABEL license="https://github.com/bluenote-1577/sylph/blob/main/LICENSE"
LABEL maintainer="Stephen Turner"
LABEL maintainer.email="vustephen@gmail.com"

# copy app from builder stage
COPY --from=builder /root/.cargo/bin/sylph /usr/local/bin/sylph

# default run command
CMD sylph -h

# singularity compatibility
ENV LC_ALL=C

# final working directory in app layer is /data
WORKDIR /data

## Test ##
FROM app as test

# making sure sylph is in PATH
RUN sylph -h

ARG SYLPH_VER

RUN apt update && apt install -y wget

WORKDIR /test

COPY --from=builder /sylph-${SYLPH_VER}/test_files/* /test

RUN date && \
    sylph sketch -i e.coli-*.fasta.gz -o database && \
    sylph sketch o157_reads.fastq.gz  && \
    sylph query database.syldb *.sylsp > ani_queries.tsv && \
    sylph profile database.syldb *.sylsp > profiling.tsv && \
    cat *.tsv && \
    date

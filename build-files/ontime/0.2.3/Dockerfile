ARG ONTIME_VER="0.2.3"
ARG TARGET="x86_64-unknown-linux-musl"

FROM rust:1.70 AS builder

ARG ONTIME_VER
ARG TARGET

RUN apt update \
    && apt install -y musl-tools

RUN wget -q https://github.com/mbhall88/ontime/archive/refs/tags/${ONTIME_VER}.tar.gz && \
    tar zxf ${ONTIME_VER}.tar.gz && \
    rm ${ONTIME_VER}.tar.gz && \
    ls / && \
    cd /ontime-${ONTIME_VER} && \
    rustup target add "${TARGET}" && \
    cargo build --release --target "${TARGET}" && \
    strip target/${TARGET}/release/ontime

FROM ubuntu:jammy as app

ARG ONTIME_VER
ARG TARGET

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="ontime"
LABEL software.version="${ONTIME_VER}"
LABEL description="Filters nanopore reads by time"
LABEL website="https://github.com/mbhall88/ontime"
LABEL license="https://github.com/mbhall88/ontime/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

COPY --from=builder /ontime-${ONTIME_VER}/target/${TARGET}/release/ontime /bin/

# for playing nice with workflow managers
RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  procps && \
  apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH" \
 LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD ontime --help

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
# The test stage must be downstream from 'app'
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN ontime --help && \
    ontime --version

COPY tests/test.fastq.gz .

RUN ontime --to 1h test.fastq.gz -o ontime.test.txt && \
    head ontime.test.txt
# -------------------------------
# STAGE 1 — Build trimal from source
# -------------------------------
FROM ubuntu:16.04 AS build

ARG TRIMAL_VERSION="v1.2rev59"
ENV DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="trimal"
LABEL software.version=$TRIMAL_VERSION
LABEL description="trimAl is a tool for the automated removal of spurious sequences or poorly aligned regions from a multiple sequence alignment."
LABEL website="https://vicfero.github.io/trimal/"
LABEL license="https://github.com/inab/trimal?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer=""
LABEL maintainer.email=""

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# Download and extract trimal source
RUN wget https://github.com/user-attachments/files/17989858/trimal.v1.2rev59.tar.gz -O trimal.tar.gz && \
    tar -xzf trimal.tar.gz

# Compile
WORKDIR /opt/trimAl/source
RUN make

# -------------------------------
# STAGE 2 — Minimal Runtime
# -------------------------------
FROM ubuntu:16.04 AS runtime

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:${PATH}"

RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy only final binary
COPY --from=build /opt/trimAl/source/trimal /usr/local/bin/trimal

WORKDIR /data

# -------------------------------
# STAGE 3 — Test
# -------------------------------
FROM runtime AS test

# Simple version test
RUN trimal --version


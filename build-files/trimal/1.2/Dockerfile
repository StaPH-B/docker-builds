##### ----- STAGE 1: app ----- #####
FROM ubuntu:focal AS app

# Set software version
ARG TRIMAL_VER="v1.2rev59"

# Metadata labels
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="TrimAl"
LABEL software.version="${TRIMAL_VER}"
LABEL description="trimAl is a tool for the automated removal of spurious sequences or poorly aligned regions from a multiple sequence alignment."
LABEL website="https://github.com/inab/trimal"
LABEL documentation="https://vicfero.github.io/trimal/"
LABEL license="https://github.com/inab/trimal?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer="Rong Jin"
LABEL maintainer.email="jinrongshanghai@gmail.com"

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Download and build TrimAl
WORKDIR /opt
RUN wget https://github.com/user-attachments/files/17989858/trimal.${TRIMAL_VER}.tar.gz -O trimal.tar.gz && \
    tar -xzf trimal.tar.gz && \
    rm trimal.tar.gz

WORKDIR /opt/trimAl/source
RUN make && \
    cp trimal /usr/local/bin/

# Set ENV variables
ENV PATH="/usr/local/bin:$PATH" \
    LC_ALL=C

# Default working directory and command
WORKDIR /data
CMD ["trimal", "--help"]

##### ----- STAGE 2: test ----- #####
FROM app AS test

WORKDIR /test

# Run basic version test
RUN trimal --version

# Functional test using the embedded example file
RUN trimal -in /opt/trimAl/dataset/example1.clw -automated1


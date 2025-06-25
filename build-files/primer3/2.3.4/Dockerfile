##### ----- STAGE 1: app ----- #####
FROM ubuntu:16.04 AS app

ARG PRIMER3_VERSION="2.3.4"
ENV DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:16.04"
LABEL dockerfile.version="1"
LABEL software="Primer3"
LABEL software.version=$PRIMER3_VERSION
LABEL description="Primer3 is a widely used open-source tool for designing PCR primers."
LABEL website="https://github.com/primer3-org/primer3"
LABEL license="https://github.com/primer3-org/primer3/tree/v2.3.4"
LABEL maintainer="FirstName LastName"
LABEL maintainer.email="my.email@email.com"


# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    unzip \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Build Primer3 from source
WORKDIR /opt
RUN wget https://github.com/primer3-org/primer3/archive/refs/tags/v${PRIMER3_VERSION}.tar.gz && \
    tar -xzf v${PRIMER3_VERSION}.tar.gz && \
    rm v${PRIMER3_VERSION}.tar.gz

WORKDIR /opt/primer3-${PRIMER3_VERSION}/src
RUN make

# Copy binaries to standard path
RUN cp primer3_core /usr/local/bin/ && \
    mkdir -p /usr/local/share/primer3_config && \
    cp -r primer3_config/* /usr/local/share/primer3_config/

# Set environment variables
ENV PRIMER3_CONFIG=/usr/local/share/primer3_config \
    PATH="/usr/local/bin:$PATH" \
    LC_ALL=C

# Default command
CMD ["primer3_core", "--help"]

# Working directory
WORKDIR /data

##### ----- STAGE 2: test ----- #####
FROM app AS test

WORKDIR /test

# Simple test for primer3_core
RUN echo -e "=SEQUENCE_ID=Test\nSEQUENCE_TEMPLATE=ATCGATCGATCG\nPRIMER_TASK=generic\nPRIMER_THERMODYNAMIC_PARAMETERS_PATH=${PRIMER3_CONFIG}/\n=" > test_input.txt && \
    primer3_core test_input.txt


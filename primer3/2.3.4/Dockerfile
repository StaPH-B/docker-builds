# -------------------------------
# STAGE 1 — Build Primer3
# -------------------------------
FROM ubuntu:16.04 AS build

ARG PRIMER3_VERSION="2.3.4"
ENV DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Primer3"
LABEL software.version=$PRIMER3_VERSION
LABEL description="Primer3 is a widely used open-source tool for designing PCR primers."
LABEL website="https://github.com/primer3-org/primer3"
LABEL license="https://github.com/primer3-org/primer3/tree/v2.3.4"
LABEL maintainer=""
LABEL maintainer.email=""

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# Download and extract Primer3 source
RUN wget https://github.com/primer3-org/primer3/archive/refs/tags/v${PRIMER3_VERSION}.tar.gz && \
    tar -xzf v${PRIMER3_VERSION}.tar.gz

# Compile
WORKDIR /opt/primer3-${PRIMER3_VERSION}/src
RUN make

# -------------------------------
# STAGE 2 — Minimal Runtime
# -------------------------------
FROM ubuntu:16.04 AS runtime

ARG PRIMER3_VERSION="2.3.4"
ENV DEBIAN_FRONTEND=noninteractive
ENV PRIMER3_CONFIG=/usr/local/share/primer3_config
ENV PATH="/usr/local/bin:${PATH}"

RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy only required files from build stage
COPY --from=build /opt/primer3-${PRIMER3_VERSION}/src/primer3_core /usr/local/bin/
COPY --from=build /opt/primer3-${PRIMER3_VERSION}/src/primer3_config ${PRIMER3_CONFIG}

WORKDIR /data

# -------------------------------
# STAGE 3 — Test (optional)
# -------------------------------
FROM runtime AS test

# Test: verify primer3_core works with config
RUN echo -e "=SEQUENCE_ID=Test\nSEQUENCE_TEMPLATE=ATCGATCGATCG\nPRIMER_TASK=generic\nPRIMER_THERMODYNAMIC_PARAMETERS_PATH=${PRIMER3_CONFIG}/\n=" > test_input.txt && \
    primer3_core test_input.txt


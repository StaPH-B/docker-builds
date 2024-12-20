ARG FLYE_VER="2.9.5"

FROM ubuntu:jammy as builder

ARG FLYE_VER

RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    gcc \
    g++ \
    python3 \
    python3-pip \
    python3-setuptools \
    zlib1g-dev \
    wget \
    ca-certificates \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget -q https://github.com/fenderglass/Flye/archive/${FLYE_VER}.tar.gz && \
    tar -xf ${FLYE_VER}.tar.gz && \
    cd Flye-${FLYE_VER} && \
    python3 setup.py install

FROM ubuntu:jammy as app

ARG FLYE_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Flye"
LABEL software.version="${FLYE_VER}"
LABEL description="Fast and accurate de novo assembler for single molecule sequencing reads"
LABEL website="https://github.com/fenderglass/Flye"
LABEL license="https://github.com/fenderglass/Flye/blob/flye/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# Minimal requirements to run Flye in final image
# python3-distutils is required for test_toy.py , but might not be needed at runtime
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-distutils \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

COPY --from=builder /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /data
CMD ["flye", "--help"]

# For Singularity compatibility
ENV LC_ALL=C

FROM app as test

# Run Flye version and help for quick validation
RUN flye --version && flye --help

# Copy Flye source files from builder for running tests
COPY --from=builder /Flye-${FLYE_VER} /Flye-${FLYE_VER}

# Run Flye's built-in toy dataset test
RUN python3 /Flye-${FLYE_VER}/flye/tests/test_toy.py

# Download test data and perform an assembly
RUN apt-get update && apt-get install --no-install-recommends -y wget ca-certificates && \
    wget -q https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz && \
    flye --nano-raw ERR3772599.fastq.gz -o flye-test-portiera -t 2

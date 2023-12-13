
ARG GENOMAD_VER="1.7.4"
ARG ARAGORN_VER="1.2.41"
ARG MMSEQS2_VER="15-6f452"

FROM ubuntu:jammy as builder

ARG ARAGORN_VER

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    libc6-dev \
    make \
    gcc \
    wget

# get ARAGORN
RUN wget -q https://www.ansikte.se/ARAGORN/Downloads/aragorn${ARAGORN_VER}.c && \
    gcc -O3 -ffast-math -finline-functions -o aragorn aragorn${ARAGORN_VER}.c && \
    /aragorn -h 

FROM ubuntu:jammy as app

ARG GENOMAD_VER
ARG MMSEQS2_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="geNomad"
LABEL software.version="${GENOMAD_VER}"
LABEL description="Identification of mobile genetic elements"
LABEL website="https://github.com/apcamargo/genomad/"
LABEL license="https://github.com/apcamargo/genomad/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

COPY --from=builder /aragorn /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps \
    python3 \
    python3-pip \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get MMSEQS2
RUN wget -q https://github.com/soedinglab/MMseqs2/releases/download/${MMSEQS2_VER}/mmseqs-linux-avx2.tar.gz && \
    tar -xvf mmseqs-linux-avx2.tar.gz && \
    rm mmseqs-linux-avx2.tar.gz

# get genomad
RUN wget -q https://github.com/apcamargo/genomad/archive/refs/tags/v${GENOMAD_VER}.tar.gz && \
    python3 -m pip install v${GENOMAD_VER}.tar.gz && \
    rm -rf v${GENOMAD_VER}.tar.gz && \
    mkdir /data

ENV PATH="/mmseqs/bin:$PATH"

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD genomad --help

# 'WORKDIR' sets working directory
WORKDIR /data

FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN genomad --help && \
    genomad --version && \
    aragorn -h && \
    mmseqs -h

RUN genomad download-database . 
#&& \
#    genomad end-to-end input.fna output genomad_db


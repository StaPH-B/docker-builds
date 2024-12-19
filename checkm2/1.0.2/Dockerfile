# Set global variables
ARG CHECKM2_VER="1.0.2"
ARG DIAMOND_VER="2.0.4"

# Builder stage
FROM ubuntu:focal AS builder
ARG CHECKM2_VER
ARG DIAMOND_VER

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    less \
    automake \
    cmake \
    zlib1g-dev \
    libzstd-dev \
    g++ \
    python3 \
    python3-pip \
    git \
    hmmer \
    prodigal \
    build-essential && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install CheckM2 and its dependencies
RUN pip install --no-cache-dir \
    numpy==1.19.5 \
    scipy==1.8.0 \
    pandas==1.4.0 \
    setuptools \
    requests \
    packaging \
    tqdm \
    scikit-learn==0.23.2 \
    h5py==2.10.0 \
    lightgbm==3.2.1 \
    protobuf==3.20.0 \
    tensorflow==2.2.0

RUN wget https://github.com/chklovski/CheckM2/archive/refs/tags/${CHECKM2_VER}.tar.gz && \
    tar xzf ${CHECKM2_VER}.tar.gz && \
    cd CheckM2-${CHECKM2_VER} && \
    python3 setup.py install && \
    cd .. && \
    rm -rf ${CHECKM2_VER}.tar.gz CheckM2-${CHECKM2_VER}


# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v${DIAMOND_VER}.tar.gz && \
    tar xzf v${DIAMOND_VER}.tar.gz && \
    cd diamond-${DIAMOND_VER} && \
    mkdir bin && cd bin && \
    cmake .. && \
    make -j4 && \
    make install && \
    rm -rf v${DIAMOND_VER}.tar.gz diamond-${DIAMOND_VER}

# Application stage
FROM ubuntu:focal AS app
ARG CHECKM2_VER
ARG DIAMOND_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CheckM2"
LABEL software.version=${CHECKM2_VER}
LABEL description="Rapid assessment of genome bin quality using machine learning."
LABEL website="https://github.com/chklovski/CheckM2"
LABEL license.url="https://github.com/chklovski/CheckM2/blob/main/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

COPY --from=builder /usr/ /usr/

# Set working directory
RUN mkdir data/
WORKDIR /data

# Test stage (optional and does not persist)
FROM app AS test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/

# Download database and set db in PATH
RUN checkm2 database --download

# Run internal tests
RUN checkm2 testrun

RUN wget -nv --no-check-certificate \
    https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa -O burk_wgs_pos_ctrl.fa && \
    wget -nv --no-check-certificate \
    https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_16S.fa -O burk_16S_neg_ctrl.fa

RUN python3 -m unittest discover -v -s ../tests

# Final image
FROM app

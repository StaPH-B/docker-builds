# Builder Stage
# Credit to https://github.com/HKU-BAL/Clair3/blob/main/Dockerfile for reference code
FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS builder
ARG CLAIR3_VER="2.0.0"
USER root
WORKDIR /opt/bin

# Install base packages for downloading source code.
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install packages needed for Clair3 and for make files.
RUN micromamba install \
    -c conda-forge \
    -c bioconda \
    python=3.11 \
    samtools \
    whatshap \
    parallel \
    zstd \
    xz \
    zlib \
    bzip2 \
    automake \
    make \
    gcc \
    gxx \
    curl \
    pigz \
    binutils \
    boost-cpp \
    -y && \
    micromamba clean -a -f -y

# Set environmental variables for PATH and installation with respect to appropriate micromamba directories.
ENV CONDA_PREFIX=/opt/conda
ENV PATH=${CONDA_PREFIX}/bin:/opt/conda/bin:/opt/bin:${PATH} LC_ALL=C.UTF-8 LANG=C.UTF-8

# Install uv for faster installation, then install relevant pytorch libraries and required packages.
RUN pip install --no-cache-dir uv && \
    uv pip install --python ${CONDA_PREFIX}/bin/python \
      torch torchvision \
      --index-url https://download.pytorch.org/whl/cpu && \
    uv pip install --python ${CONDA_PREFIX}/bin/python \
      numpy \
      h5py \
      hdf5plugin \
      numexpr \
      tqdm \
      cffi \
      torchmetrics

# Get Clair3 Source code and extract
RUN wget -q https://github.com/HKU-BAL/Clair3/archive/refs/tags/v${CLAIR3_VER}.tar.gz && \
    tar -xzf v${CLAIR3_VER}.tar.gz && \
    cp -a Clair3-${CLAIR3_VER}/. /opt/bin/ && \
    rm -rf v${CLAIR3_VER}.tar.gz Clair3-${CLAIR3_VER}

# Use makefile to build Clair3
RUN make PREFIX=${CONDA_PREFIX} PYTHON=${CONDA_PREFIX}/bin/python && \
    cd /opt/bin/preprocess/realign && \
    g++ -std=c++14 -O1 -shared -fPIC -o realigner ssw_cpp.cpp ssw.c realigner.cpp && \
    g++ -std=c++11 -shared -fPIC -o debruijn_graph -O3 debruijn_graph.cpp && \
    rm -rf /opt/bin/samtools-* /opt/bin/longphase-*

# Download required pypy3 tools
RUN wget -q https://downloads.python.org/pypy/pypy3.11-v7.3.20-linux64.tar.bz2 && \
    tar -xjf pypy3.11-v7.3.20-linux64.tar.bz2 && \
    rm pypy3.11-v7.3.20-linux64.tar.bz2 && \
    ln -sf /opt/bin/pypy3.11-v7.3.20-linux64/bin/pypy3 ${CONDA_PREFIX}/bin/pypy3 && \
    ln -sf /opt/bin/pypy3.11-v7.3.20-linux64/bin/pypy3 ${CONDA_PREFIX}/bin/pypy && \
    pypy3 -m ensurepip && \
    pypy3 -m pip install --no-cache-dir mpmath==1.2.1

# Download models for different sequencing approaches
ARG CLAIR3_MODELS_URL=https://www.bio8.cs.hku.hk/clair3/clair3_models_pytorch/
RUN set -eux; \
    mkdir -p /opt/models /tmp/clair3-models; \
    base_url="${CLAIR3_MODELS_URL%/}"; \
    wget -r -np -nH --cut-dirs=2 -R "index.html*" -P /tmp/clair3-models "${base_url}/"; \
    if [ -d /tmp/clair3-models/clair3_models_pytorch ]; then \
        cp -a /tmp/clair3-models/clair3_models_pytorch/. /opt/models/; \
    else \
        cp -a /tmp/clair3-models/. /opt/models/; \
    fi; \
    rm -rf /tmp/clair3-models
    

# App Stage
FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app
ARG CLAIR3_VER="2.0.0"
USER root
WORKDIR /opt/bin

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="CLAIR3"
LABEL software.version="${CLAIR3_VER}"
LABEL description="A deep learning-based germline small variant caller for long-reads."
LABEL website="https://github.com/HKU-BAL/Clair3"
LABEL license="https://github.com/HKU-BAL/Clair3/blob/master/LICENSE.md"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install packages needed for Clair3.
RUN micromamba install \
    -c conda-forge \
    -c bioconda \
    python=3.11 \
    samtools \
    whatshap \
    parallel \
    zstd \
    xz \
    zlib \
    bzip2 \
    pigz \
    boost-cpp \
    -y && \
    micromamba clean -a -f -y

ENV CONDA_PREFIX=/opt/conda
ENV PATH=${CONDA_PREFIX}/bin:/opt/conda/bin:/opt/bin:/clair3:/clair3/models:${PATH} LC_ALL=C.UTF-8 LANG=C.UTF-8

# Copy conda env and built binaries from builder
COPY --from=builder /opt/bin /opt/bin
COPY --from=builder /opt/models /opt/models

# Install uv for faster installation, then install relevant pytorch libraries and required packages.
RUN pip install --no-cache-dir uv && \
    uv pip install --python ${CONDA_PREFIX}/bin/python \
      torch torchvision \
      --index-url https://download.pytorch.org/whl/cpu && \
    uv pip install --python ${CONDA_PREFIX}/bin/python \
      numpy \
      h5py \
      hdf5plugin \
      numexpr \
      tqdm \
      cffi \
      torchmetrics

# Relink required pypy3 tools
RUN ln -sf /opt/bin/pypy3.11-v7.3.20-linux64/bin/pypy3 ${CONDA_PREFIX}/bin/pypy3 && \
    ln -sf /opt/bin/pypy3.11-v7.3.20-linux64/bin/pypy3 ${CONDA_PREFIX}/bin/pypy


# Generate symlinks for /opt and /clair3
RUN ln -s /opt /clair3

RUN mkdir /data
WORKDIR /data


FROM app AS test

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN run_clair3.sh --help && \
    run_clair3.sh --version

# Download ont_quick_test script and run with prespecified arguments
RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/clair3/1.0.9/ont_quick_test.sh && \
    chmod +x ont_quick_test.sh &&\
    ./ont_quick_test.sh

# list models
RUN ls /clair3/models

# list tools installed with micromamba
RUN micromamba list
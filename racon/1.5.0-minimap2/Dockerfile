ARG RACON_VER="1.5.0"
ARG MINIMAP2_VER="2.28"

# Use ubuntu as base image
FROM ubuntu:jammy AS builder

ARG RACON_VER
ARG MINIMAP2_VER

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  perl \
  default-jre \
  gnuplot \
  libgomp1 \
  maven \
  git \
  wget \
  python3 \
  build-essential \
  cmake \
  zlib1g-dev \
  curl \
  bzip2 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install Racon
RUN wget https://github.com/lbcb-sci/racon/archive/refs/tags/${RACON_VER}.tar.gz && \
  tar -xvf ${RACON_VER}.tar.gz && \
  cd racon-${RACON_VER} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make

# Add Racon to PATH
ENV PATH="/racon-${RACON_VER}/build/bin:${PATH}"

# Test Racon
RUN racon_test

# Install Minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner && \
    mv minimap2-${MINIMAP2_VER}_x64-linux /usr/local/minimap2

# Add Minimap2 to PATH
ENV PATH="/usr/local/minimap2:${PATH}"

# Test Minimap2
RUN minimap2 --version

FROM ubuntu:jammy AS app

ARG RACON_VER
ARG MINIMAP2_VER

# Metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Racon + Minimap2"
LABEL racon.version="${RACON_VER}"
LABEL software.version="Racon-${RACON_VER}, Minimap2-${MINIMAP2_VER}"
LABEL racon.version="${RACON_VER}"
LABEL minimap2.version="${MINIMAP2_VER}"
LABEL description="Racon for assembly polishing and Minimap2 for alignment"
LABEL website="https://github.com/lbcb-sci/racon, https://github.com/lh3/minimap2"
LABEL license="https://github.com/lbcb-sci/racon/blob/master/LICENSE, https://github.com/lh3/minimap2/blob/master/LICENSE.txt"
LABEL maintainer="Fraser Combe"
LABEL maintainer.email="fraser.combe@theiagen.com"

# Install Python and essential tools
RUN apt-get update && apt-get install -y \
  procps \
  wget \
  python3 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Copy Racon and Minimap2 binaries
COPY --from=builder /racon-${RACON_VER}/build/bin/* /usr/local/bin/
COPY --from=builder /usr/local/minimap2/* /usr/local/bin/

RUN mkdir /data

WORKDIR /data

# Set locale settings
ENV PATH=${PATH} LC_ALL=C

CMD racon --help

FROM app AS test

# Test Racon and Minimap2
RUN racon --help && racon --version && minimap2 --version

COPY --from=builder /racon-${RACON_VER}/test/data/* /test/

WORKDIR /test

# Minimap2 alignment test
RUN wget -q https://raw.githubusercontent.com/lh3/minimap2/master/test/MT-human.fa && \
    wget -q https://raw.githubusercontent.com/lh3/minimap2/master/test/MT-orang.fa && \
    minimap2 -a MT-human.fa MT-orang.fa > test.sam && \
    head test.sam

# Example polishing workflow
RUN wget -q https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/prokaryotes/bacteroides_fragilis/genome/genome.paf && \
  wget -q https://github.com/nf-core/test-datasets/raw/modules/data/genomics/prokaryotes/bacteroides_fragilis/genome/genome.fna.gz && \
  wget -q https://github.com/nf-core/test-datasets/raw/modules/data/genomics/prokaryotes/bacteroides_fragilis/nanopore/fastq/test.fastq.gz && \
  minimap2 -x map-ont genome.fna.gz test.fastq.gz > test.paf && \
  racon -t 2 test.fastq.gz test.paf genome.fna.gz > test_polished.fasta && \
  head test_polished.fasta

ARG MINIPOLISH_VER=0.2.0
ARG MINIMAP2_VER=2.30
ARG RACON_VER=1.5.0
ARG MINIASM_VER=0.3


FROM ubuntu:jammy AS builder
ARG MINIPOLISH_VER
ARG MINIMAP2_VER
ARG RACON_VER
ARG MINIASM_VER

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
    mv minimap2-${MINIMAP2_VER}_x64-linux /usr/local/bin/minimap2

# miniasm
RUN wget https://github.com/lh3/miniasm/archive/v${MINIASM_VER}.tar.gz && \
  mkdir miniasm && \
  tar -xzvf v${MINIASM_VER}.tar.gz -C miniasm --strip-components 1 && \
  rm v${MINIASM_VER}.tar.gz && \
  cd miniasm && \
  make && \
  mv miniasm /usr/local/bin/.

FROM ubuntu:jammy AS app
ARG MINIPOLISH_VER
ARG RACON_VER

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="minipolish"
LABEL software.version="${MINIPOLISH_VER}"
LABEL description="Racon polishing for GFA graphs produced by miniasm"
LABEL website="https://github.com/rrwick/Minipolish"
LABEL license="https://github.com/rrwick/Minipolish/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  ca-certificates \
  python3-pip && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /racon-${RACON_VER}/build/bin/* /usr/local/bin/
COPY --from=builder /usr/local/bin/* /usr/local/bin/

# install minipolish
RUN wget https://github.com/rrwick/Minipolish/archive/refs/tags/v${MINIPOLISH_VER}.tar.gz && \
  tar -vxf v${MINIPOLISH_VER}.tar.gz && \
  pip install v${MINIPOLISH_VER}.tar.gz && \
  rm v${MINIPOLISH_VER}.tar.gz 
# in theory, this can be tested with python3 -m pytest

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/Minipolish-${MINIPOLISH_VER}:${PATH}" \
  TERM=xterm-256color \
  LC_ALL=C

# set working directory
WORKDIR /data

CMD ["minipolish", "--help"]

FROM app AS test

RUN minipolish --help

# checking dependencies
RUN minimap2 --version && racon --help && miniasm -V

WORKDIR /test

RUN wget https://github.com/rrwick/Unicycler/raw/refs/heads/main/sample_data/long_reads_high_depth.fastq.gz

RUN miniasm_and_minipolish.sh long_reads_high_depth.fastq.gz 4 > test.gfa && head test.gfa
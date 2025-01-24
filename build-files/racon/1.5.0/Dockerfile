ARG RACON_VER="1.5.0"

# Use ubuntu as base image
FROM ubuntu:jammy as builder

ARG RACON_VER

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
  zlib1g-dev && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install racon
RUN wget https://github.com/lbcb-sci/racon/archive/refs/tags/${RACON_VER}.tar.gz && \
  tar -xvf ${RACON_VER}.tar.gz && \
  cd racon-${RACON_VER} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make

ENV PATH="/racon-${RACON_VER}/build/bin:${PATH}"

RUN racon_test

FROM ubuntu:jammy as app

ARG RACON_VER

# metadata
LABEL base.image="ubuntu:jammy"
LABEL version="1"
LABEL dockerfile.version="1"
LABEL software="Racon"
LABEL software.version="${RACON_VER}"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/lbcb-sci/racon"
LABEL license="https://github.com/lbcb-sci/racon/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install python
RUN apt-get update && apt-get install -y \
  procps \
  wget \
  python3 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /racon-${RACON_VER}/build/bin/* /usr/local/bin/

RUN mkdir /data

WORKDIR /data

# set perl locale settings
ENV PATH=${PATH} LC_ALL=C

CMD racon --help

FROM app as test

RUN racon --help && racon --version

COPY --from=builder /racon-${RACON_VER}/test/data/* /test/

WORKDIR /test

RUN wget -q https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/prokaryotes/bacteroides_fragilis/genome/genome.paf && \
  wget -q https://github.com/nf-core/test-datasets/raw/modules/data/genomics/prokaryotes/bacteroides_fragilis/genome/genome.fna.gz && \
  wget -q https://github.com/nf-core/test-datasets/raw/modules/data/genomics/prokaryotes/bacteroides_fragilis/nanopore/fastq/test.fastq.gz && \
  racon -t 2 test.fastq.gz genome.paf genome.fna.gz > test_polished.fasta && \
  head test_polished.fasta

ARG RAVEN_VERSION=1.8.3

## Builder ##
FROM ubuntu:noble AS builder

ARG RAVEN_VERSION

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    clang \
    git \
    gcc \
    zlib1g-dev \
    build-essential \
    cmake \
    libboost-all-dev \
    doxygen \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/*

# prevent avx512f instructions which cause illegal instruction error on older CPUs
ENV CFLAGS="-march=x86-64-v3 -mno-avx512f"
ENV CXXFLAGS="-march=x86-64-v3 -mno-avx512f"

# build raven
RUN wget https://github.com/lbcb-sci/raven/archive/refs/tags/${RAVEN_VERSION}.tar.gz && \
    tar -xvf ${RAVEN_VERSION}.tar.gz && \
    cd raven-${RAVEN_VERSION} && \
    cmake -S ./ -B ./build -DRAVEN_BUILD_EXE=1 -DCMAKE_BUILD_TYPE=Release -Wno-dev && \
    cmake --build build && \
    cmake --install ./build

## App ##
FROM ubuntu:noble AS app

ARG RAVEN_VERSION

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="raven"
LABEL software.version="${RAVEN_VERSION}"
LABEL description="Raven is a de novo genome assembler for long uncorrected reads."
LABEL website="https://github.com/lbcb-sci/raven"
LABEL license="https://github.com/lbcb-sci/raven/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/lib/ /usr/local/lib/
COPY --from=builder /usr/local/include/raven/ /usr/local/include/raven/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

ENV LC_ALL=C

WORKDIR /data

CMD ["raven", "--help"]

## Test ##
FROM app AS test

WORKDIR /test

ARG RAVEN_VERSION

COPY --from=builder /raven-${RAVEN_VERSION}/RavenTest/data/ERA476754.fastq.gz /test/ERA476754.fastq.gz

RUN raven --graphical-fragment-assembly ERA476754.gfa /test/ERA476754.fastq.gz > ERA476754.fasta && \
    test -f ERA476754.gfa && test -f ERA476754.fasta

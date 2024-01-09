# Use ubuntu as base image
FROM ubuntu:jammy as app

ARG RACON_VER="1.5.0"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL version="1"
LABEL dockerfile.version="1"
LABEL software="Racon"
LABEL software.version="${RACON_VER}"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/isovic/racon"
LABEL license="https://github.com/isovic/racon/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install python
RUN apt-get update && apt-get install -y \
    perl \
    default-jre \
    gnuplot \
    libgcc-5-dev \
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
RUN wget https://github.com/isovic/racon/releases/download/${RACON_VER}/racon-v${RACON_VER}.tar.gz && \
  tar -xvf racon-v${RACON_VER}.tar.gz && \
  rm racon-v${RACON_VER}.tar.gz && \
  cd racon-v${RACON_VER} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make && \
  mkdir /data

ENV PATH="/racon-v${RACON_VER}/build/bin:${PATH}"

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

CMD racon --help

FROM app as test

RUN racon --help && racon --version



# base image
FROM ubuntu:focal

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="raven"
LABEL software.version="1.5.1"
LABEL description="Raven is a de novo genome assembler for long uncorrected reads."
LABEL website="https://github.com/lbcb-sci/raven"
LABEL license="https://github.com/lbcb-sci/raven/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# version to build with
ARG RAVEN_VERSION=1.5.1
# otherwise tzdata won't install
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies via apt-get or yum if using a centos or fedora base 
RUN apt-get update && apt-get install -y \
  wget \
  git \
  clang \
  gcc \
  zlib1g-dev \
  build-essential \
  cmake \
  && apt-get autoclean \
  && rm -rf /var/lib/apt/lists/*

# install raven
RUN wget https://github.com/lbcb-sci/raven/archive/refs/tags/${RAVEN_VERSION}.tar.gz && \
  tar -xvf ${RAVEN_VERSION}.tar.gz && \
  rm ${RAVEN_VERSION}.tar.gz && \
  cd raven-${RAVEN_VERSION} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. \
  && make install

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/raven-${RAVEN_VERSION}/:$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

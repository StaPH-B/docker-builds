# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
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
ARG CMAKE_VERSION=3.21.0

# install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y \
 wget \
 git \
 clang \
 zlib1g-dev \
 gcc \
 build-essential \
 libssl-dev \
 libcurl4-openssl-dev

# install cmake because raven needs a version greater than 3.5
RUN wget https://github.com/Kitware/CMake/releases/download/v3.21.0/cmake-${CMAKE_VERSION}.tar.gz && \
    tar -xvf cmake-${CMAKE_VERSION}.tar.gz && \
    rm cmake-${CMAKE_VERSION}.tar.gz && \
    cd cmake-${CMAKE_VERSION} && \
    ./configure && \
    make && \
    make install

# install raven
RUN wget https://github.com/lbcb-sci/raven/archive/refs/tags/${RAVEN_VERSION}.tar.gz && \
  tar -xvf ${RAVEN_VERSION}.tar.gz && \
  rm ${RAVEN_VERSION}.tar.gz && \
  cd raven-1.5.1 && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. \
  && make install

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/raven-1.5.1/:$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

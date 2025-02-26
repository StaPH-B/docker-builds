# base image
FROM ubuntu:focal

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="minipolish"
LABEL software.version="0.1.3"
LABEL description="Racon polishing for GFA graphs produced by miniasm"
LABEL website="https://github.com/rrwick/Minipolish"
LABEL license="https://github.com/rrwick/Minipolish/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
# racon installation was stolen from Curtis Kapsak at https://github.com/StaPH-B/docker-builds/blob/master/racon/1.4.20/Dockerfile
# minimap2 installation was stolen from Curtis Kapsak at https://github.com/StaPH-B/docker-builds/blob/master/minimap2/2.18/Dockerfile

# version to build with
ARG MINIPOLISH_VER=0.1.3
ARG MINIMAP2_VER=2.18
ARG RACON_VER=1.4.20
ARG MINIASM_VER=0.3

# to get around tzdata time zone config
ENV DEBIAN_FRONTEND noninteractive

# install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  perl \
  default-jre \
  gnuplot \
  libgomp1 \
  git \
  gcc \
  python3 \
  build-essential \
  cmake \
  bzip2 \
  curl \
  python3-setuptools \
  zlib1g-dev && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install racon
RUN wget https://github.com/lbcb-sci/racon/releases/download/${RACON_VER}/racon-v${RACON_VER}.tar.gz && \
  tar -xvf racon-v${RACON_VER}.tar.gz && \
  rm racon-v${RACON_VER}.tar.gz && \
  cd racon-v${RACON_VER} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make && \
  mkdir /data

# install minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf -

# miniasm
RUN wget https://github.com/lh3/miniasm/archive/v${MINIASM_VER}.tar.gz && \
  mkdir miniasm && \
  tar -xzvf v${MINIASM_VER}.tar.gz -C miniasm --strip-components 1 && \
  rm v${MINIASM_VER}.tar.gz && \
  cd miniasm && \
  make

# install minipolish
RUN wget https://github.com/rrwick/Minipolish/archive/refs/tags/v${MINIPOLISH_VER}.tar.gz && \
  tar -xvf v${MINIPOLISH_VER}.tar.gz && \
  rm v${MINIPOLISH_VER}.tar.gz && \
  cd Minipolish-${MINIPOLISH_VER} && \
  python3 setup.py install
# in theory, this can be tested with python3 -m pytest

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/racon-v${RACON_VER}/build/bin:/minimap2-${MINIMAP2_VER}_x64-linux:/Minipolish-${MINIPOLISH_VER}/:/miniasm:${PATH}" \
  LC_ALL=C

# set working directory
WORKDIR /data

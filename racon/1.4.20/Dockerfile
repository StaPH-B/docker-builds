# Use ubuntu as base image
FROM ubuntu:focal

# for easy upgrade later. ARG variables only persist during build time
ARG RACON_VER="1.4.20"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Racon"
LABEL software.version="1.4.20"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/lbcb-sci/racon/"
LABEL license="https://github.com/lbcb-sci/racon/blob/master/LICENSE"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# to get around tzdata time zone config
ENV DEBIAN_FRONTEND noninteractive

# install depedencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 perl \
 default-jre \
 gnuplot \
 gcc \
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
RUN wget https://github.com/lbcb-sci/racon/releases/download/${RACON_VER}/racon-v${RACON_VER}.tar.gz&& \
  tar -xvf racon-v${RACON_VER}.tar.gz && \
  rm racon-v${RACON_VER}.tar.gz && \
  cd racon-v${RACON_VER} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make && \
  mkdir /data

# set PATH and locale settings for singularity compatibility
ENV PATH="/racon-v${RACON_VER}/build/bin:${PATH}"\
    LC_ALL=C

WORKDIR /data

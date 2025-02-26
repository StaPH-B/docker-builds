# Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL dockerfile.version="1"
LABEL software="Racon"
LABEL software.version="1.4.3"
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
RUN wget https://github.com/isovic/racon/releases/download/1.4.3/racon-v1.4.3.tar.gz && \
  tar -xvf racon-v1.4.3.tar.gz && \
  rm racon-v1.4.3.tar.gz && \
  cd racon-v1.4.3 && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make && \
  mkdir /data

ENV PATH="/racon-v1.4.3/build/bin:${PATH}"

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

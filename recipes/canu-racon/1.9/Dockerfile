# Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Canu, Minimap2, Racon"
LABEL software.version="1.9.0; 2.17; 1.4.3"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/marbl/canu; https://github.com/lh3/minimap2; https://github.com/isovic/racon"
LABEL license="See program repositories"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

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
   apt-get clean

# install canu
RUN wget https://github.com/marbl/canu/releases/download/v1.9/canu-1.9.Linux-amd64.tar.xz && \
  tar -xvf canu-1.9.Linux-amd64.tar.xz && \
  rm canu-1.9.Linux-amd64.tar.xz

# install minimap2
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
  tar -xvf minimap2-2.17_x64-linux.tar.bz2 && \
  rm minimap2-2.17_x64-linux.tar.bz2

# install racon
RUN wget https://github.com/isovic/racon/releases/download/1.4.3/racon-v1.4.3.tar.gz && \
  tar -xvf racon-v1.4.3.tar.gz && \
  rm racon-v1.4.3.tar.gz && \
  cd racon-v1.4.3 && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make

ENV PATH="/canu-1.9/Linux-amd64/bin:/racon-v1.4.3/build/bin:/minimap2-2.17_x64-linux:${PATH}"

RUN mkdir /data
WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

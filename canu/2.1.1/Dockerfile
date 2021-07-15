# Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL software="Canu"
LABEL software.version="2.1.1"
LABEL dockerfile.version="1"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/marbl/canu"
LABEL license="https://github.com/marbl/canu/blob/master/README.license.GPL"
LABEL maintainer="Thomas A. Christensen II"
LABEL maintainer.email="25492070+MillironX@users.noreply.github.com"

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
   apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
   mkdir /data

# install canu
RUN wget https://github.com/marbl/canu/releases/download/v2.1.1/canu-2.1.1.Linux-amd64.tar.xz && \
  tar -xvf canu-2.1.1.Linux-amd64.tar.xz && \
  rm canu-2.1.1.Linux-amd64.tar.xz

ENV PATH="/canu-2.1.1/bin:${PATH}"

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

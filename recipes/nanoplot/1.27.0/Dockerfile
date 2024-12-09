FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="2"
LABEL software="NanoPlot"
LABEL software.version="1.27.0"
LABEL description="Plotting suite for Oxford Nanopore sequencing data and alignments"
LABEL website="https://github.com/wdecoster/NanoPlot"
LABEL license="https://github.com/wdecoster/NanoPlot/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y zlib1g-dev \
  bzip2 \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  libncurses5-dev \
  libssl-dev \
  python3 \
  python3-pip \
  python3-setuptools \
  locales && \
  locale-gen en_US.UTF-8 && \
  apt-get autoclean

# for singularity compatibility
ENV LC_ALL=C

# update pip, install NanoPlot 1.27.0
RUN python3 -m pip install -U pip && \
  pip3 install psutil requests NanoPlot==1.27.0 && \
  mkdir /data

WORKDIR /data

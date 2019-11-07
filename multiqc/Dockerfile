# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="MultiQC"
LABEL software.version="1.7"
LABEL description="Aggregate bioinformatics results across many samples into a single report."
LABEL website="https://github.com/ewels/MultiQC"
LABEL license="https://github.com/ewels/MultiQC/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install dependencies
RUN apt-get update && apt-get install -y \
  wget \
  python3 \
  python3-dev \
  python3-pip \
  locales && \
  locale-gen en_US.UTF-8 && \
  apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install multiqc
RUN wget https://github.com/ewels/MultiQC/archive/v1.7.tar.gz && \
    tar -xvf v1.7.tar.gz && \
    cd MultiQC-1.7/ && \
    pip3 install multiqc

ENV LC_ALL='C.UTF-8' LANG='C.UTF-8'

RUN mkdir /data
WORKDIR /data

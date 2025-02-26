# Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="wtdbg2"
LABEL software.version="2.5"
LABEL description="A fuzzy Bruijn graph approach to long noisy reads assembly "
LABEL website="https://github.com/ruanjue/wtdbg2"
LABEL license="https://github.com/ruanjue/wtdbg2/blob/master/LICENSE.txt"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install dependancies
RUN apt-get update && apt-get -y install \
  build-essential\
  wget \
  perl \
  libperl4-corelibs-perl && \
  apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install wtdbg2
RUN wget https://github.com/ruanjue/wtdbg2/releases/download/v2.5/wtdbg-2.5_x64_linux.tgz && \
  tar -xvf wtdbg-2.5_x64_linux.tgz && \
  rm wtdbg-2.5_x64_linux.tgz

ENV PATH="/wtdbg-2.5_x64_linux:${PATH}"

RUN mkdir /data
WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

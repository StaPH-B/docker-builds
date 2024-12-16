# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="rasusa"
LABEL software.version="0.2.0"
LABEL description="Randomly subsample sequencing reads to a specified coverage."
LABEL website="https://github.com/mbhall88/rasusa"
LABEL license="https://github.com/mbhall88/rasusa/blob/master/LICENSE"
LABEL maintainer="Jake Garfin"
LABEL maintainer.email="jake.garfin@state.mn.us"

# install dependencies
RUN apt-get update && apt-get -y install \
  wget && apt-get clean

# install rasusa
RUN mkdir rasusa && \
  cd rasusa && \
  wget https://github.com/mbhall88/rasusa/releases/download/0.2.0/rasusa-0.2.0-x86_64-unknown-linux-musl.tar.gz && \
  tar -xvf rasusa-0.2.0-x86_64-unknown-linux-musl.tar.gz && \
  rm -rf rasusa-0.2.0-x86_64-unknown-linux-musl.tar.gz && \
  mkdir /data

ENV PATH="${PATH}:/rasusa"

# set perl locale settings
ENV LC_ALL=C

WORKDIR /data

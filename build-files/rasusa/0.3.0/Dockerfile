FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="rasusa"
LABEL software.version="0.3.0"
LABEL description="Randomly subsample sequencing reads to a specified coverage."
LABEL website="https://github.com/mbhall88/rasusa"
LABEL license="https://github.com/mbhall88/rasusa/blob/master/LICENSE"
LABEL maintainer1="Jake Garfin"
LABEL maintainer1.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install wget and cleanup apt garbage
RUN apt-get update && apt-get -y install \
 wget && \
 apt-get clean && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# install rasusa
ENV rasusaVer=0.3.0
RUN mkdir rasusa && \
  cd rasusa && \
  wget https://github.com/mbhall88/rasusa/releases/download/${rasusaVer}/rasusa-${rasusaVer}-x86_64-unknown-linux-musl.tar.gz && \
  tar -xvf rasusa-${rasusaVer}-x86_64-unknown-linux-musl.tar.gz && \
  rm -rf rasusa-${rasusaVer}-x86_64-unknown-linux-musl.tar.gz && \
  mkdir /data

# set PATH and perl locale settings
ENV PATH="${PATH}:/rasusa" \
 LC_ALL=C

WORKDIR /data

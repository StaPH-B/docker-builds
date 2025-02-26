FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Filtlong"
LABEL software.version="0.2.0"
LABEL description="Filter long reads by quality and length. Can use ILMN reads as reference."
LABEL website="https://github.com/rrwick/Filtlong"
LABEL license="https://github.com/rrwick/Filtlong/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y \
  wget \
  g++ \
  zlib1g-dev \
  make \
  python3 \
  pigz

RUN wget https://github.com/rrwick/Filtlong/archive/v0.2.0.tar.gz && \
  tar -xzf v0.2.0.tar.gz && \
  rm -r v0.2.0.tar.gz && \
  cd Filtlong-0.2.0/ && \
  make -j && \
  mkdir /data

# required for singularity compatibility
ENV LC_ALL=C

ENV PATH="${PATH}:/Filtlong-0.2.0/bin"
WORKDIR /data

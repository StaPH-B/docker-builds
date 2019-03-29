FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SPAdes"
LABEL software.version="3.12.0"
LABEL description="de novo DBG genome assembler"
LABEL website="http://cab.spbu.ru/files/release3.12.0/manual.html"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y python \
  wget

RUN wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz && \
  tar -xzf SPAdes-3.12.0-Linux.tar.gz && \
  rm -r SPAdes-3.12.0-Linux.tar.gz && \
  mkdir /data

ENV PATH="${PATH}:/SPAdes-3.12.0-Linux/bin"
WORKDIR /data

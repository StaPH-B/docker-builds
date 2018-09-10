FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SPAdes"
LABEL software.version="3.12"
LABEL description="do novo DBG genome assembler"
LABEL website="http://cab.spbu.ru/files/release3.12.0/manual.html"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

RUN apt-get update && apt-get install -y python\
  wget

RUN wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz && tar -xzf SPAdes-3.12.0-Linux.tar.gz && rm -r SPAdes-3.12.0-Linux.tar.gz
ENV PATH="/SPAdes-3.12.0-Linux/bin:${PATH}"

WORKDIR /data/

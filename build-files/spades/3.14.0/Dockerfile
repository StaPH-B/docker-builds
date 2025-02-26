FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="SPAdes"
LABEL software.version="3.14.0"
LABEL description="de novo DBG genome assembler"
LABEL website="http://cab.spbu.ru/files/release3.14.0/manual.html"
LABEL license="https://github.com/ablab/spades/blob/spades_3.14.0/assembler/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y python \
  wget

RUN wget http://cab.spbu.ru/files/release3.14.0/SPAdes-3.14.0-Linux.tar.gz && \
  tar -xzf SPAdes-3.14.0-Linux.tar.gz && \
  rm -r SPAdes-3.14.0-Linux.tar.gz && \
  mkdir /data

# because why not?
ENV LC_ALL=C

ENV PATH="${PATH}:/SPAdes-3.14.0-Linux/bin"
WORKDIR /data

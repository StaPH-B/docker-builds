FROM ubuntu:xenial

# to make it easier to upgrade for new versions
ENV SPAdesVer=3.14.1

LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="SPAdes"
LABEL software.version="3.14.1"
LABEL description="de novo DBG genome assembler"
LABEL website="https://github.com/ablab/spades"
LABEL license="https://github.com/ablab/spades/blob/spades_3.14.1/assembler/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y python \
 wget && \
 rm -rf /var/lib/apt/lists/* 

RUN wget http://cab.spbu.ru/files/release${SPAdesVer}/SPAdes-${SPAdesVer}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPAdesVer}-Linux.tar.gz && \
  rm -r SPAdes-${SPAdesVer}-Linux.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C \
    PATH="${PATH}:/SPAdes-${SPAdesVer}-Linux/bin"

WORKDIR /data

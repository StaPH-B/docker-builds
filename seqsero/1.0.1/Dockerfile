# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SeqSero"
LABEL software.version="1.0.1"
LABEL description="Pipeline for Salmonella serotype determination from reads or assemblies"
LABEL website="https://github.com/denglab/SeqSero"
LABEL license="https://github.com/denglab/SeqSero/blob/master/LICENSE"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# install dependencies using conda
RUN apt-get update && apt-get -y install python-biopython \
  wget \
  bwa \
  samtools \
  sra-toolkit && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/denglab/SeqSero/archive/v1.0.1.tar.gz && \
  tar -xzf v1.0.1.tar.gz && rm -rf v1.0.1.tar.gz && mkdir /data

ENV PATH="$PATH:/SeqSero-1.0.1"
WORKDIR /data

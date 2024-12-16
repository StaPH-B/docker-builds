FROM ubuntu:xenial

# ARGs are variables that are only available during docker image build, not available
# when running the container
ARG SEQTK_VER=1.3

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="seqtk"
LABEL software.version="1.3"
LABEL description="Toolkit for processing sequences in FASTA/Q formats"
LABEL website="https://github.com/lh3/seqtk"
LABEL license="https://github.com/lh3/seqtk/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies, take out the apt garbage
RUN apt-get update && apt-get install -y make \
 wget \
 gcc \
 zlib1g-dev && \
 apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install seqtk, make /data 
RUN wget https://github.com/lh3/seqtk/archive/v${SEQTK_VER}.tar.gz && \
 tar -xzvf v${SEQTK_VER}.tar.gz && \
 rm v${SEQTK_VER}.tar.gz && \
 cd seqtk-${SEQTK_VER} && \
 make && \
 mkdir /data

# set PATH and working directory
ENV PATH="${PATH}:/seqtk-${SEQTK_VER}"
WORKDIR /data

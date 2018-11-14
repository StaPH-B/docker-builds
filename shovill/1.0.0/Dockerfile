FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Shovill"
LABEL software.version="1.0.0"
LABEL description="faster than SPAdes de novo DBG genome assembler"
LABEL website="https://github.com/tseemann/shovill"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

RUN apt-get update && apt-get install -y python \
  wget \
  pigz \
  zlib1g-dev \
  make \
  gcc \
  g++ \
  libpthread-stubs0-dev 

# get spades, unpack, remove tarball
RUN mkdir spades &&\
  cd spades &&\ 
  wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz &&\
  tar -xzf SPAdes-3.12.0-Linux.tar.gz &&\
  rm -r SPAdes-3.12.0-Linux.tar.gz

# get Seqtk
RUN mkdir seqtk &&\ 
  cd seqtk &&\
  wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz &&\
  tar -zxf v1.3.tar.gz &&\
  rm v1.3.tar.gz &&\
  cd seqtk-1.3/ &&\
  make &&\
  make install

# get Mash and the associated RefSeqSketches k=21 s=1000 database
RUN wget https://github.com/marbl/Mash/releases/download/v2.1/mash-Linux64-v2.1.tar && \
  tar -xvf mash-Linux64-v2.1.tar && \
  rm -rf mash-Linux64-v2.1.tar && \
  # make database directory, store mash db there
  mkdir /db && \
  cd /db && \
  wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
  gunzip RefSeqSketchesDefaults.msh.gz

# install lighter 1.1.1
RUN wget https://github.com/mourisl/Lighter/archive/v1.1.1.tar.gz &&\
  tar -zxf v1.1.1.tar.gz &&\
  rm -rf v1.1.1.tar.gz &&\
  cd Lighter-1.1.1 &&\
  make

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

# set $PATH
ENV PATH="${PATH}:\
/spades/SPAdes-3.12.0-Linux/bin:\
/mash-Linux64-v2.1:\
/Lighter-1.1.1"

FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="Flye"
LABEL software.version="2.5"
LABEL description="Fast and accurate de novo assembler for single molecule sequencing reads"
LABEL website="https://github.com/fenderglass/Flye"
LABEL lisence="https://github.com/fenderglass/Flye/blob/flye/LICENSE"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y make \
  gcc \
  g++ \
  python \
  zlib1g-dev \
  wget

RUN wget https://github.com/fenderglass/Flye/archive/2.5.tar.gz &&\
  tar -xvf 2.5.tar.gz &&\
  rm 2.5.tar.gz &&\
  cd Flye-2.5 &&\
  python setup.py build &&\
  python setup.py install &&\
  mkdir /data

WORKDIR /data


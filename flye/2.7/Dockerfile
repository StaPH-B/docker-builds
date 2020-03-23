FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Flye"
LABEL software.version="2.7"
LABEL description="Fast and accurate de novo assembler for single molecule sequencing reads"
LABEL website="https://github.com/fenderglass/Flye"
LABEL license="https://github.com/fenderglass/Flye/blob/flye/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="Abigail.Shockey@slh.wisc.edu"

RUN apt-get update && apt-get install -y make \
  gcc \
  g++ \
  python \
  python-pip \
  zlib1g-dev \
  wget

RUN pip install setuptools

RUN wget https://github.com/fenderglass/Flye/archive/2.7.tar.gz &&\
  tar -xvf 2.7.tar.gz &&\
  rm 2.7.tar.gz &&\
  cd Flye-2.7 &&\
  python setup.py build &&\
  python setup.py install &&\
  mkdir /data

WORKDIR /data

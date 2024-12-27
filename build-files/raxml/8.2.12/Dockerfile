# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="Standard RAxML and RAxML Next Generation"
LABEL software.version="8.2.12;0.9.0"
LABEL description="A tool for phylogenetic analysis and post-analysis of large phylogenies"
LABEL website="https://github.com/stamatak/standard-RAxML;https://github.com/amkozlov/raxml-ng"
LABEL license="https://github.com/stamatak/standard-RAxML/blob/master/gpl-3.0.txt;https://github.com/amkozlov/raxml-ng/blob/master/LICENSE.txt"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update && \
    apt-get -y install build-essential\
    wget \
    zip \
    unzip && \
    apt-get clean

# install raxml HPC, SSE3 and AVC, both sequential and pthreads versions
RUN wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz && \
  tar -xvf v8.2.12.tar.gz && \
  rm -rf v8.2.12.tar.gz && \
  cd standard-RAxML-8.2.12/ && \
  make -f Makefile.gcc && \
  rm *.o && \
  make -f Makefile.SSE3.gcc && \
  rm *.o && \
  make -f Makefile.AVX.gcc && \
  rm *.o && \
  make -f Makefile.PTHREADS.gcc && \
  rm *.o && \
  make -f Makefile.SSE3.PTHREADS.gcc && \
  rm *.o && \
  make -f Makefile.AVX.PTHREADS.gcc && \
  rm *.o

# install raxml-ng
RUN wget https://github.com/amkozlov/raxml-ng/releases/download/0.9.0/raxml-ng_v0.9.0_linux_x86_64.zip && \
  unzip raxml-ng_v0.9.0_linux_x86_64.zip && \
  mkdir raxml_ng && \
  mv raxml-ng raxml_ng/ && \
  rm -rf raxml-ng_v0.9.0_linux_x86_64.zip

# add programs to path
ENV PATH="${PATH}:/standard-RAxML-8.2.12:/raxml_ng"

WORKDIR /data

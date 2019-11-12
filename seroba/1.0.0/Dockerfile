# base image
FROM debian:testing

# metadata
LABEL base.image="debian:testing"
LABEL version="1"
LABEL software="SeroBA"
LABEL software.version="1.0.0"
LABEL description="k-mer based Pipeline to serotype from Illumina NGS reads"
LABEL website="https://github.com/sanger-pathogens/seroba"
LABEL license="https://github.com/sanger-pathogens/seroba/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install Debian dependencies
RUN apt-get update && apt-get -y upgrade && apt-get -y install git \
  wget \
  unzip \
  zlib1g-dev \
  libbz2-dev \
  liblzma-dev \
  python3.6 \
  python3-pip \
  libpython3-dev \
  python3-setuptools \
  python-minimal && \
  apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the latest release from github and install dependencies
RUN wget https://github.com/sanger-pathogens/seroba/archive/v1.0.0.tar.gz && \
  tar -xvf v1.0.0.tar.gz && \
  cd seroba-1.0.0 && \
  sed -i 's/pymummer/\"pymummer==0.10.3\"/g' /seroba-1.0.0/install_dependencies.sh && \
  /seroba-1.0.0/install_dependencies.sh

# set path
ENV PATH="/seroba-1.0.0:/seroba-1.0.0/build:/seroba-1.0.0/build/MUMmer3.23:/seroba-1.0.0/build/bowtie2-2.3.1-legacy:/seroba-1.0.0/build/cdhit-4.6.8:${PATH}"

# install seroba and create database (/seroba-1.0.0/database/)
RUN cd /seroba-1.0.0 && \
  python3 setup.py install && \
  seroba createDBs database/ 71

RUN mkdir /data
WORKDIR /data

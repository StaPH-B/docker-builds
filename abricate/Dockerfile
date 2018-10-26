FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Prokka"
LABEL software.version="1.13"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# install dependencies
RUN apt-get update && apt-get install -y \
  emboss \
  bioperl \
  ncbi-blast+ \
  gzip \ 
  unzip \ 
  libjson-perl \
  libtext-csv-perl \
  libfile-slurp-perl \
  liblwp-protocol-https-perl \
  libwww-perl \
  git \
  wget && apt-get clean

RUN wget https://github.com/tseemann/abricate/archive/v0.8.7.tar.gz && tar -zxvf v0.8.7.tar.gz && rm -rf v0.8.7.tar.gz
ENV PATH="/abricate-0.8.7/bin:$PATH"

RUN abricate --check
RUN abricate --setupdb && mkdir /data

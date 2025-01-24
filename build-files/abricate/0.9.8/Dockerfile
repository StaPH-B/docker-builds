FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="Abricate"
LABEL software.version="0.9.8"
LABEL description="Mass screening of contigs for AMR or virulence genes"
LABEL website="https://github.com/tseemann/abricate"
LABEL license="https://github.com/tseemann/abricate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

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
  libpath-tiny-perl \
  git \
  wget && apt-get clean

# get any2fasta
RUN cd /usr/local/bin && \
  wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
  chmod +x any2fasta

RUN wget https://github.com/tseemann/abricate/archive/v0.9.8.tar.gz && \
    tar -zxvf v0.9.8.tar.gz && \
    rm -rf v0.9.8.tar.gz

ENV PATH="/abricate-0.9.8/bin:$PATH"

# check dependencies, setup db's, test, make working directory '/data'
RUN abricate --check && \
    abricate --setupdb && \
    abricate /abricate-0.9.8/test/assembly.fa && \
    mkdir /data

# set perl locale settings for singularity compatibility
ENV LC_ALL=C

WORKDIR /data

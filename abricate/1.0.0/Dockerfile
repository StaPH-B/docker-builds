FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Abricate"
LABEL software.version="1.0.0"
LABEL description="Mass screening of contigs for AMR or virulence genes"
LABEL website="https://github.com/tseemann/abricate"
LABEL license="https://github.com/tseemann/abricate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get install -y \
  emboss \
  bioperl \
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

# ncbi-blast+ 2.9.0
# apt version of blast is very old (2.2.31)
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.9.0/ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 rm ncbi-blast-2.9.0+-x64-linux.tar.gz

# get any2fasta
RUN cd /usr/local/bin && \
  wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
  chmod +x any2fasta

# abricate 1.0.0
RUN wget https://github.com/tseemann/abricate/archive/v1.0.0.tar.gz && \
    tar -zxvf v1.0.0.tar.gz && \
    rm -rf v1.0.0.tar.gz

# set $PATH
# set perl locale settings for singularity compatibility
ENV PATH="/abricate-1.0.0/bin:\
/ncbi-blast-2.9.0+/bin:\
$PATH"\
    LC_ALL=C

# check dependencies, setup db's, make working directory /data
# tests now run as part of travis, instead of in dockerfile
RUN abricate --check && \
    abricate --setupdb && \
    mkdir /data

WORKDIR /data

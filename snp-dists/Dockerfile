FROM ubuntu:xenial
 
# metadata
LABEL base.image="ubuntu:snp-dists"
LABEL version="1"
LABEL software="snp-dists"
LABEL software.version="1.0"
LABEL description="Convert a FASTA alignment to SNP distance matrix"
LABEL website="https://github.com/tseemann/snp-dists"

MAINTAINER Kevin Libuit <kevin.libuit@dgs.virginia.gov>

RUN apt-get update && apt-get install -y python \
  git make libz-dev gcc

RUN cd / &&\
  git clone https://github.com/tseemann/snp-dists.git && \
  cd /snp-dists &&\
  make &&\
  make PREFIX=/usr/local install 


FROM ubuntu:xenial
 
# metadata
LABEL base.image="ubuntu:snp-dists"
LABEL version="1"
LABEL software="snp-dists"
LABEL software.version="1.0"
LABEL description="Convert a FASTA alignment to SNP distance matrix"
LABEL website="https://github.com/tseemann/snp-dists"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@dgs.virginia.gov"

RUN apt-get update && apt-get install -y python \
  wget make libz-dev gcc

RUN cd / &&\
  wget https://github.com/tseemann/snp-dists/archive/v0.6.2.tar.gz && \
  tar -xzf v0.6.2.tar.gz &&\
  rm v0.6.2.tar.gz &&\
  cd /snp-dists-0.6.2 &&\
  make &&\
  make PREFIX=/usr/local install 

RUN mkdir /data
WORKDIR /data

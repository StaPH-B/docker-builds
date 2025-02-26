FROM ubuntu:xenial

# For easy upgrade later. ARG variables only persist during build time
ARG SNP_DISTS_VER=0.8.2
 
# metadata
LABEL base.image="ubuntu:snp-dists"
LABEL dockerfile.version="1"
LABEL software="snp-dists"
LABEL software.version="0.8.2"
LABEL description="Convert a FASTA alignment to SNP distance matrix"
LABEL website="https://github.com/tseemann/snp-dists"
LABEL license="https://github.com/tseemann/snp-dists/blob/master/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@theiagen.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# so apt doesn't ask questions
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y python \
 wget \
 make \
 libz-dev \
 gcc && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install snp-dists; make /data
RUN wget https://github.com/tseemann/snp-dists/archive/v${SNP_DISTS_VER}.tar.gz && \
 tar -xzf v${SNP_DISTS_VER}.tar.gz && \
 rm v${SNP_DISTS_VER}.tar.gz && \
 cd /snp-dists-${SNP_DISTS_VER} && \
 make && \
 make PREFIX=/usr/local install && \
 mkdir /data 

WORKDIR /data

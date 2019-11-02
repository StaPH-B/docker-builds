FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1.0.0"
LABEL software="Snippy"
LABEL software.version="4.4.5"
LABEL description="Rapid haploid variant calling and core genome alignment"
LABEL website="https://github.com/tseemann/snippy"
LABEL license="https://github.com/tseemann/snippy/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
 wget \ 
 gcc \ 
 libstdc++6 \ 
 libbz2-1.0 \
 emboss \
 cpanminus \

 bzip2 \
 gzip \
 wget \
 perl \
 less \
 libdatetime-perl \
 libxml-simple-perl \
 libdigest-md5-perl \
 default-jre \
 bioperl \
 hmmer \
 zlib1g-dev \
 python \
 liblzma-dev \
 libbz2-dev \
 xz-utils \ 
 curl \
 g++ \
 make && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install bedtools 2.29.0 since >=2.27.0 is required for barrnap and the apt-get package is 2.25.0
# dependencies required for bedtools: zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
  tar -zxf bedtools-2.29.0.tar.gz && \
  rm bedtools-2.29.0.tar.gz && \
  cd bedtools2 && \
  make

# add bedtools to PATH for barrnap test
ENV PATH="$PATH:/bedtools2/bin"

# install bwa
RUN mkdir bwa &&\
  cd /bwa &&\
  wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2 &&\
  tar -xjf bwa-0.7.17.tar.bz2 &&\
  rm bwa-0.7.17.tar.bz2 &&\
  cd bwa-0.7.17 &&\
  make

# get Seqtk
RUN mkdir seqtk &&\ 
  cd seqtk &&\
  wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz &&\
  tar -zxf v1.3.tar.gz &&\
  rm v1.3.tar.gz &&\
  cd seqtk-1.3/ &&\
  make &&\
  make install

RUN wget https://github.com/tseemann/prokka/archive/v1.14.0.tar.gz && \
    tar -xzf v1.14.0.tar.gz && \
    rm -rf v1.14.0.tar.gz && \
    mkdir /data

ENV PATH="/prokka-1.14.0/bin:\
/barrnap-0.9/bin:\
$PATH"

# set perl locale settings so barrnap works in singularity image
ENV LC_ALL=C

RUN prokka --setupdb && prokka --listdb
WORKDIR /data

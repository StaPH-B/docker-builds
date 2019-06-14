# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="2"
LABEL software="Prokka"
LABEL software.version="1.13.3"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# install dependencies using conda
RUN apt-get update && apt-get -y install \
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
 bedtools \
 make && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

#### bedtools installed via apt-get. It's v2.25 (Sept 2015) but it should still work.
#### It's too much of a pain to install and compile from source. Ran into problems with gcc/g++

# install bedtools, required for barrnap
#RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.27.1/bedtools-2.27.1.tar.gz &&\
#    tar -xzf bedtools-2.27.1.tar.gz &&\
#    rm bedtools-2.27.1.tar.gz &&\
#    cd bedtools2/ &&\
#    make

# install barrnap
RUN wget https://github.com/tseemann/barrnap/archive/0.9.tar.gz &&\
    tar -zxf 0.9.tar.gz &&\
    rm 0.9.tar.gz &&\
    cd barrnap-0.9 &&\
    make test

RUN wget https://github.com/tseemann/prokka/archive/v1.13.4.tar.gz && \
    tar -xzf v1.13.4.tar.gz && \
    rm -rf v1.13.4.tar.gz && \
    mkdir /data

ENV PATH="$PATH:/prokka-1.13.4/bin:\
/barrnap-0.9/bin"

# set perl locale settings so barrnap works in singularity image
ENV LC_ALL=C

RUN prokka --setupdb && prokka --listdb
WORKDIR /data

FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="Prokka"
LABEL software.version="1.14.0"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
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

# install barrnap
RUN wget https://github.com/tseemann/barrnap/archive/0.9.tar.gz &&\
    tar -zxf 0.9.tar.gz &&\
    rm 0.9.tar.gz &&\
    cd barrnap-0.9 &&\
    make test

RUN wget https://github.com/tseemann/prokka/archive/v1.14.0.tar.gz && \
    tar -xzf v1.14.0.tar.gz && \
    rm -rf v1.14.0.tar.gz && \
    mkdir /data

ENV PATH="$PATH:/prokka-1.14.0/bin:\
/barrnap-0.9/bin"

# set perl locale settings so barrnap works in singularity image
ENV LC_ALL=C

RUN prokka --setupdb && prokka --listdb
WORKDIR /data

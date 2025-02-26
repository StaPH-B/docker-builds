FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Abricate"
# the "s" is for serotypefinder
LABEL software.version="0.8.13s"
LABEL description="Mass screening of contigs for AMR or virulence genes"
LABEL website="https://github.com/tseemann/abricate"
LABEL license="https://github.com/tseemann/abricate/blob/master/LICENSE"

# Maintainer
MAINTAINER Erin Young <eriny@utah.gov>
# although, most of this was written by Curtis, I just added a few lines

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

RUN wget https://github.com/tseemann/abricate/archive/v0.8.13.tar.gz &&\
    tar -zxvf v0.8.13.tar.gz &&\
    rm -rf v0.8.13.tar.gz
ENV PATH="/abricate-0.8.13/bin:$PATH"

# downloading the serotypefinder database
RUN wget https://bitbucket.org/genomicepidemiology/serotypefinder_db/get/df7e85438b94.zip &&\
    unzip df7e85438b94.zip &&\
    mkdir -p /abricate-0.8.13/db/serotypefinder &&\
    cat genomicepidemiology-serotypefinder_db-df7e85438b94/O_type.fsa genomicepidemiology-serotypefinder_db-df7e85438b94/H_type.fsa > /abricate-0.8.13/db/serotypefinder/sequences

RUN abricate --check &&\
    abricate --setupdb &&\
    mkdir /data

# set perl locale settings
ENV LC_ALL=C

WORKDIR /data

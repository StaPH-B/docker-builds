# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="staramr"
LABEL software.version="0.5.1"
LABEL description="staramr scans bacterial genome contigs for AMR genes and plasmids"
LABEL website="https://github.com/phac-nml/staramr"
LABEL license="https://github.com/phac-nml/staramr"

# Maintainer
MAINTAINER Rachael St. Jacques <rachael.stjacques@dgs.virginia.gov>

# install dependencies using conda
RUN apt-get update && apt-get install -y \
 python3.6\
 python3-pip\
 ncbi-blast+\
 git

#get staramr
RUN pip3 install staramr

RUN mkdir /data

WORKDIR /data

# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="staramr"
LABEL software.version="0.5.1"
LABEL description="staramr scans bacterial genome contigs for AMR genes and plasmids"
LABEL website="https://github.com/phac-nml/staramr"
LABEL license="https://github.com/phac-nml/staramr/blob/master/LICENSE"
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"

# install dependencies
RUN apt-get update && apt-get install -y \
 python3.6\
 python3-pip\
 ncbi-blast+\
 git

#get staramr
RUN pip3 install staramr==0.5.1

RUN mkdir /data

WORKDIR /data

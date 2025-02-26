# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL container.version="1"
LABEL software="centroid"
LABEL software.version="v0.1"
LABEL description=" a tool for determining the ideal reference genome given a set of fasta files"
LABEL website="https://github.com/stjacqrm/centroid"
LABEL license="https://github.com/stjacqrm/centroid"
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
    unzip \
    tar \
    python3.7 \
    python3-pip \
    gzip \
    wget && \
    apt-get clean

#install numpy
RUN python3 -m pip install numpy

# install mash
RUN wget --no-check-certificate https://github.com/marbl/Mash/releases/download/v2.2/mash-Linux64-v2.2.tar && \
    tar -xvf mash-Linux64-v2.2.tar && \
    rm -rf mash-Linux64-v2.2.tar && \
    mkdir /data

#install the software
RUN wget --no-check-certificate https://github.com/stjacqrm/centroid/archive/72fba4a8cd1e289fd48cd1b3581d1710813eae3b.zip && \
    unzip 72fba4a8cd1e289fd48cd1b3581d1710813eae3b.zip && \
    rm 72fba4a8cd1e289fd48cd1b3581d1710813eae3b.zip && \
    mv centroid-72fba4a8cd1e289fd48cd1b3581d1710813eae3b centroid && \
    chmod 777 -R centroid

#set paths
ENV PATH="/mash-Linux64-v2.2:\
/centroid:\
$PATH"\
    LC_ALL=C

WORKDIR /data

# make db dir. Store db there. Better to have db's added in the last layers
RUN mkdir /db && \
    cd /db && \
    wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
    gunzip RefSeqSketchesDefaults.msh.gz

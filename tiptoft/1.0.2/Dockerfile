FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="tiptoft"
LABEL software.version="1.0.2"
LABEL description="Predict plasmids from uncorrected long read data"
LABEL website="https://github.com/andrewjpage/tiptoft"
LABEL license="https://github.com/andrewjpage/tiptoft/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y git \
 python3 \
 python3-setuptools \
 python3-biopython \
 python3-pip \
 curl && \
 apt-get clean && \
 rm -rf /var/lib/apt/lists/* 

# install cython
RUN pip3 install cython==0.29.14 tiptoft==1.0.2 && \
 mkdir /data

# This will store a database in /tiptoftDB marked with the date it was downloaded 
# (docker image was built on this day)
# Tiptoft will use it's included DB by default, you must specify this DB with:
# -d /tiptoftDB/tiptoftDB-downloaded-on-$(date +%Y-%m-%d) if you want to use it.
RUN mkdir /tiptoftDB && cd /tiptoftDB && \
 tiptoft_database_downloader tiptoftDB-downloaded-on-$(date +%Y-%m-%d)

WORKDIR /data
ENV LC_ALL=C

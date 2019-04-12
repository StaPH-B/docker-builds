FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="SalmID"
LABEL software.version="0.1.23"
LABEL description="Rapid confirmation of Salmonella spp. and subspp. from sequence data"
LABEL website="https://github.com/hcdenbakker/SalmID"
LABEL lisence="https://github.com/hcdenbakker/SalmID/blob/master/LICENSE"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y \
 python-setuptools \
 python3 \
 python3-pip \
 curl \
 build-essential \
 file \
 git \
 python3-venv

# install poetry, needed to make python wheel
RUN pip3 install poetry

RUN git clone https://github.com/hcdenbakker/SalmID.git --branch 0.1.23 --single-branch &&\
 cd SalmID &&\
 poetry build -vvv &&\
 pip3 install dist/salmid*.whl &&\
 mkdir /data

WORKDIR /data

### Example command to run SalmID (broken into two lines for readability)
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/salmid:0.1.23 /bin/bash -c \
#  'SalmID.py -i SRR498373.cleaned.fastq.gz >/data/salmid-SRR498373.results.tsv'

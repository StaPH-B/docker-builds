# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Mash"
LABEL software.version="2.0.0"
LABEL description="Fast genome and metagenome distance estimation using MinHash"
LABEL website="https://mash.readthedocs.io/en/latest/index.html"
LABEL license="https://github.com/marbl/Mash/blob/master/LICENSE.txt"

MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# install dependencies
RUN apt-get update && apt-get -y install wget && apt-get clean && apt-get autoclean

RUN wget https://github.com/marbl/Mash/releases/download/v2.0/mash-Linux64-v2.0.tar && tar -xvf mash-Linux64-v2.0.tar
ENV PATH="/mash-Linux64-v2.0:${PATH}"

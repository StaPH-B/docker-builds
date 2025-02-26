FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="BBTools"
LABEL software.version="38.76"
LABEL description="A set of tools labeled as \"Bestus Bioinformaticus\""
LABEL website="https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/"
LABEL license="https://jgi.doe.gov/disclaimer/"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"

RUN apt-get update && apt-get install -y openjdk-8-jre-headless\
 wget

RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_38.76.tar.gz &&\
  tar -xzf BBMap_38.76.tar.gz &&\
  rm BBMap_38.76.tar.gz

ENV PATH="${PATH}:/bbmap"
WORKDIR /data

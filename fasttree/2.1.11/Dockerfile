# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="Fasttree"
LABEL software.version="2.1.11"
LABEL description="Infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences"
LABEL website="http://www.microbesonline.org/fasttree"
LABEL license="http://www.microbesonline.org/fasttree/"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update && \
    apt-get -y install build-essential\
    wget && \
    apt-get clean

# install fasttree
RUN wget http://www.microbesonline.org/fasttree/FastTree && \
  chmod +x FastTree && \
  mkdir fasttree && \
  mv FastTree fasttree/

# add to path
ENV PATH="${PATH}:/fasttree"

RUN mkdir /data
WORKDIR /data

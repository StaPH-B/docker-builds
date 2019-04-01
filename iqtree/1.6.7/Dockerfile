#use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="IQ-Tree"
LABEL software.version="1.6.7"
LABEL description="Efficient software for phylogenomic inference"
LABEL website="http://www.iqtree.org/"
LABEL license="https://github.com/Cibiv/IQ-TREE/blob/master/LICENSE"

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>

#install dependencies
RUN apt-get update && apt-get install -y \
 wget

RUN wget https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.7/iqtree-1.6.7-Linux.tar.gz
RUN tar -xzvf iqtree-1.6.7-Linux.tar.gz
ENV PATH="/iqtree-1.6.7-Linux/bin/:${PATH}"
RUN rm iqtree-1.6.7-Linux.tar.gz

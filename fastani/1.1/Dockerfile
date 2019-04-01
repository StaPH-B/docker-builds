FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="FastANI"
LABEL software.version="1.1"
LABEL description="Fast alignment-free computation of whole-genome Average Nucleotide Identity"
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL license="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"

# Maintainer
MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>

# install dependencies
RUN apt-get update && apt-get install -y autoconf \
	libgsl-dev \
	libboost1.58-dev \
	zlib1g-dev \
	g++ \
	make \
	wget
                     

RUN wget https://github.com/ParBLiSS/FastANI/archive/v1.1.tar.gz &&\
	tar -xzf v1.1.tar.gz &&\
	rm v1.1.tar.gz &&\
	cd FastANI-1.1 &&\
	./bootstrap.sh &&\
	./configure &&\
	make

ENV PATH="${PATH}:/FastANI-1.1"

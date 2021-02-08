# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="tiptoft"
LABEL software.version="1.0.0"
LABEL description="Predict plasmids from uncorrected long read data"
LABEL website="https://github.com/andrewjpage/tiptoft"
LABEL license="https://github.com/andrewjpage/tiptoft/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update && apt-get install -y git \
python3 \
python3-setuptools \
python3-biopython \
python3-pip

# install cython
RUN pip3 install "cython==0.29.14"

# install tiptoft
RUN pip3 install "tiptoft==1.0.0"

# Note: Use default database included with tiptoft or build your own (building the plasmidfinder db from scratch throws an error 
# because the fsa files have changed repos)

RUN mkdir /data
WORKDIR /data

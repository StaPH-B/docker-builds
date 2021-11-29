FROM ubuntu:xenial

# ARG variables only persist during build time. Adding for easy upgrade later
ARG FLYE_VER="2.9"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Flye"
LABEL software.version="2.9"
LABEL description="Fast and accurate de novo assembler for single molecule sequencing reads"
LABEL website="https://github.com/fenderglass/Flye"
LABEL license="https://github.com/fenderglass/Flye/blob/flye/LICENSE"
LABEL maintainer1="Abigail Shockey"
LABEL maintainer1.email="Abigail.Shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

RUN apt-get update && apt-get install -y make \
 gcc \
 g++ \
 python \
 python-pip \
 python-setuptools \
 zlib1g-dev \
 wget && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install flye and make /data
RUN wget https://github.com/fenderglass/Flye/archive/${FLYE_VER}.tar.gz && \
 tar -xvf ${FLYE_VER}.tar.gz && \
 rm ${FLYE_VER}.tar.gz && \
 cd Flye-${FLYE_VER} && \
 python setup.py build && \
 python setup.py install && \
 mkdir /data

WORKDIR /data

# just in case for singularity compatibility
ENV LC_ALL=C

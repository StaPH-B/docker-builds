# hmmer
# http://hmmer.org/
# v3.3

# base image: Ubuntu
FROM ubuntu:xenial

# File Author / Maintainer
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="hmmer"
LABEL software.version="3.3"
LABEL description="This software provides HMMer for hmmsearch etc.!"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="Joachim Johansen"
LABEL maintainer.email="joacjohansen@gmail.com"


ENV HMMERVERSION="3.3"


RUN apt-get update --fix-missing \
    && apt-get install -y wget make gcc \
    && wget http://eddylab.org/software/hmmer/hmmer-${HMMERVERSION}.tar.gz \
    && tar -xzvf hmmer-${HMMERVERSION}.tar.gz \
    && rm -f hmmer-${HMMERVERSION}.tar.gz \
    && cd hmmer-${HMMERVERSION}/ \
    && ./configure \
    && make \
    && make install \
    && apt-get remove -y wget make gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir data

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/hmmer-${HMMERVERSION}/src:$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data 

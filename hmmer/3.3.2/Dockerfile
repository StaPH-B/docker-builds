# base image: Ubuntu
FROM ubuntu:jammy as app

# File Author / Maintainer
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="hmmer"
LABEL software.version="3.3.2"
LABEL description="This software provides HMMer for hmmsearch etc.!"
LABEL website="http://hmmer.org/"
LABEL license="http://eddylab.org/software/hmmer/Userguide.pdf"
LABEL maintainer="Neranjan Perera"
LABEL maintainer.email="neranjan007@gmail.com"


ARG HMMERVERSION="3.3.2"


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
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir data

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="$PATH:/hmmer-${HMMERVERSION}/src" \
 LC_ALL=C

# set working directory
WORKDIR /data 

# default command is to print help options
CMD [ "hmmscan", "-h" ]

# test layer
FROM app as test

RUN apt-get update && \
    apt-get install make gcc perl python3 -y 
 

# print version and run help flag
RUN hmmscan -h && hmmbuild -h

WORKDIR /hmmer-${HMMERVERSION}

# compile and run a test suite
RUN make check
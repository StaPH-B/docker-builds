# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="Mugsy"
LABEL software.version="1r2.3"
LABEL description="Multiple whole genome aligner"
LABEL website="http://mugsy.sourceforge.net"
LABEL license="Archived in https://sourceforge.net/projects/mugsy/files/mugsy_x86-64-v1r2.3.tgz"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update && apt-get install -y wget \
  build-essential \
  perl \
  perl-doc

# install mugsy
RUN wget https://sourceforge.net/projects/mugsy/files/mugsy_x86-64-v1r2.3.tgz && \
  tar -xvf mugsy_x86-64-v1r2.3.tgz && \
  rm mugsy_x86-64-v1r2.3.tgz

# install perl dependency
RUN perl -MCPAN -e install Pod::Usage

# add path to mugsyenv.sh
RUN cd mugsy_x86-64-v1r2.3/ && \
  bash -c "sed -i 's/\.\/mugsy_x86-64-v1r2.3/\/mugsy_x86-64-v1r2.3/g' mugsyenv.sh"

RUN mkdir /data
WORKDIR /data

# export paths
ENV MUGSY_INSTALL="/mugsy_x86-64-v1r2.3"
ENV PATH="/mugsy_x86-64-v1r2.3:/mugsy_x86-64-v1r2.3/mapping:${PATH}"
ENV PERL5LIB="/mugsy_x86-64-v1r2.3/perllibs"

# singularity compatibility 
ENV LC_ALL=C

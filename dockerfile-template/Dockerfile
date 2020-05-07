# base image
FROM ubuntu:xenial

# metadata - optional, but highly recommended
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="SoftwareName"
LABEL software.version="1.0.0"
LABEL description="This software does X, Y, AND Z!"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="FirstName LastName"
LABEL maintainer.email="my.email@email.com"

# install dependencies via apt-get or yum if using a centos or fedora base 
RUN apt-get update && apt-get install -y \
 wget \
 perl

# install and/or setup more things
# Example: ncbi-blast+ 2.9.0
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.9.0/ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 rm ncbi-blast-2.9.0+-x64-linux.tar.gz

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/ncbi-blast-2.9.0+/bin:$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

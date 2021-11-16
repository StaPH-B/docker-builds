# Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL software="datasets-sars-cov-2"
LABEL software.version="v0.4"
LABEL dockerfile.version="1"
LABEL description="Benchmark datasets for WGS analysis of SARS-CoV-2."
LABEL website="https://github.com/CDCgov/datasets-sars-cov-2"
LABEL license="https://github.com/CDCgov/datasets-sars-cov-2/blob/master/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"

# version to build with
ARG CANU_VERSION=2.2

# install python
RUN apt-get update && apt-get install -y \
 wget\
 build-essential\
 libxml2\
 libmagic-dev\
 libhdf5-dev\
 git\
 openjdk-8-jdk\
 software-properties-common\
 lsb-release\
 apt-transport-https\
 ca-certificates\
 doxygen\
 uuid-runtime


# install latest cmake
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null && \
 apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main" && \
 apt-get update && apt-get install -y cmake

# install newer gcc g++
RUN add-apt-repository ppa:ubuntu-toolchain-r/test &&\
 apt-get update && apt-get install -y \
 gcc-9 g++-9 && \
 update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 --slave /usr/bin/gcov gcov /usr/bin/gcov-9

# get NCBI SRA Tools
RUN mkdir /ncbi && cd /ncbi && \
 git clone https://github.com/ncbi/sra-tools.git && \
 git clone https://github.com/ncbi/ngs.git && \
 git clone https://github.com/ncbi/ncbi-vdb.git

RUN cd /ncbi/ncbi-vdb && ./configure && \
 make && \
 make install

RUN cd /ncbi/ngs && ./configure && \
 make -C ngs-sdk && \
 make -C ngs-sdk install && \
 make -C ngs-java && \
 make -C ngs-java install && \
 make -C ngs-python

RUN cd /ncbi/sra-tools && ./configure && \
 make && \
 make install

# install edirect
RUN mkdir /edirect && \
    perl -MNet::FTP -e '$ftp = new Net::FTP("ftp.ncbi.nlm.nih.gov", Passive => 1);$ftp->login; $ftp->binary;$ftp->get("/entrez/entrezdirect/edirect.tar.gz");' && \
    gunzip -c edirect.tar.gz | tar xf - && \
    rm edirect.tar.gz

# vdb-config workaround: https://github.com/ncbi/sra-tools/issues/291
RUN mkdir /home/user/ /home/user/.ncbi/ && printf '/LIBS/GUID = "%s"\n' `uuidgen` > /home/user/.ncbi/user-settings.mkfg

# get datasets-sars-cov-2
RUN cd /home/user/ && git clone --depth 1 --branch v0.4 https://github.com/CDCgov/datasets-sars-cov-2.git

ENV HOME /home/user/

ENV PATH=$PATH:/edirect:/usr/local/ncbi/sra-tools/bin:/home/user/datasets-sars-cov-2/scripts

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

FROM ubuntu:bionic

# for easy upgrade later. ARG variables only persist during image build time
ARG kleborateVer="2.0.4"
ARG blastVer="2.9.0"
ARG mashVer="2.1"
ARG kaptiveVer="0.7.3"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Kleborate"
LABEL software.version="2.0.4"
LABEL description="tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC)"
LABEL website="https://github.com/katholt/Kleborate"
LABEL license="https://github.com/katholt/Kleborate/blob/master/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="kapsakcj@gmail.com"

# install prerequisites. Cleanup apt garbage
RUN apt-get update && apt-get install -y  \
 python3 \
 python3-pip \
 python3-setuptools \
 wget \
 bzip2 \
 locales && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# to avoid encoding issues during kleborate setup.py install step
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# mash
RUN wget https://github.com/marbl/Mash/releases/download/v${mashVer}/mash-Linux64-v${mashVer}.tar && \
 tar -xvf mash-Linux64-v${mashVer}.tar && \
 rm -rf mash-Linux64-v${mashVer}.tar && \
 mkdir /data

# ncbi-blast+
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
 rm ncbi-blast-${blastVer}+-x64-linux.tar.gz

# kaptive
RUN wget https://github.com/katholt/Kaptive/archive/refs/tags/v${kaptiveVer}.tar.gz && \
 tar -xzf v${kaptiveVer}.tar.gz && \
 rm -f v${kaptiveVer}.tar.gz 

# set PATH
ENV PATH="/mash-Linux64-v${mashVer}:\
/ncbi-blast-${blastVer}+/bin/:\
${PATH}"

# kleborate
# move kaptive dir inside kleborate (as per author instructions)
RUN python3 -m pip install biopython && \ 
 wget https://github.com/katholt/Kleborate/archive/refs/tags/v${kleborateVer}.tar.gz && \
 tar -xzf v${kleborateVer}.tar.gz && \
 rm -f v${kleborateVer}.tar.gz && \
 mv -v Kaptive-${kaptiveVer}/* /Kleborate-${kleborateVer}/kaptive/ && \
 rm -rf Kaptive-${kaptiveVer} && \
 cd /Kleborate-${kleborateVer} && \
 python3 setup.py install

# set working directory
WORKDIR /data

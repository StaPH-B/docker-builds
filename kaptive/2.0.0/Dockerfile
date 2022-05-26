FROM ubuntu:focal

ARG KAPTIVE_VER="2.0.0"
ARG DEBIAN_FRONTEND=noninteractive

ARG blastVer="2.3.0"
ARG kaptiveVer="2.0.0"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Kaptive"
LABEL software.version=$KAPTIVE_VER
LABEL description="Report information about surface polysaccharide loci for Klebsiella pneumoniae species complex and Acinetobacter baumannii genome assemblies"
LABEL website="https://github.com/katholt/Kaptive"
LABEL license="https://github.com/katholt/Kaptive/blob/master/LICENSE"
LABEL maintainer="Tamas Stirling"
LABEL maintainer.email="stirling.tamas@gmail.com"

RUN apt-get update && apt-get install -y \
  locales \
  python3 \
  python3-pip \
  python3-setuptools \
  software-properties-common \
  wget \
  --no-install-recommends && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# set locale
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# ncbi-blast+
RUN wget "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz" && \
  tar zxvpf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
  rm ncbi-blast-${blastVer}+-x64-linux.tar.gz
 
# kaptive
RUN wget https://github.com/katholt/Kaptive/archive/refs/tags/v${KAPTIVE_VER}.tar.gz && \
  tar -xzf v${kaptiveVer}.tar.gz && \
  rm -f v${kaptiveVer}.tar.gz && \
  mv /Kaptive-${kaptiveVer} /kaptive
 
RUN pip3 install biopython

ENV PATH="/ncbi-blast-${blastVer}+/bin:${PATH}"
ENV PATH="/kaptive:${PATH}"

WORKDIR /data


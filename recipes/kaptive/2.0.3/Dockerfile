FROM ubuntu:focal as app

ARG KAPTIVE_VER="2.0.3"
ARG blastVer="2.3.0"

ARG DEBIAN_FRONTEND=noninteractive

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
RUN wget "https://github.com/katholt/Kaptive/archive/refs/tags/v${KAPTIVE_VER}.tar.gz" && \
  tar -xzf v${KAPTIVE_VER}.tar.gz && \
  rm -f v${KAPTIVE_VER}.tar.gz && \
  mv /Kaptive-${KAPTIVE_VER} /kaptive
 
RUN pip3 install biopython

ENV PATH="/ncbi-blast-${blastVer}+/bin:${PATH}"
ENV PATH="/kaptive:${PATH}"

WORKDIR /data

# test layer
FROM app as test

# test with A. baumannii
RUN wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/486/705/GCA_016486705.1_PDT000751301.1/GCA_016486705.1_PDT000751301.1_genomic.fna.gz" && \
  gunzip GCA_016486705.1_PDT000751301.1_genomic.fna.gz
# k locus
RUN kaptive.py -a GCA_016486705.1_PDT000751301.1_genomic.fna -k /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk
# o locus
RUN kaptive.py -a GCA_016486705.1_PDT000751301.1_genomic.fna -k /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk

# test with K. pneumoniae
RUN wget "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/022/268/055/GCA_022268055.1_PDT000434809.1/GCA_022268055.1_PDT000434809.1_genomic.fna.gz" && \
  gunzip GCA_022268055.1_PDT000434809.1_genomic.fna.gz
# k locus
RUN kaptive.py -a GCA_022268055.1_PDT000434809.1_genomic.fna -k /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk
# o locus
RUN kaptive.py -a GCA_022268055.1_PDT000434809.1_genomic.fna -k /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk

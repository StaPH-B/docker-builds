FROM ubuntu:18.04

LABEL base.image="ubuntu:18.04"
LABEL container.version="1.1-SC2"
LABEL sc2="Modified from the staphb/ivar:1.1 image to include tools for SARS-CoV-2 (SC2) analysis"
LABEL software="iVar"
LABEL software.version="1.1-PR"
LABEL comments="Clone of ivar v1.1 pre-release most recent commit as of 05/09/2020"
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL website="https://github.com/gkarthik/ivar"
LABEL license="https://github.com/gkarthik/ivar/blob/master/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@dgs.virginia.gov"

RUN apt-get update
RUN apt-get install -y build-essential autoconf zlib1g-dev python3 wget libbz2-dev liblzma-dev libncurses-dev git bedtools python3-pip vim nano
# Artic ncov2019 (most recent commit as of 03/24/2020)
RUN git clone -n https://github.com/artic-network/artic-ncov2019.git &&\
    cd artic-ncov2019 &&\
    git checkout d50a5f6a3265fb45a5d0c8949dfd037fd869f8f9 
# Seqtk
RUN mkdir seqtk &&\
    cd seqtk &&\
    wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz && \
    tar -zxf v1.3.tar.gz && \
    rm v1.3.tar.gz && \
    cd seqtk-1.3/ && \
    make && \
    make install
# Minimap2
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
    tar -xvf minimap2-2.17_x64-linux.tar.bz2 && \
    rm minimap2-2.17_x64-linux.tar.bz2
# HTSlib
RUN cd root/ &&\
    wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 &&\
    tar xvf htslib-1.9.tar.bz2 &&\
    cd htslib-1.9/ &&\
    ./configure &&\
    make &&\
    make install &&\
    cd ../ &&\
    rm htslib-1.9.tar.bz2
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
# SAMtools
RUN cd root &&\
    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 &&\
    tar xvf samtools-1.9.tar.bz2 &&\
    cd samtools-1.9/ &&\
    ./configure &&\
    make &&\
    make install &&\
    cd ../ &&\
    rm samtools-1.9.tar.bz2
# iVar v1.1-PR (most recent commit as of 03/19/2020)
RUN cd root/ &&\
    git clone -n https://github.com/andersen-lab/ivar.git &&\
    cd ivar/ &&\
    git checkout 1610e0efee46459528a65769692936e1e35a17f3 &&\
    ./autogen.sh &&\
    ./configure &&\
    make &&\
    make install
# bwa
RUN mkdir bwa &&\
    cd bwa &&\
    wget https://github.com/lh3/bwa/archive/v0.7.17.tar.gz &&\
    tar xvf v0.7.17.tar.gz &&\
    rm v0.7.17.tar.gz &&\ 
    cd bwa-0.7.17/ &&\
    make 

ENV PATH="/bwa/bwa-0.7.17:/minimap2-2.17_x64-linux:${PATH}"
# Snakemake
RUN pip3 install pandas snakemake

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

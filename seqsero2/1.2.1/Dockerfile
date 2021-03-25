FROM ubuntu:bionic

# for easy upgrade later. ARG variables only persist during build time
ARG SEQSERO2_VER="1.2.1"

# Metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="SeqSero2"
LABEL software.version="1.2.1"
LABEL description="Salmonella serotyping from genome sequencing data"
LABEL website="https://github.com/denglab/SeqSero2"
LABEL license="https://github.com/denglab/SeqSero2/blob/master/LICENSE"
LABEL maintainer1="Jake Garfin"
LABEL maintainer1.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
LABEL maintainer3="Kelsey Florek"
LABEL maintainer3.email="kelsey.florek@slh.wisc.edu"

# python = 2.7.17
# python3 = 3.6.9
# biopython = 1.73
# bedtools = 2.26.0 
# sra-toolkit = 2.8.2
# bwa = 0.7.17
# ncbi-blast+ = 2.6.0
RUN apt-get update && apt-get install -y \
 python3 \
 python3-pip \
 bwa \
 ncbi-blast+ \
 sra-toolkit \
 bedtools \
 wget \
 zlib1g-dev \
 libbz2-dev \
 liblzma-dev \
 build-essential \
 libncurses5-dev && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install samtools 1.9
RUN wget 'https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2' && \
 tar -xvf samtools-1.9.tar.bz2 && \
 rm samtools-1.9.tar.bz2 && \
 cd samtools-1.9 && \
 make

# Install salmID 0.122
RUN wget https://github.com/hcdenbakker/SalmID/archive/0.122.tar.gz && \
 tar -xzf 0.122.tar.gz && \
 rm -rf 0.122.tar.gz

# Install SPAdes 3.9.0
RUN wget https://github.com/ablab/spades/releases/download/v3.9.0/SPAdes-3.9.0-Linux.tar.gz && \
 tar -xzf SPAdes-3.9.0-Linux.tar.gz && \
 rm -rf SPAdes-3.9.0-Linux.tar.gz

# Install SeqSero2; make /data
RUN wget https://github.com/denglab/SeqSero2/archive/v${SEQSERO2_VER}.tar.gz && \
 tar -xzf v${SEQSERO2_VER}.tar.gz && \
 rm -rf v${SEQSERO2_VER}.tar.gz && \
 cd /SeqSero2-${SEQSERO2_VER}/ && \
 python3 -m pip install . && \
 mkdir /data

# PATH edited to include /SeqSero2-1.1.0/bin in previous python3 command
ENV PATH="${PATH}:/SPAdes-3.9.0-Linux/bin:/SalmID-0.122:/samtools-1.9" \
    LC_ALL=C

WORKDIR /data

FROM ubuntu:xenial

ARG FASTQC_VER="0.11.9"

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="FASTQC"
LABEL software.version="0.11.9"
LABEL description="A quality control analysis tool for high throughput sequencing data"
LABEL website="https://www.bioinformatics.babraham.ac.uk/projects/fastqc/"
LABEL license="https://github.com/s-andrews/FastQC/blob/master/LICENSE.txt"
LABEL maintainer1="Abigail Shockey"
LABEL maintainer1.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y \
 unzip \
 wget \
 perl \
 default-jre && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install fastqc
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQC_VER}.zip && \
    unzip fastqc_v${FASTQC_VER}.zip && \
    rm fastqc_v${FASTQC_VER}.zip && \
    chmod +x FastQC/fastqc && \
    mkdir /data

# set PATH and working directory
ENV PATH="${PATH}:/FastQC/"
WORKDIR /data

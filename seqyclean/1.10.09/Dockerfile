FROM ubuntu:xenial

# metadata (there are a few other labels you can add, these are optional but preferred!)
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="seqyclean"
LABEL software.version="1.10.09"
LABEL description="Trims and cleans fastq files"
LABEL website="https://github.com/ibest/seqyclean"
LABEL license="https://github.com/ibest/seqyclean/blob/master/LICENSE"

MAINTAINER Erin Young <eriny@utah.gov>

# getting dependencies
RUN apt-get update && \
    apt-get -y install zlib1g-dev wget make gcc g++

RUN wget https://github.com/ibest/seqyclean/archive/1.10.09.tar.gz && \
    tar -xzf 1.10.09.tar.gz && \
    rm -r 1.10.09.tar.gz && \
    cd /seqyclean-1.10.09 && \
    make && mkdir /data

RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/seqyclean/Adapters_plus_PhiX_174.fasta

# Set working directory
WORKDIR /data

# add to path
ENV PATH="/seqyclean-1.10.09/bin:${PATH}"

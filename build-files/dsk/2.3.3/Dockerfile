ARG DSK_VER="2.3.3"

FROM ubuntu:jammy as app
ARG DSK_VER
ARG GATBCORE_VER="1.4.2"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="DSK"
LABEL software.version=${DSK_VER}
LABEL description="DSK is a k-mer counter for reads or genomes."
LABEL website="https://github.com/GATB/dsk"
LABEL documentation="https://gatb.inria.fr/software/dsk/"
LABEL license="https://github.com/GATB/dsk/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends\
    build-essential \
    cmake \
    wget \
    libz-dev \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Download DSK source code
RUN wget -q https://github.com/GATB/dsk/releases/download/v${DSK_VER}/dsk-v${DSK_VER}-bin-Linux.tar.gz && \
    tar -vxf dsk-v${DSK_VER}-bin-Linux.tar.gz && \
    rm -rf dsk-v${DSK_VER}-bin-Linux.tar.gz && \
    wget -q https://github.com/GATB/gatb-core/releases/download/v${GATBCORE_VER}/gatb-core-${GATBCORE_VER}-bin-Linux.tar.gz && \
    tar -xvf gatb-core-${GATBCORE_VER}-bin-Linux.tar.gz && \
    rm -rf gatb-core-${GATBCORE_VER}-bin-Linux.tar.gz && \
    cp /gatb-core-${GATBCORE_VER}-bin-Linux/bin/*  /dsk-v${DSK_VER}-bin-Linux/bin && \
    rm -rf /gatb-core-${GATBCORE_VER}-bin-Linux && \
    mkdir /data

# Add DSK executable to PATH
ENV PATH="/dsk-v${DSK_VER}-bin-Linux/bin:$PATH"

CMD dsk

WORKDIR /data

FROM app as test
ARG DSK_VER

RUN dsk

# Run DSK's internal tests
WORKDIR /dsk-v${DSK_VER}-bin-Linux/test

RUN bash ./simple_test.sh

# Run DSK on sample file

WORKDIR /test

RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    dsk  -file SRR13957123_1.fastq.gz -kmer-size 31 && \
    ls && \
    gatb-h5dump -y -d dsk/solid/0 SRR13957123_1.fastq.h5 && \
    gatb-h5dump -y -d histogram/histogram SRR13957123_1.fastq.h5 && \
    dsk2ascii -file SRR13957123_1.fastq.h5 -out output.txt && \
    head output.txt
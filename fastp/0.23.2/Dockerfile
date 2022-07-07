FROM ubuntu:bionic as app

ARG FASTP_VER="0.23.2"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Fastp"
LABEL software.version=$FASTP_VER
LABEL description="An ultra-fast all-in-one FASTQ preprocessor"
LABEL website="https://github.com/OpenGene/fastp"
LABEL license="https://github.com/OpenGene/fastp/blob/master/LICENSE"
LABEL maintainer="Idowu Olawoye"
LABEL maintainer.email="olawoyei0303@run.edu.ng"

RUN apt-get update && apt-get install -y \
 wget \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN mkdir fastp && \
 cd fastp && \ 
 wget http://opengene.org/fastp/fastp.${FASTP_VER} && \
 mv fastp.${FASTP_VER} fastp && \
 chmod a+x ./fastp && \
 mkdir /data
 
ENV PATH="$PATH:/fastp/"

WORKDIR /data

# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app as test

RUN fastp --help

# downloading sars-cov-2 fastq test files
RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz
RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz

# running fastp on the files
RUN fastp \
        -i SRR13957123_1.fastq.gz \
        -I SRR13957123_2.fastq.gz \
        -o SRR13957123_PE1.fastq.gz \
        -O SRR13957123_PE2.fastq.gz \
        -h SRR13957123_fastp.html \
        -j SRR13957123_fastp.json

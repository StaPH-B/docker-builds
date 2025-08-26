ARG TRIMMOMATIC_VER="0.40"

#use ubuntu as base image
FROM ubuntu:jammy AS app
ARG TRIMMOMATIC_VER

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Trimmomatic"
LABEL software.version=$TRIMMOMATIC_VER
LABEL description="Trimmomatic: A flexible read trimming tool for Illumina NGS data"
LABEL website="https://https://github.com/usadellab/Trimmomatic"
LABEL documentation="http://www.usadellab.org/cms/?page=trimmomatic"
LABEL license="https://github.com/usadellab/Trimmomatic/blob/main/distSrc/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
LABEL maintainer3="Sarah Nadeau"
LABEL maintainer3.email="sarah.nadeau@bsse.ethz.ch"

WORKDIR /usr/local/bin

#install openjdk-11 jre
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jre \
    wget \
    unzip \
  && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/usadellab/Trimmomatic/releases/download/v${TRIMMOMATIC_VER}/Trimmomatic-${TRIMMOMATIC_VER}.zip &&\
  unzip Trimmomatic-${TRIMMOMATIC_VER}.zip &&\
  rm -rf Trimmomatic-${TRIMMOMATIC_VER}.zip &&\
  chmod +x trimmomatic-${TRIMMOMATIC_VER}.jar &&\
  echo "#!/bin/bash" >> trimmomatic &&\
  echo "exec java -jar /usr/local/bin/trimmomatic-${TRIMMOMATIC_VER}.jar """"$""@"""" " >> trimmomatic &&\
  chmod +x trimmomatic

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

CMD ["trimmomatic"]

FROM app AS test
ARG TRIMMOMATIC_VER

RUN trimmomatic || trimmomatic -version

# Run test script
RUN wget https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz && \
  wget https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz && \
  ADAPTERS="/usr/local/bin/adapters/TruSeq3-PE.fa" && \
  trimmomatic \
  PE \
  -phred33 \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  R1.paired.fq R1.unpaired.fq \
  R2.paired.fq R2.unpaired.fq \
  ILLUMINACLIP:$ADAPTERS:2:20:10:8:TRUE \
  SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50 && \
  ls && \
  ls R1.paired.fq R1.unpaired.fq R2.paired.fq R2.unpaired.fq

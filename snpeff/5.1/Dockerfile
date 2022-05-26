FROM ubuntu:focal as app

ARG SNPEFF_VER="5.1"

# Metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SnpEff & SnpSift"
LABEL software.version="5.1"
LABEL description.SnpEff="Genetic variant annotation and effect prediction toolbox."
LABEL description.SnpSift="Used after SnpEff annotation to filter and manipulate annotated files."
LABEL website="https://pcingola.github.io/SnpEff"
LABEL license="https://github.com/pcingola/SnpEff/blob/master/LICENSE.md"
LABEL maintainer="Tom Iverson"
LABEL maintainer.email="tiverson@utah.gov"

# Install open using apt 
RUN apt-get update && apt-get install -y software-properties-common &&\
  apt-get update && apt-get install -y \
  openjdk-11-jre \
  wget \
  unzip

# Use wget to install SnpEff and SnpSift
RUN wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip && \
  unzip snpEff_latest_core.zip && \
  rm -rf snpEff_latest_core.zip && \
  chmod +x /snpEff/snpEff.jar && \
  echo "#!/bin/bash" >> /snpEff/snpeff && \
  chmod +x /snpEff/SnpSift.jar && \
  echo "#!/bin/bash" >> /snpEff/snpsift && \
  echo "exec java -jar /snpEff/snpEff.jar """"$""@"""" " >> /snpEff/snpeff && \
  chmod +x /snpEff/snpeff && \
  echo "exec java -jar /snpEff/SnpSift.jar """"$""@"""" " >> /snpEff/snpsift && \
  chmod +x /snpEff/snpsift

# Set environment variable $PATH
ENV PATH="${PATH}:/snpEff" 

# Set working directory
RUN mkdir /data
WORKDIR /data

# Run test of annotation
FROM app as test

COPY test_snpeff_snpsift.sh .
RUN bash test_snpeff_snpsift.sh 

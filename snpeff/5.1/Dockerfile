ARG SNPEFF_VER="5.1d"
ARG SNPSIFT_VER="5.1"

FROM ubuntu:focal as app

ARG SNPEFF_VER
ARG SNPSIFT_VER

# Metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SnpEff & SnpSift"
LABEL snpeff.software.version=$SNPEFF_VER
LABEL snpsift.software.version=$SNPSIFT_VER
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
  ant \
  maven \
  wget \
  unzip

# Use wget to get the source code for SnpEff and SnpSift from GitHub.
RUN wget https://github.com/pcingola/SnpEff/archive/refs/tags/v${SNPEFF_VER}.tar.gz && \
  tar -xvf v${SNPEFF_VER}.tar.gz && \
  rm v${SNPEFF_VER}.tar.gz && \ 
  wget https://github.com/pcingola/SnpSift/archive/refs/tags/v${SNPSIFT_VER}.tar.gz && \
  tar -xvf v${SNPSIFT_VER}.tar.gz && \
  rm v${SNPSIFT_VER}.tar.gz

# Build libraries from the source code using Maven.
RUN cd SnpEff-${SNPEFF_VER}/lib && \
  mvn install:install-file -Dfile=antlr-4.5.1-complete.jar -DgroupId=org.antlr -DartifactId=antlr -Dversion=4.5.1 -Dpackaging=jar && \
  mvn install:install-file -Dfile=biojava3-core-3.0.7.jar -DgroupId=org.biojava -DartifactId=biojava3-core -Dversion=3.0.7 -Dpackaging=jar && \
  mvn install:install-file -Dfile=biojava3-structure-3.0.7.jar -DgroupId=org.biojava -DartifactId=biojava3-structure -Dversion=3.0.7 -Dpackaging=jar

# Once libraries are installed, use make.sh to build the code.
COPY make.sh .
COPY galaxy.sh .
RUN bash make.sh

# Modify java executables and set environment variable $PATH
RUN mv SnpEff-${SNPEFF_VER} snpEff && \
  chmod +x /snpEff/snpEff.jar && \
  echo "#!/bin/bash" >> /snpEff/snpeff && \
  chmod +x /snpEff/SnpSift.jar && \
  echo "#!/bin/bash" >> /snpEff/snpsift && \
  echo "exec java -jar /snpEff/snpEff.jar """"$""@"""" " >> /snpEff/snpeff && \
  chmod +x /snpEff/snpeff && \
  echo "exec java -jar /snpEff/SnpSift.jar """"$""@"""" " >> /snpEff/snpsift && \
  chmod +x /snpEff/snpsift
ENV PATH="${PATH}:/snpEff" 

# Set working directory
RUN mkdir /data
WORKDIR /data

# Run test of annotation
FROM app as test

COPY test_snpeff_snpsift.sh .
RUN bash test_snpeff_snpsift.sh 

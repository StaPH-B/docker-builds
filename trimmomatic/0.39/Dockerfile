ARG TRIMMOMATIC_VER="0.39"

#use ubuntu as base image
FROM ubuntu:xenial as app
ARG TRIMMOMATIC_VER

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="Trimmomatic"
LABEL software.version=$TRIMMOMATIC_VER
LABEL description="Trimmomatic: A flexible read trimming tool for Illumina NGS data"
LABEL website="http://www.usadellab.org/cms/?page=trimmomatic"
LABEL license="https://github.com/usadellab/Trimmomatic/blob/main/distSrc/LICENSE"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
LABEL maintainer3="Sarah Nadeau"
LABEL maintainer3.email="sarah.nadeau@bsse.ethz.ch"

#install openjdk-11 jre
RUN apt-get update && apt-get install -y software-properties-common &&\
  add-apt-repository -y ppa:openjdk-r/ppa &&\
  apt-get update && apt-get install -y \
  openjdk-11-jre \
  wget \
  unzip

#copy the files into the image
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-${TRIMMOMATIC_VER}.zip &&\
  unzip Trimmomatic-${TRIMMOMATIC_VER}.zip &&\
  rm -rf Trimmomatic-${TRIMMOMATIC_VER}.zip &&\
  chmod +x Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar &&\
  echo "#!/bin/bash" >> /Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic &&\
  echo "exec java -jar /Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar """"$""@"""" " >> /Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic &&\
  chmod +x /Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic

ENV PATH="${PATH}:/Trimmomatic-${TRIMMOMATIC_VER}/"

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

FROM app as test
ARG TRIMMOMATIC_VER

# Run test script
COPY test_trimmomatic.sh .
RUN bash test_trimmomatic.sh $TRIMMOMATIC_VER

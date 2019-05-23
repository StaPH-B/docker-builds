#use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Trimmomatic"
LABEL software.version="0.39"
LABEL description="Trimmomatic: A flexible read trimming tool for Illumina NGS data"
LABEL website="http://www.usadellab.org/cms/?page=trimmomatic"
LABEL license="GNU General Public License"

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>
MAINTAINER Curtis Kapsak <pjx8@cdc.gov> 

#install openjdk-11 jre
RUN apt-get update && apt-get install -y software-properties-common &&\
  add-apt-repository -y ppa:openjdk-r/ppa &&\
  apt-get update && apt-get install -y \
  openjdk-11-jre \
  wget \
  unzip

#copy the files into the image
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip &&\
  unzip Trimmomatic-0.39.zip &&\
  rm -rf Trimmomatic-0.39.zip &&\
  chmod +x Trimmomatic-0.39/trimmomatic-0.39.jar &&\
  echo "#!/bin/bash" >> /Trimmomatic-0.39/trimmomatic &&\
  echo "exec java -jar /Trimmomatic-0.39/trimmomatic-0.39.jar """"$""@"""" " >> /Trimmomatic-0.39/trimmomatic &&\
  chmod +x /Trimmomatic-0.39/trimmomatic

ENV PATH="${PATH}:/Trimmomatic-0.39/"

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

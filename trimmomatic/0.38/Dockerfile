#use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Trimmomatic"
LABEL software.version="0.38"
LABEL description="Trimmomatic: A flexible read trimming tool for Illumina NGS data"
LABEL website="http://www.usadellab.org/cms/?page=trimmomatic"
LABEL license="GNU General Public License"

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>

#install openjdk-11 jre
RUN apt-get update && apt-get install -y software-properties-common &&\
 add-apt-repository -y ppa:openjdk-r/ppa && apt-get update && apt-get install -y \
 openjdk-11-jre\
 wget\
 unzip

#copy the files into the image
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip &&\
 unzip Trimmomatic-0.38.zip

 # create /data directory and set as working directory
 RUN mkdir /data
 WORKDIR /data

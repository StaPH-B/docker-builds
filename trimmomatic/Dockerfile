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

MAINTAINER Nicholas Florek <nicholas.florek@slh.wisc.edu>

#install java jre
RUN apt-get update && apt-get install -y openjdk-9-jre wget unzip

#copy the files into the image
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip
RUN unzip Trimmomatic-0.38.zip

FROM ubuntu:bionic as app

ARG FASTP_VER="0.23.2"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Fastp"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="An ultra-fast all-in-one FASTQ preprocessor"
LABEL website="https://github.com/OpenGene/fastp"
LABEL license="https://github.com/OpenGene/fastp/blob/master/LICENSE"
LABEL maintainer="Idowu Olawoye"
LABEL maintainer.email="olawoyei0303@run.edu.ng"

RUN apt-get update && apt-get install -y \
 wget

RUN mkdir fastp && \
 cd fastp && \ 
 wget http://opengene.org/fastp/fastp.0.23.1 && \
 mv fastp.0.23.1 fastp && \
 chmod a+x ./fastp && \
 mkdir /data
 
ENV PATH="$PATH:/fastp/"

WORKDIR /data

# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app as test

RUN fastp --help

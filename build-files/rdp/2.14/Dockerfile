# set global variables
ARG RDP_VER="2.14"

# build Dockerfile
FROM ubuntu:jammy as app
ARG RDP_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="RDP Classifier"
LABEL software.version=${RDP_VER}
LABEL description="The RDP Classifier is a naive Bayesian classifier which was developed to provide rapid taxonomic placement based on rRNA sequence data."
LABEL website="https://github.com/rdpstaff/classifier"
LABEL documentation="https://sourceforge.net/projects/rdp-classifier/"
LABEL license.url="https://github.com/rdpstaff/classifier/blob/master/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jre \
    wget \
    unzip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# Install rdp_classifer
RUN wget -q https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/rdp_classifier_${RDP_VER}.zip &&\
    unzip rdp_classifier_${RDP_VER}.zip &&\
    mv /rdp_classifier_${RDP_VER} /rdp_classifier &&\
    chmod +x /rdp_classifier/dist/classifier.jar &&\
    echo "#!/bin/bash" >> /rdp_classifier/dist/classifier &&\
    echo "exec java -jar /rdp_classifier/dist/classifier.jar """"$""@"""" " >> /rdp_classifier/dist/classifier &&\
    chmod +x /rdp_classifier/dist/classifier

ENV PATH="${PATH}:/rdp_classifier/dist" LC_ALL=C

CMD classifier

RUN mkdir data/
WORKDIR /data

# Running RDP on test controls
FROM app as test

WORKDIR /test

# running help to ensure executable is in path
RUN classifier

# testing on real files
RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests

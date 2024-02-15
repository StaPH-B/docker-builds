# set global variables
ARG RDP_VER="2.14"

# build Dockerfile
FROM ubuntu:focal as builder
ARG RDP_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="RDP Classifier"
LABEL software.version=${RDP_VER}
LABEL description="The RDP Classifier is a naive Bayesian classifier which was developed to provide rapid taxonomic placement based on rRNA sequence data."
LABEL website="https://sourceforge.net/projects/rdp-classifier/"
LABEL license.url="https://github.com/rdpstaff/classifier/blob/master/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    wget \
    curl \
    unzip 

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"

# Install RDP
ENV RDP_ZIP rdp_classifier_2.14.zip
ENV RDP_DOWNLOAD https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/rdp_classifier_2.14.zip/download
ENV RDP_PATH /rdp_classifier_2.14

RUN wget $RDP_DOWNLOAD -O /tmp/$RDP_ZIP &&\
  unzip /tmp/$RDP_ZIP -d /tmp &&\
  mv /tmp/${RDP_ZIP%.*} $RDP_PATH &&\
  rm -rf /tmp/$RDP_ZIP &&\
  chmod +x ${RDP_PATH}/dist/classifier.jar &&\
  echo "#!/bin/bash" >> /${RDP_PATH}/dist/classifier &&\
  echo "exec java -jar /${RDP_PATH}/dist/classifier.jar """"$""@"""" " >> /${RDP_PATH}/dist/classifier &&\
  chmod +x /${RDP_PATH}/dist/classifier

ENV PATH="${PATH}:/${RDP_PATH}/dist/"


# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG RDP_VER

COPY --from=builder /rdp_classifier_2.14/ /rdp_classifier_2.14/
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

ENV RDP_PATH /rdp_classifier_2.14
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"
ENV PATH="${PATH}:/${RDP_PATH}/dist"

RUN mkdir data/
WORKDIR /data

# Running RDP on test controls
FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests

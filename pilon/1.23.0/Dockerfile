FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="pilon"
LABEL software.version="1.23.0"
LABEL description="Automatically improve draft assemblies and find variation among strains"
LABEL website="https://github.com/broadinstitute/pilon"
LABEL license="https://github.com/broadinstitute/pilon/blob/master/LICENSE"
LABEL maintainer="Jake Garfin"
LABEL maintainer.email="jake.garfin@state.mn.us"

RUN apt-get update && apt-get install -y wget \
  openjdk-9-jre

# install pilon
RUN mkdir pilon && \
  cd pilon && \
  wget https://github.com/broadinstitute/pilon/releases/download/v1.23/pilon-1.23.jar && \
  chmod +x pilon-1.23.jar && \
  echo "#!/bin/bash" >> pilon && \
  echo "exec java -jar /pilon/pilon-1.23.jar """"$""@"""" " >> pilon && \
  chmod +x pilon && \
  mkdir /data

WORKDIR /data


ENV PATH="${PATH}:/pilon"

# set perl locale settings
ENV LC_ALL=C
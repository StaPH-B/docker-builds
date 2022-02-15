FROM ubuntu:focal as app

# ARG sets environment variables during the build stage
ARG PILONVER="1.24"
ARG JAVAVER="11"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="pilon"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Automatically improve draft assemblies and find variation among strains"
LABEL website="https://github.com/broadinstitute/pilon"
LABEL license="https://github.com/broadinstitute/pilon/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y \
  wget \
  openjdk-${JAVAVER}-jre

# install pilon
# creating a versionless jarfile so that scripts don't have to be updated
RUN mkdir pilon && \
  cd pilon && \
  wget https://github.com/broadinstitute/pilon/releases/download/v${PILONVER}/pilon-${PILONVER}.jar && \
  cp pilon-${PILONVER}.jar pilon.jar && \
  mkdir /data

WORKDIR /data


ENV PATH="${PATH}:/pilon"

ENV LC_ALL=C

# A second FROM insruction creates a new stage
# We use `test` for the test image
#FROM app as test

# Demonstrate that the program is successfully installed

# Option 1: run the program's internal tests, for example with SPAdes:
#RUN spades.py --test

# Option 2: write your own tests in a bash script in the same directory as your Dockerfile:
#COPY my_tests.sh .
#RUN bash my_tests.sh

# Option 3: write python unit tests in a tests/ directory in the same directory as your Dockerfile:
#RUN apt-get install -y python3
#RUN mkdir tests/
#COPY tests/ tests/
#RUN python3 -m unittest discover -s tests

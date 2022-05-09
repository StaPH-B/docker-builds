# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM ubuntu:focal as app

# ARG sets environment variables during the build stage
ARG NGMASTER_VER="0.5.8"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="ngmaster"
LABEL software.version=$NGMASTER_VER
LABEL description="In silico multi-antigen sequence typing for Neisseria gonorrhoeae (NG-MAST)"
LABEL website="https://github.com/MDU-PHL/ngmaster"
LABEL license="https://github.com/MDU-PHL/ngmaster/blob/master/LICENSE"
LABEL maintainer="Curtis kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
# cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 python3 \
 python3-biopython \
 python3-pip \
 unzip \
 wget \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install isPcr 0.33
RUN 

# install ngmaster via pypi
RUN pip3 install ngmaster==${NGMASTER_VER}

# ENV instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="$PATH" \
 LC_ALL=C

# WORKDIR sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app as test

# Demonstrate that the program is successfully installed

# Option 1: run the program's internal tests, for example with SPAdes:
RUN spades.py --test

# Option 2: write your own tests in a bash script in the same directory as your Dockerfile:
COPY my_tests.sh .
RUN bash my_tests.sh

# Option 3: write python unit tests in a tests/ directory in the same directory as your Dockerfile:
RUN apt-get install -y python3
RUN mkdir tests/
COPY tests/ tests/
RUN python3 -m unittest discover -s tests


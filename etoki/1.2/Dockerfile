# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM ubuntu:focal as app

# ARG sets environment variables during the build stage
ARG ETOKI_VER="1.2"
# Persistence with an env
ENV ETOKI_VER_ENV=$ETOKI_VER

# set workdir to default for building; set to /data at the end
WORKDIR /

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="EToKi"
LABEL software.version=$ETOKI_VER
LABEL description="All methods related to Enterobase data analysis pipelines"
LABEL website="https://github.com/zheminzhou/EToKi"
LABEL license="https://github.com/zheminzhou/EToKi/blob/master/LICENSE"
LABEL maintainer="Lee Katz"
LABEL maintainer.email="gzu2@cdc.gov"

# Multistage build
FROM staphb/shovill:1.1.0 AS shovill
FROM staphb/kraken2:2.1.2-no-db AS kraken2
FROM staphb/bowtie2:2.4.4 AS bowtie2
FROM staphb/lyveset:1.1.4f AS lyveset
FROM torognes/vsearch:2.21.1 as vsearch

# Back to the base app so that we have things like ENV variables
FROM app

# https://askubuntu.com/a/1013396
# avoid asking about timezone during apt-get
ARG DEBIAN_FRONTEND=noninteractive

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 perl \
 libcurl4-gnutls-dev \
 gcc \
 g++ \
 python-setuptools \
 zlib1g-dev \
 python3-pip \
 python3-dev \
 libgconf-2-4 \
 curl \
 unzip \
 build-essential \
 git \
 pigz \
 libcurl4 \
 ant \
 libssl-dev \
 python3-venv \
 wget && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

 #openjdk-8-jdk \
 #libcurl4-openssl-dev \

# Gimme python3 instead of python2
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

COPY --from=shovill   /skesa/skesa         /usr/local/bin/
COPY --from=shovill   /megahit             /megahit
COPY --from=shovill   /pilon               /pilon
COPY --from=shovill   /SPAdes-*-Linux      /spades
COPY --from=kraken2   /kraken2-2.1.2       /kraken2
COPY --from=kraken2   /kraken2-db          /kraken2-db
COPY --from=bowtie2   /opt/bowtie2-*       /opt/bowtie2

# Copied from flye container
ENV FLYE_VER="2.9"
RUN wget https://github.com/fenderglass/Flye/archive/${FLYE_VER}.tar.gz && \
 tar -xvf ${FLYE_VER}.tar.gz && \
 rm ${FLYE_VER}.tar.gz && \
 cd Flye-${FLYE_VER} && \
 python setup.py build && \
 python setup.py install

# Copied from samtools container
ENV SAMTOOLSVER="1.15"
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
 tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
 rm samtools-${SAMTOOLSVER}.tar.bz2 && \
 cd samtools-${SAMTOOLSVER} && \
 ./configure && \
 make && \
 make install

# vsearch aims to be a drop in replacement for usearch and so let's see if that's true
# ie, set `usearch` as path to vsearch
COPY --from=vsearch  /usr/local/bin/vsearch /usr/local/bin/vsearch
COPY --from=vsearch  /usr/local/bin/vsearch /usr/local/bin/usearch

## EToKi itself ##

# ENV instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="/usr/local/bin/EToKi:$PATH" \
 LC_ALL=C

WORKDIR /usr/local/bin
RUN git clone https://github.com/zheminzhou/EToKi.git -b ${ETOKI_VER_ENV}

RUN pip3 install ete3 numba numpy==1.21 pandas scikit-learn psutil click scipy

# Install all 3rd party software except the kraken database
WORKDIR /usr/local/bin/EToKi
# Install 3rd party tools
# Samtools has an issue for some reason and so explicitly give that path
# Also give the path to usearch since it is normally proprietary (although we have vsearch)
RUN python EToKi.py configure --install --usearch $(which usearch)
RUN python EToKi.py configure --path samtools=$(which samtools)
RUN python EToKi.py configure --path blast=$(which blastn)

# Fix the shebang line for all EToKi scripts to /usr/bin/env python
RUN find /usr/local/bin/EToKi -name '*.py' -exec sed -i.bak -e '1 i #!/usr/bin/env python\n# ^^^ inserted corrected shebang for this container' {} \;

# WORKDIR sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
# We use `test` for the test image
#FROM app as test

# Demonstrate that the program is successfully installed

# Option 1: run the program's internal tests, for example with SPAdes:
WORKDIR /usr/local/bin/EToKi
RUN usearch && which usearch
RUN EToKi.py --help
RUN bash -e example.bash

# Option 2: write your own tests in a bash script in the same directory as your Dockerfile:
#COPY my_tests.sh .
#RUN bash my_tests.sh

# Option 3: write python unit tests in a tests/ directory in the same directory as your Dockerfile:
#RUN apt-get install -y python3
#RUN mkdir tests/
#COPY tests/ tests/
#RUN python3 -m unittest discover -s tests
#

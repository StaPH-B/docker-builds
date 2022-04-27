# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
#FROM ubuntu:focal as app
# Copying the Freyja container a bit
FROM mambaorg/micromamba:0.22.0 as app

# ARG sets environment variables during the build stage
ARG SOFTWARENAME_VER="1.2"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="EToKi"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="All methods related to Enterobase data analysis pipelines"
LABEL website="https://github.com/zheminzhou/EToKi"
LABEL license="https://github.com/zheminzhou/EToKi/blob/master/LICENSE"
LABEL maintainer="Lee Katz"
LABEL maintainer.email="gzu2@cdc.gov"

# https://askubuntu.com/a/1013396
# avoid asking about timezone during apt-get
ARG DEBIAN_FRONTEND=noninteractive

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
 python3-pip \
 python3-dev \
 libgconf-2-4 \
 curl \
 unzip \
 libcurl4-openssl-dev \
 build-essential \
 git \
 pigz \
 libcurl4-openssl-dev \
 libcurl4 \
 ant \
 libssl-dev \
 python3-venv \
 wget && \
 apt-get autoclean

 #openjdk-8-jdk \

# Gimme python3 instead of python2
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Double check the python version
RUN python --version

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/etoki/bin:/opt/conda/envs/env/bin:${PATH}" \
 LC_ALL=C.UTF-8


RUN micromamba create -n etoki python=3.8 -c conda-forge -c bioconda -c defaults ete3 numba numpy pandas scikit-learn psutil click scipy && \
 micromamba clean -a -y
# might also have to install sklearn??

# Now get us into that yummy yummy EToKi env
ENV ENV_NAME="etoki"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

## EToKi itself ##

# ENV instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="/usr/local/bin/EToKi:$PATH" \
 LC_ALL=C

RUN cd /usr/local/bin && git clone https://github.com/zheminzhou/EToKi.git -b ${SOFTWARENAME_VER}

# Installs all 3rd party software except the kraken database and usearch
RUN cd /usr/local/bin/EToKi && python EToKi.py configure --install

RUN find /usr/local/bin/EToKi -name '*.py' -exec sed -i.bak -e '1 i #!/usr/bin/env python\n# ^^^ inserted corrected shebang for this container' {} \;

# WORKDIR sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
# We use `test` for the test image
#FROM app as test

# Demonstrate that the program is successfully installed

# Option 1: run the program's internal tests, for example with SPAdes:
RUN cd /usr/local/bin/EToKi && EToKi.py --help
#RUN cd /usr/local/bin/EToKi && $(which python) $(which EToKi.py) --help
RUN cd /usr/local/bin/EToKi && bash example.bash

# Option 2: write your own tests in a bash script in the same directory as your Dockerfile:
#COPY my_tests.sh .
#RUN bash my_tests.sh

# Option 3: write python unit tests in a tests/ directory in the same directory as your Dockerfile:
#RUN apt-get install -y python3
#RUN mkdir tests/
#COPY tests/ tests/
#RUN python3 -m unittest discover -s tests
#

# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM --platform=linux/x86_64 ubuntu:bionic as app

#https://bitbucket.org/genomicepidemiology/plasmidfinder/issues/10/version-number
# ARG sets environment variables during the build stage
ARG LIFTOFF_VER="1.6.3"
ARG MINIMAP2_VER="2.24"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="liftoff"
LABEL software.version=$LIFTOFF_VER
LABEL description="A tool that accurately maps annotations in GFF or GTF between assemblies of the same, or closely-related species."
LABEL website="https://github.com/agshumate/Liftoff"
LABEL license="https://github.com/agshumate/Liftoff/blob/master/LICENSE.md"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"


ENV DEBIAN_FRONTEND noninteractive

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update -y && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    libbz2-dev \
    liblzma-dev \
    wget && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

#Install Python from source
RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz && \
    tar -xf Python-3.8.0.tgz && \
    cd Python-3.8.0 && ./configure --enable-optimizations && make -j 8 && make altinstall

#Install pip and python dependencies
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.8 get-pip.py && pip3 install --upgrade pip

# Download git repository for Liftoff
RUN wget https://github.com/agshumate/Liftoff/archive/refs/tags/${LIFTOFF_VER}.tar.gz && \
    mkdir Liftoff && tar -xvf ${LIFTOFF_VER}.tar.gz -C Liftoff --strip-components 1 && \
    pip3 install Liftoff pytest

# MINIMAP2 installation
RUN wget -O minimap2.tar.gz https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 && \
        tar -jxvf minimap2.tar.gz
ENV PATH="${PATH}:/minimap2-${MINIMAP2_VER}_x64-linux"

# WORKDIR sets working directory
WORKDIR /data

FROM app as test

RUN liftoff -h

RUN python3.8 /Liftoff/liftoff/tests/test_basic.py

RUN python3.8 /Liftoff/liftoff/tests/test_advanced.py

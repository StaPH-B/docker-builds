# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM ubuntu:xenial as app

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:xenial"
LABEL software.version="3.12.0"

# RUN executes code during the build
# If you're using a Ubuntu base image, run apt-get update to update the package list first
RUN apt-get update && apt-get install -y \
    python \
    wget

# Download and install the tool
RUN wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz && \
    tar -xzf SPAdes-3.12.0-Linux.tar.gz && \
    rm -r SPAdes-3.12.0-Linux.tar.gz && \
    mkdir /data

# ENV instructions set environment variables that persist from the build into the resulting image
ENV PATH="${PATH}:/SPAdes-3.12.0-Linux/bin"

# WORKDIR sets working directory, this persists from the build into the resulting image
WORKDIR /data

# A second FROM insruction creates a new stage
# Here we add a test stage to run internal tests on the installed software.
FROM app as test

RUN spades.py --test

FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="BBTools"
LABEL software.version="38.94"
LABEL description="A set of tools labeled as \"Bestus Bioinformaticus\""
LABEL website="https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/"
LABEL license="https://jgi.doe.gov/disclaimer/"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Padraic Fanning"
LABEL maintainer2.email="faninnpm AT miamioh DOT edu"

RUN apt-get update && apt-get install -y build-essential \
    openjdk-8-jre-headless \
    wget && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean

# get miniconda and the artic-ncov19 repo
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  && \
    rm Miniconda3-latest-Linux-x86_64.sh

# set the environment
ENV PATH="/miniconda/bin:$PATH"

RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda install sambamba samtools && \
    conda clean -a -y

RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_38.94.tar.gz && \
    tar -xzf BBMap_38.94.tar.gz && \
    rm BBMap_38.94.tar.gz

ENV PATH="${PATH}:/bbmap"\
    LC_ALL=C

WORKDIR /data

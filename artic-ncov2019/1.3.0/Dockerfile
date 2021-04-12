FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="ARTIC-nCov19"
LABEL software.version="1.3.0"
LABEL description="A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore"
LABEL website="https://github.com/artic-network/fieldbioinformatics"
LABEL license="https://github.com/artic-network/fieldbioinformatics/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install needed software for conda install
RUN apt-get update && apt-get install -y \
  wget \
  git \
  build-essential && \
  apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

# get miniconda and the fieldbioinformatics repo
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
 bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  && \
  rm Miniconda3-latest-Linux-x86_64.sh && \
  git clone --recursive https://github.com/artic-network/fieldbioinformatics && \
  cd fieldbioinformatics/ && \
  git checkout 23a8460

# set path to miniconda
ENV PATH="/miniconda/bin:$PATH"

# create the conda environment and set as default
RUN conda env create -f /fieldbioinformatics/environment.yml && \
  echo "source activate artic" > /etc/bash.bashrc && \
  cd /fieldbioinformatics/ && \
  python setup.py install && \
  conda clean -a -y

# get primer-schemes
RUN git clone --recursive https://github.com/artic-network/primer-schemes && \
  cd primer-schemes/ && \
  git checkout 34fcf68

RUN mkdir /data

# set path
ENV PATH="/miniconda/envs/artic/bin:/miniconda/bin:/artic-ncov2019:/fieldbioinformatics:/primer-schemes:${PATH}"
WORKDIR /data

# just in case for singularity compatibility
ENV LC_ALL=C

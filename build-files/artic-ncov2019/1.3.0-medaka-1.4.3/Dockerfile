FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="ARTIC-nCov19"
LABEL software.version="1.3.0"
LABEL description="A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore"
LABEL website="https://github.com/artic-network/fieldbioinformatics"
LABEL license="https://github.com/artic-network/fieldbioinformatics/blob/master/LICENSE"
LABEL maintainer1="Abigail Shockey"
LABEL maintainer1.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install needed software for conda install
RUN apt-get update && apt-get install -y \
  wget \
  git \
  build-essential \
  libbz2-dev \
  libcurl4-openssl-dev \
  python3-setuptools \
  libz-dev && \
  apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

# get miniconda and the fieldbioinformatics repo
# checkout commit on 1.3.0-dev branch, March 5th 2021
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
 bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  && \
 rm Miniconda3-latest-Linux-x86_64.sh && \
 git clone --recursive https://github.com/artic-network/fieldbioinformatics && \
 cd fieldbioinformatics/ && \
 git checkout 00fdbc9

# set path to miniconda
ENV PATH="/miniconda/bin:$PATH"

# create the conda environment and set as default
# modify envrionment.yml to install medaka v1.4.3
# use mamba to speedup install/environment creation
RUN conda install mamba -n base -c conda-forge && \
  sed -i 's|medaka==1.2.3|medaka==1.4.3|' /fieldbioinformatics/environment.yml && \
 mamba env create -f /fieldbioinformatics/environment.yml && \
 echo "source activate artic" > /etc/bash.bashrc && \
 cd /fieldbioinformatics/ && \
 python setup.py install && \
 mamba clean -a -y

# get primer-schemes
RUN git clone --recursive https://github.com/artic-network/primer-schemes && \
 cd primer-schemes/ && \
 git checkout 34fcf68 && \
 mkdir /data

# set path & locale settings for singularity compatibility
ENV PATH="/miniconda/envs/artic/bin:/miniconda/bin:/artic-ncov2019:/fieldbioinformatics:/primer-schemes:${PATH}"\
 LC_ALL=C
WORKDIR /data

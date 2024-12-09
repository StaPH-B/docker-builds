# virsorter2
# https://github.com/jiarong/VirSorter2
# v2.1

# base image: Ubuntu
FROM ubuntu:xenial

# File Author / Maintainer
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="virsorter2"
LABEL software.version="2.1"
LABEL description="This software provides virsorter2 for viral prediction"
LABEL website="https://github.com/jiarong/VirSorter2"
LABEL license="https://github.com/jiarong/VirSorter2/blob/master/LICENSE"
LABEL maintainer="Joachim Johansen"
LABEL maintainer.email="joacjohansen@gmail.com"

ENV PATH=/miniconda/bin:${PATH} \
    LC_ALL=C

RUN apt-get update --fix-missing \
    && apt-get install -y wget gcc \
    && wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b \
    && rm Miniconda3-latest-Linux-x86_64.sh \
    && conda update -y conda \
    && conda install -c bioconda -c conda-forge python scikit-learn=0.22.1 imbalanced-learn pandas seaborn \
    && conda install -c bioconda -c conda-forge hmmer==3.3 prodigal screed ruamel.yaml click mamba \
    && conda install -c bioconda -c conda-forge snakemake \
    && conda install -c bioconda -c conda-forge pip git

RUN git clone https://github.com/jiarong/VirSorter2.git \
    && cd VirSorter2 \
    && pip install -e . 

RUN mkdir data
WORKDIR /data
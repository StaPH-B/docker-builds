# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Prokka"
LABEL software.version="1.13"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# install dependencies using conda
RUN apt-get update && apt-get -y install \
 bzip2 \
 gzip \
 wget && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh
RUN ./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda
ENV PATH="/miniconda/bin:$PATH"
# Configure channels for bioconda
RUN conda update -y -n base conda && conda config --add channels conda-forge && conda config --add channels defaults &&  conda config --add channels bioconda
RUN conda install -y prokka=1.13 && conda clean -ay

ENV PATH="./miniconda/bin/prokka:${PATH}"
WORKDIR /data
RUN prokka --setupdb

FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="ARTIC-nCov19"
LABEL software.version="1.1.0"
LABEL description="Conda environment for ARTIC network nCov19 bioinformatic SOP"
LABEL website="https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html"
LABEL license=""
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"

# install needed software for conda install
RUN apt-get update && apt-get install -y \
  wget \
  git \
  build-essential

# get miniconda and the artic-ncov19 repo
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
 bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  &&\
  rm Miniconda3-latest-Linux-x86_64.sh &&\
  git clone --recursive https://github.com/artic-network/artic-ncov2019.git &&\
  cd artic-ncov2019/ &&\
  git checkout 270d954

# set the environment
ENV PATH="/miniconda/bin:$PATH"

# RUN find /artic-ncov2019/ -type d -exec chmod 755 {} \;
#RUN find /artic-ncov2019/ -type f -exec chmod 755 {} \;

# create the conda environment and set as default
RUN conda env create -f /artic-ncov2019/environment.yml
RUN echo "source activate artic-ncov2019" > /etc/bash.bashrc
ENV PATH /miniconda/envs/artic-ncov2019/bin:$PATH
WORKDIR /data

RUN cp /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta.fai /artic-ncov2019/primer_schemes/nCoV-2019/V2/
RUN cp /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta.fai /artic-ncov2019/primer_schemes/nCoV-2019/V1/

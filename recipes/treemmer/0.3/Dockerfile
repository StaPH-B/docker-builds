FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Treemmer"
LABEL software.version="0.3"
LABEL description="Python tool to reduce size and redundancy of phylogenetic datasets"
LABEL website="https://github.com/fmenardo/Treemmer"
LABEL license="https://github.com/fmenardo/Treemmer/blob/master/COPYING"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install dependencies and clean apt
RUN  apt-get update && apt-get -y install \
  build-essential \
  git \
  wget \
  python2.7 \
  python-pip && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip2 install 'numpy==1.16.6' pathlib 'ete3==3.1.1' 'wheel==0.33.4' 'kiwisolver==1.1.0' 'matplotlib==2.2.4' 'joblib==0.13.2'

# install Treemer
RUN git clone https://git.scicore.unibas.ch/TBRU/Treemmer.git && \
  mkdir /data && \
  cd Treemmer && \
  chmod +x Treemmer_v0.3.py

# set working directory, PATH, and locale settings for singularity (just in case)
WORKDIR /data
ENV PATH="/Treemmer:${PATH}" \
  LC_ALL=C

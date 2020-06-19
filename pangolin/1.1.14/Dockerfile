FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="pangolin"
LABEL software.version="1.1.14"
LABEL description="Conda environment for Pangolin. Pangolin: Software package for assigning SARS-CoV-2 genome sequences to global lineages."
LABEL website="https://github.com/hCoV-2019/pangolin"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/hCoV-2019/pangolin/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install needed software for conda install
RUN apt-get update && apt-get install -y \
  wget \
  git \
  build-essential

# get miniconda and the pangolin repo
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh &&\
 bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  &&\
  rm Miniconda3-latest-Linux-x86_64.sh &&\
  git clone --recursive https://github.com/hCoV-2019/pangolin.git

# set the environment
ENV PATH="/miniconda/bin:$PATH"\
 LC_ALL=C

# create the conda environment and set as default
RUN conda env create -f /pangolin/environment.yml
RUN echo "source activate pangolin" > /etc/bash.bashrc
ENV PATH /miniconda/envs/pangolin/bin:$PATH
RUN cd pangolin && \
 python setup.py install && \
 mkdir /data

WORKDIR /data

RUN pangolin -v && pangolin -lv

FROM ubuntu:xenial

ENV PANGOLIN_VERSION="2.1.10" \
  PANGOLIN_LEARN_VERSION="2021-02-01"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="pangolin"
LABEL software.version=${PANGOLIN_VERSION}
LABEL description="Conda environment for Pangolin. Pangolin: Software package for assigning SARS-CoV-2 genome sequences to global lineages."
LABEL website="https://github.com/cov-lineages/pangolin"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/cov-lineages/pangolin/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Anders Goncalves da Silva"
LABEL maintainer2.email="andersgs@gmail.com"
LABEL maintainer3="Curtis Kapsak"
LABEL maintainer3.email="kapsakcj@gmail.com"

# install needed software for conda install; cleanup apt garbage
RUN apt-get update && apt-get install -y \
 wget \
 git \
 build-essential && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# get miniconda and the pangolin repo
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
 bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  && \
 rm Miniconda3-latest-Linux-x86_64.sh && \
 wget "https://github.com/cov-lineages/pangolin/archive/${PANGOLIN_VERSION}.tar.gz" && \
 tar -xf ${PANGOLIN_VERSION}.tar.gz && \
 rm ${PANGOLIN_VERSION}.tar.gz && \
 mv pangolin-${PANGOLIN_VERSION} pangolin

# set the environment
ENV PATH="/miniconda/bin:$PATH" \
 LC_ALL=C

# create the conda environment and set as default
RUN conda env create -f /pangolin/environment.yml && \
 echo "source activate pangolin" > /etc/bash.bashrc
ENV PATH /miniconda/envs/pangolin/bin:$PATH
RUN cd pangolin && \
 python setup.py install && \
 mkdir /data

# install and update pangoLEARN
# do it here to allow for caching of the previous layers
# check versions; 'pangolin -lv' deprecated in pangolin >=v2.2.0
RUN /bin/bash -c 'cd .. && \
 source activate pangolin && \
 wget https://github.com/cov-lineages/pangoLEARN/archive/${PANGOLIN_LEARN_VERSION}.tar.gz && \
 tar -xf ${PANGOLIN_LEARN_VERSION}.tar.gz && \
 rm ${PANGOLIN_LEARN_VERSION}.tar.gz && \
 cd pangoLEARN-${PANGOLIN_LEARN_VERSION} && \
 pip install . && \
 conda clean -a -y && \
 pangolin -v && pangolin -pv'

WORKDIR /data

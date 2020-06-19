FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1.1.14"
LABEL container.version="1.1.14"
LABEL software="pangolin"
LABEL software.version="1.1.14"
LABEL description="Conda environment for pangolin"
LABEL website="https://github.com/hCoV-2019/pangolin"
LABEL license="GNU General Public License v3.0"
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
ENV PATH="/miniconda/bin:$PATH"

# create the conda environment and set as default
RUN conda env create -f /pangolin/environment.yml
RUN echo "source activate pangolin" > /etc/bash.bashrc
ENV PATH /miniconda/envs/pangolin/bin:$PATH
RUN cd pangolin && python setup.py install
WORKDIR /data

RUN pangolin -v
RUN pangolin -lv

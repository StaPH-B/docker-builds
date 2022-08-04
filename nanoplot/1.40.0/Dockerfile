FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time.
ARG NANOPLOT_VER="1.40.0"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="nanoplot"
LABEL software.version="${NANOPLOT_VER}"
LABEL description="Plotting suite for Oxford Nanopore sequencing data and alignments"
LABEL website="https://github.com/wdecoster/NanoPlot"
LABEL license="https://github.com/wdecoster/NanoPlot/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies via apt; cleanup apt garbage; set locale to en_US.UTF-8
RUN apt-get update && apt-get install -y zlib1g-dev \
 bzip2 \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 libncurses5-dev \
 libssl-dev \
 python3 \
 python3-pip \
 python3-setuptools \
 locales && \
 locale-gen en_US.UTF-8 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# for singularity compatibility
ENV LC_ALL=C

# update pip, install NanoPlot
# matplotlib 3.1.3 to avoid warnings about some color API that isn't public anymore
RUN pip3 install matplotlib psutil requests NanoPlot==${NANOPLOT_VER} && \
 mkdir /data

WORKDIR /data

FROM app as test

RUN NanoPlot --help && NanoPlot --version
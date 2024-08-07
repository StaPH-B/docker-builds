ARG TRYCYCLER_VER=0.5.4

FROM ubuntu:jammy as app

ARG TRYCYCLER_VER
ARG MASH_VER=2.3
ARG MINIASM_VER=0.3
ARG MINIMAP2_VER=2.24

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Trycycler"
LABEL software.version="${TRYCYCLER_VER}"
LABEL description="A tool for generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Trycycler"
LABEL license="https://github.com/rrwick/Trycycler/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install prerequisites, cleanup apt garbage
# muscle version: 3.8.31
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
 python3 \
 python3-pip \
 gcc \
 wget \
 curl \
 bzip2 \
 build-essential \
 procps \
 ca-certificates \
 libz-dev \
 muscle \
 r-base \
 gfortran \
 libblas-dev \
 liblapack-dev && \
 apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# minimap2
# apt deps: curl bzip2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf -

# mash
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
 tar -xvf mash-Linux64-v${MASH_VER}.tar && \
 rm -rf mash-Linux64-v${MASH_VER}.tar

# miniasm
RUN wget https://github.com/lh3/miniasm/archive/v${MINIASM_VER}.tar.gz && \
 mkdir miniasm && \
 tar -xzvf v${MINIASM_VER}.tar.gz -C miniasm --strip-components 1 && \
 rm v${MINIASM_VER}.tar.gz && \
 cd miniasm && \
 make

# install R packages
RUN R -e "install.packages(c('ape',\
 'phangorn'),\
 repos = 'http://cran.us.r-project.org')"

# Trycycler
# apt deps: muscle gcc
RUN wget https://github.com/rrwick/Trycycler/archive/v${TRYCYCLER_VER}.tar.gz && \
 tar -xzf v${TRYCYCLER_VER}.tar.gz && \
 rm v${TRYCYCLER_VER}.tar.gz && \
 pip3 install ./Trycycler-${TRYCYCLER_VER} Pillow && \
 mkdir /data

# set /data as working directory
WORKDIR /data

# set env PATH variable for installed programs
# LC_ALL for singularity compatibility
# TERM set so that output is pretty during tests and so warnings about TERM not being set are silenced
ENV PATH="/mash-Linux64-v${MASH_VER}:/minimap2-${MINIMAP2_VER}_x64-linux:/miniasm:${PATH}"\
 LC_ALL=C \
 TERM=xterm-256color

FROM app as test

ARG TRYCYCLER_VER

WORKDIR /Trycycler-${TRYCYCLER_VER}

RUN trycycler --help && trycycler --version

RUN pytest
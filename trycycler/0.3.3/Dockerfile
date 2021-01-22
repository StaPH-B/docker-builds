FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Trycycler"
LABEL software.version="0.3.3"
LABEL description="A tool for generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Trycycler"
LABEL license="https://github.com/rrwick/Trycycler/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# so apt doesn't ask questions during install
ARG DEBIAN_FRONTEND=noninteractive

# install prerequisites, cleanup apt garbage 
# muscle version: 3.8.31
RUN apt-get update && apt-get install -y \
 python3 \
 python3-pip \
 gcc \
 wget \
 curl \
 bzip2 \
 build-essential \
 muscle \
 r-base && \
 apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# ARGs are arguments that are used during build time. They are no longer availble after image is built.
ARG TRYCYCLER_VER="0.3.3"
ARG MASH_VER="2.2"
ARG MINIMAP2_VER="2.17" 

# minimap2
# apt deps: curl bzip2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf -

# mash
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
 tar -xvf mash-Linux64-v${MASH_VER}.tar && \
 rm -rf mash-Linux64-v${MASH_VER}.tar

# install R packages
RUN R -e "install.packages(c('ape',\
 'phangorn'),\
 repos = 'http://cran.us.r-project.org')"

# Trycycler
# apt deps: muscle gcc
RUN wget https://github.com/rrwick/Trycycler/archive/v${TRYCYCLER_VER}.tar.gz && \
 tar -xzf v${TRYCYCLER_VER}.tar.gz && \
 rm v${TRYCYCLER_VER}.tar.gz && \
 pip3 install ./Trycycler-${TRYCYCLER_VER} && \
 mkdir /data

# set /data as working directory
WORKDIR /data

# set env path variable for installed programs. LC_ALL for singularity compatibility.
ENV PATH="/mash-Linux64-v${MASH_VER}:\
 /minimap2-${MINIMAP2_VER}_x64-linux:${PATH}"\
 LC_ALL=C

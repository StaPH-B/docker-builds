FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist at build time
ARG FASTANI_VER="1.32"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="FastANI"
LABEL software.version="1.32"
LABEL description="Fast alignment-free computation of whole-genome Average Nucleotide Identity"
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL license="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y wget \
 unzip \
 libgomp1 && \
 apt-get clean && rm -rf /var/lib/apt/lists/*

# download pre-compiled binary; unzip; put binary in /usr/bin; make /data
# apt dependencies: libgomp1 unzip wget
RUN wget https://github.com/ParBLiSS/FastANI/releases/download/v${FASTANI_VER}/fastANI-Linux64-v${FASTANI_VER}.zip && \
 unzip fastANI-Linux64-v${FASTANI_VER}.zip -d /usr/bin && \
 rm fastANI-Linux64-v${FASTANI_VER}.zip && \
 mkdir /data

# set working directory
WORKDIR /data

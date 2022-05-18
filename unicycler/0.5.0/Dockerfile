FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time
ARG unicyclerVer="0.5.0"
ARG blastVer="2.12.0"
# the spades.py version is actually VERY important
ARG spadesVer="3.15.4"
ARG raconVer="1.4.3"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Unicycler"
LABEL software.version="0.5.0"
LABEL description="Unicycler is an assembly pipeline for bacterial genomes."
LABEL website="https://github.com/rrwick/Unicycler"
LABEL license="https://github.com/rrwick/Unicycler#license"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
  python3 \
  python3-distutils \
  python-setuptools \
  cmake \
  build-essential \
  wget \
  libgomp1 \
  libz-dev \
  ca-certificates && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
  # python v3.8.10 is installed here; point 'python' to python3
  update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# install prerequisites including openjdk-11. Cleanup apt garbage
# RUN apt-get update && apt-get install -y software-properties-common && \
# add-apt-repository -y ppa:openjdk-r/ppa && apt-get update && apt-get install -y \
# python3 \
# python3-pip \
# python3-distutils \
# libz-dev \
# bowtie2 \
# openjdk-11-jre \
# python-is-python3 \
# wget \
# bzip2 \
# libncurses5-dev \
# libncursesw5-dev \
# libbz2-dev \
# liblzma-dev \
# cmake && \
# rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install SPAdes binary
RUN wget http://cab.spbu.ru/files/release${spadesVer}/SPAdes-${spadesVer}-Linux.tar.gz && \
  tar -xzf SPAdes-${spadesVer}-Linux.tar.gz && \
  rm -r SPAdes-${spadesVer}-Linux.tar.gz

# ncbi-blast+
# apt version of blast is very old (2.2.31)
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
  tar -xzf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
  rm ncbi-blast-${blastVer}+-x64-linux.tar.gz

# get racon
RUN wget https://github.com/isovic/racon/releases/download/${raconVer}/racon-v${raconVer}.tar.gz && \
  mkdir racon && \
  tar -xzvf racon-v${raconVer}.tar.gz -C racon --strip-components 1 && \
  rm racon-v${raconVer}.tar.gz && \
  cd racon && \
    mkdir build && \
    cd build && \
# for installing racon tests - keeping as a comment in case needed in the future
#      cmake -DCMAKE_BUILD_TYPE=Release -Dracon_build_tests=ON ../ && \
      cmake -DCMAKE_BUILD_TYPE=Release ../ && \
      make && \
      make install

# get unicycler
RUN wget https://github.com/rrwick/Unicycler/archive/v${unicyclerVer}.tar.gz && \
  mkdir unicycler && \
  tar -xzvf v${unicyclerVer}.tar.gz -C unicycler --strip-components 1 && \
  rm v${unicyclerVer}.tar.gz && \
  python3 /unicycler/setup.py install && \
  mkdir /data

ENV PATH="/SPAdes-${spadesVer}-Linux/bin:/ncbi-blast-${blastVer}+/bin/:${PATH}" \
 LC_ALL=C

# set PATH and locale settings for singularity
# ENV LC_ALL=C.UTF-8 \
#    PATH="${PATH}:/SPAdes-${spadesVer}-Linux/bin"

WORKDIR /data

FROM app as test

# RUN spades.py --test # added in to make sure that spades wasn't an issue

# RUN /racon/build/bin/racon_test # added in to make sure that racon wasn't an issue

# RUN cd /unicycler && python -m unittest

RUN wget https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/prokaryotes/bacteroides_fragilis/illumina/fastq/test1_1.fastq.gz &&\
  wget https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/prokaryotes/bacteroides_fragilis/illumina/fastq/test1_2.fastq.gz &&\
  wget https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/prokaryotes/bacteroides_fragilis/nanopore/fastq/test.fastq.gz

RUN unicycler --version && unicycler --help && \
  unicycler -1 test1_1.fastq.gz -2 test1_2.fastq.gz -l test.fastq.gz --out test

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
LABEL license="https://github.com/rrwick/Unicycler/blob/main/LICENSE"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
  python3 \
  python3-pip \
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

# install SPAdes binary
RUN wget http://cab.spbu.ru/files/release${spadesVer}/SPAdes-${spadesVer}-Linux.tar.gz && \
  tar -xzf SPAdes-${spadesVer}-Linux.tar.gz && \
  rm -r SPAdes-${spadesVer}-Linux.tar.gz

# ncbi-blast+
# ubuntu:focal apt version of blast is old-ish (2.9.0)
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
# for installing racon tests
  cmake -DCMAKE_BUILD_TYPE=Release -Dracon_build_tests=ON ../ && \
  cmake -DCMAKE_BUILD_TYPE=Release ../ && \
  make && \
  make install

# LC_ALL for singularity compatibility
# set PATH so that blast binaries and spades.py are available during unicycler install
# TERM set so that output is pretty during tests - also ensures unicycler unit tests pass 
ENV PATH="/SPAdes-${spadesVer}-Linux/bin:/ncbi-blast-${blastVer}+/bin/:${PATH}" \
 LC_ALL=C.UTF-8 \
 TERM=xterm-256color

# get unicycler; install
RUN wget https://github.com/rrwick/Unicycler/archive/v${unicyclerVer}.tar.gz && \
  mkdir unicycler && \
  tar -xzvf v${unicyclerVer}.tar.gz -C unicycler --strip-components 1 && \
  rm v${unicyclerVer}.tar.gz && \
  python3 /unicycler/setup.py install && \
  mkdir /data

# final working directory in app layer is /data, as usual
WORKDIR /data

FROM app as test

# test spades and unicycler unit tests
RUN spades.py --test && \
  cd /unicycler && python -m unittest

# test racon; added in to make sure that racon wasn't an issue
RUN /racon/build/bin/racon_test 

# testing on the test data (ILMN and ONT) provided with unicycler code
RUN unicycler --version && unicycler --help && \
  unicycler -1 /unicycler/sample_data/short_reads_1.fastq.gz \
  -2 /unicycler/sample_data/short_reads_2.fastq.gz \
  -l /unicycler/sample_data/long_reads_high_depth.fastq.gz \
  --out sample_data_hybrid_asm_test

# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM ubuntu:xenial as app

# ARG sets environment variables during the build stage
# USHER ver is in the conda version style.
ARG SHIGATYPER_VER="2.0.1"
ARG SAMTOOLSVER="1.15"
ARG MINIMAP2_VER="2.24"
ARG bcftoolsVer="1.14"


# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="shigatyper"
LABEL software.version=$SHIGATYPER_VER
LABEL description="Determine Shigella serotype using Illumina (single or paired-end) or Oxford Nanopore reads!"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y \
 wget \
 git \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 zlib1g-dev \
 libssl-dev \
 gcc \
 make \
 perl \
 bzip2 \
 gnuplot \
 ca-certificates \
 gawk \
 curl \
 build-essential && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

 # shigatyper depends on samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
   tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
   rm samtools-${SAMTOOLSVER}.tar.bz2 && \
   cd samtools-${SAMTOOLSVER} && \
   ./configure && \
   make && \
   make install && \
   cd ..

 # shigatyper depends on MINIMAP2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf -
ENV PATH="${PATH}:/minimap2-${MINIMAP2_VER}_x64-linux"

 # shigatyper depends on bcftools
RUN wget https://github.com/samtools/bcftools/releases/download/${bcftoolsVer}/bcftools-${bcftoolsVer}.tar.bz2 && \
  tar -vxjf bcftools-${bcftoolsVer}.tar.bz2 && \
  rm bcftools-${bcftoolsVer}.tar.bz2 && \
  cd bcftools-${bcftoolsVer} && \
  make && \
  make install && \
  cd ..

# get miniconda and the shigatyper repo
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
 bash ./Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b  && \
 rm Miniconda3-latest-Linux-x86_64.sh && \
 wget https://github.com/CFSAN-Biostatistics/shigatyper/archive/refs/tags/conda-package-${SHIGATYPER_VER}.tar.gz && \
 tar -xf conda-package-${SHIGATYPER_VER}.tar.gz && \
 rm conda-package-${SHIGATYPER_VER}.tar.gz && \
 mv -v shigatyper-* shigatyper

# set the environment
ENV PATH="${PATH}:/minimap2-${MINIMAP2_VER}_x64-linux"
ENV PATH="/miniconda/bin:$PATH" \
  LC_ALL=C

# install shigatyper
RUN cd shigatyper && \
  pip install . && \
  conda clean -a -y && \
  mkdir /data

# WORKDIR sets working directory
WORKDIR /data

RUN chmod -R a+rwx /miniconda/bin/shigatyper

CMD ["shigatyper"]

#This software takes fastq files which may to large for the git repository; would like guidance here.
FROM app as test

RUN shigatyper -h && \
  shigatyper --version && \
  wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz && \
  tar -vxzf sratoolkit.tar.gz && \
  rm sratoolkit.tar.gz
ENV PATH="$PATH:/data/sratoolkit.2.9.2-ubuntu64/bin" \
  LC_ALL=C
RUN fasterq-dump SRR8186675 &&\
  shigatyper --R1 SRR8186675_1.fastq --R2 SRR8186675_2.fastq

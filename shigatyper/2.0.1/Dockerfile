FROM ubuntu:focal as app

ARG SHIGATYPER_VER="2.0.1"
ARG SAMTOOLSVER="1.9"
ARG BCFTOOLSVER="1.9"
ARG MINIMAP2_VER="2.24"

ARG DEBIAN_FRONTEND=noninteractive

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="4"
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
 python3 \
 python3-setuptools \
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

# shigatyper depends on bcftools
RUN wget https://github.com/samtools/bcftools/releases/download/${BCFTOOLSVER}/bcftools-${BCFTOOLSVER}.tar.bz2 && \
  tar -vxjf bcftools-${BCFTOOLSVER}.tar.bz2 && \
  rm bcftools-${BCFTOOLSVER}.tar.bz2 && \
  cd bcftools-${BCFTOOLSVER} && \
  make && \
  make install && \
  cd ..

# shigatyper depends on MINIMAP2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf -

# get shigatyper repo
# RUN git clone -b conda-package-${SHIGATYPER_VER} https://github.com/CFSAN-Biostatistics/shigatyper && \
RUN wget https://github.com/CFSAN-Biostatistics/shigatyper/archive/refs/tags/conda-package-${SHIGATYPER_VER}.tar.gz && \
 tar -xf conda-package-${SHIGATYPER_VER}.tar.gz && \
 rm conda-package-${SHIGATYPER_VER}.tar.gz && \
 cd shigatyper-conda-package-${SHIGATYPER_VER} && \
 python3 setup.py install && \
 samtools faidx /usr/local/lib/python3.8/dist-packages/ShigaTyper-${SHIGATYPER_VER}-py3.8.egg/shigatyper/resources/ShigellaRef5.fasta

# set the environment
ENV PATH="${PATH}:/shigatyper-conda-package-${SHIGATYPER_VER}:/minimap2-${MINIMAP2_VER}_x64-linux" \
  LC_ALL=C

# WORKDIR sets working directory
WORKDIR /data

FROM app as test

# install fastq-dl via conda for downloading data
# instead installing fastq-dl from bioconda and using that to get the fastq files for testing
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b && \
rm Miniconda3-latest-Linux-x86_64.sh

# put miniconda and fastq-dl environment bin in the PATH
ENV PATH="/miniconda/bin:/miniconda/envs/fastq-dl/bin:${PATH}"

# create the fastq-dl conda environment
RUN conda create -y -n fastq-dl -c conda-forge -c bioconda -c defaults fastq-dl

# don't know if this is actually needed or not. keeping just in case
RUN echo "source activate fastq-dl" > /etc/bash.bashrc

# for activating fastq-dl conda environment
SHELL ["conda", "run", "-n", "fastq-dl", "/bin/bash", "-c"]

# download fastq files; list out files in PWD
RUN fastq-dl SRR8186675 ENA && \
 fastq-dl SRR7738178 ENA && \
 ls -lh

# revert shell back to default
SHELL ["/bin/sh", "-c"]

# actually run shigatyper on test fastq files
RUN shigatyper --R1 SRR8186675_1.fastq.gz --R2 SRR8186675_2.fastq.gz --name SRR8186675 && \
 shigatyper --R1 SRR7738178_1.fastq.gz --R2 SRR7738178_2.fastq.gz --name SRR7738178

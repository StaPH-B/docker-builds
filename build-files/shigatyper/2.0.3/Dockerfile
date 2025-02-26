FROM ubuntu:focal as app

ARG SHIGATYPER_VER="2.0.3"
ARG SAMTOOLSVER="1.9"
ARG BCFTOOLSVER="1.9"
ARG MINIMAP2_VER="2.24"

ARG DEBIAN_FRONTEND=noninteractive

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="shigatyper"
LABEL software.version=${SHIGATYPER_VER}
LABEL description="Determine Shigella serotype using Illumina (single or paired-end) or Oxford Nanopore reads!"
LABEL website="https://github.com/CFSAN-Biostatistics/shigatyper"
LABEL license="https://github.com/CFSAN-Biostatistics/shigatyper/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"

# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
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
  tar -xjf bcftools-${BCFTOOLSVER}.tar.bz2 && \
  rm bcftools-${BCFTOOLSVER}.tar.bz2 && \
  cd bcftools-${BCFTOOLSVER} && \
  make && \
  make install && \
  cd ..

# shigatyper depends on MINIMAP2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxf -

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

# test layer
FROM app as test

# fetch test data from ENA FTP
# SRR8186675 = https://www.ncbi.nlm.nih.gov/biosample/SAMN10040549 , expect Shigella boydii serotype 12
# SRR7738178 = https://www.ncbi.nlm.nih.gov/biosample/SAMN09878976 , expect Shigella sonnei (I think Form II?)
RUN wget -P /data ftp.sra.ebi.ac.uk/vol1/fastq/SRR818/005/SRR8186675/SRR8186675_1.fastq.gz && \
  wget -P /data ftp.sra.ebi.ac.uk/vol1/fastq/SRR818/005/SRR8186675/SRR8186675_2.fastq.gz && \
  wget -P /data ftp.sra.ebi.ac.uk/vol1/fastq/SRR773/008/SRR7738178/SRR7738178_1.fastq.gz && \
  wget -P /data ftp.sra.ebi.ac.uk/vol1/fastq/SRR773/008/SRR7738178/SRR7738178_2.fastq.gz

# actually run shigatyper on test fastq files; ls to see output filenames
RUN shigatyper --R1 /data/SRR8186675_1.fastq.gz --R2 /data/SRR8186675_2.fastq.gz --name SRR8186675 && \
  shigatyper --R1 /data/SRR7738178_1.fastq.gz --R2 /data/SRR7738178_2.fastq.gz --name SRR7738178 && \
  echo && \
  ls -lh && \
  shigatyper --version

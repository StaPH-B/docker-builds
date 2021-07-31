FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Shovill-SE"
LABEL software.version="1.1.0"
LABEL description="faster than SPAdes de novo DBG genome assembler for single-end reads"
LABEL website="https://github.com/rpetit3/shovill"
LABEL lisence="https://github.com/tseemann/shovill/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer="Robert A. Petit III"
LABEL maintainer.email="robert.petit@theiagen.com"

# install dependencies, cleanup apt garbage
RUN apt-get update && apt-get install -y python \
  wget \
  pigz \
  zlib1g-dev \
  make \
  gcc \
  g++ \
  libpthread-stubs0-dev \
  openjdk-9-jre \
  unzip \
  bzip2 \
  libncurses5-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  libssl-dev \
  libfindbin-libs-perl && \
  apt-get clean && apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

# SPAdes
ENV spadesVer=3.14.1
RUN wget https://github.com/ablab/spades/releases/download/v${spadesVer}/SPAdes-${spadesVer}-Linux.tar.gz && \
  tar -xzf SPAdes-${spadesVer}-Linux.tar.gz && \
  rm SPAdes-${spadesVer}-Linux.tar.gz

# Seqtk 1.3
RUN mkdir seqtk && \ 
  cd seqtk && \
  wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz && \
  tar -zxf v1.3.tar.gz && \
  rm v1.3.tar.gz && \
  cd seqtk-1.3/ && \
  make && \
  make install

# kmc
RUN mkdir kmc && \
  cd kmc && \
  wget https://github.com/refresh-bio/KMC/releases/download/v3.1.1/KMC3.1.1.linux.tar.gz && \
  tar -xzf KMC3.1.1.linux.tar.gz && \
  rm KMC3.1.1.linux.tar.gz  

# lighter 1.1.1
RUN wget https://github.com/mourisl/Lighter/archive/v1.1.1.tar.gz && \
  tar -zxf v1.1.1.tar.gz && \
  rm -rf v1.1.1.tar.gz && \
  cd Lighter-1.1.1 && \
  make

# trimmomatic 0.38
RUN mkdir trimmomatic && \
  cd trimmomatic && \
  wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip && \
  unzip Trimmomatic-0.38.zip && \
  rm -rf Trimmomatic-0.38.zip && \
  chmod +x Trimmomatic-0.38/trimmomatic-0.38.jar && \
  echo "#!/bin/bash" >> trimmomatic && \
  echo "exec java -jar /trimmomatic/Trimmomatic-0.38/trimmomatic-0.38.jar """"$""@"""" " >> trimmomatic && \
  chmod +x trimmomatic

# bwa (mem) 0.7.17
RUN mkdir bwa && \
  cd bwa && \
  wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2 && \
  tar -xjf bwa-0.7.17.tar.bz2 && \
  rm bwa-0.7.17.tar.bz2 && \
  cd bwa-0.7.17 && \
  make

# samtools 1.10 
RUN mkdir samtools && \
  cd samtools && \
  wget https://github.com/samtools/samtools/releases/download/1.10/samtools-1.10.tar.bz2 && \
  tar -xjf samtools-1.10.tar.bz2 && \
  rm samtools-1.10.tar.bz2 && \
  cd samtools-1.10 && \
  ./configure && \
  make && \
  make install

# skesa 2.3.0 (skesa 2.4.0 binary works better on ubuntu:bionic, so not upgrading here)
RUN mkdir skesa && \
  cd skesa && \
  wget https://github.com/ncbi/SKESA/releases/download/v2.3.0/skesa.centos6.10 && \
  mv skesa.centos6.10 skesa && \
  chmod +x skesa

# MEGAHIT 1.1.4 binary (I'm pretty sure these are binaries at this point)
RUN mkdir megahit && \
  cd megahit && \
  wget https://github.com/voutcn/megahit/releases/download/v1.1.4/megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin.tar.gz && \
  tar -xzf megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin.tar.gz && \
  rm megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin.tar.gz

# Velvet 1.2.10
RUN mkdir velvet && \
  cd velvet && \
  wget https://github.com/dzerbino/velvet/archive/v1.2.10.tar.gz && \
  tar -xzf v1.2.10.tar.gz && \
  rm -rf v1.2.10.tar.gz && \
  cd velvet-1.2.10 && \
  make

# Flash 1.2.11
RUN mkdir flash && \
  cd flash && \
  wget https://sourceforge.net/projects/flashpage/files/FLASH-1.2.11.tar.gz && \
  tar -zxf FLASH-1.2.11.tar.gz && \
  rm -rf FLASH-1.2.11.tar.gz && \
  cd FLASH-1.2.11 && \
  make

# pilon 1.22
RUN mkdir pilon && \
  cd pilon && \
  wget https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar && \
  chmod +x pilon-1.22.jar && \
  echo "#!/bin/bash" >> pilon && \
  echo "exec java -jar /pilon/pilon-1.22.jar """"$""@"""" " >> pilon && \
  chmod +x pilon

# Samclip
RUN mkdir samclip && \
  cd samclip && \
  wget https://raw.githubusercontent.com/tseemann/samclip/master/samclip && \
  chmod +x samclip

# aaannnddd finally install shovill-se v1.1.0 itself
# extra perl module I had to install via apt-get: libfindbin-libs-perl
# create /data for working directory
RUN mkdir shovill && \
  cd shovill && \
  wget https://github.com/rpetit3/shovill/archive/refs/tags/v1.1.0se.tar.gz && \
  tar -xzf v1.1.0se.tar.gz && \
  rm v1.1.0se.tar.gz && \
  mkdir /data

# set /data as working directory
WORKDIR /data

# set $PATH's
ENV PATH="${PATH}:\
/SPAdes-${spadesVer}-Linux/bin:\
/kmc:\
/Lighter-1.1.1:\
/trimmomatic:\
/bwa/bwa-0.7.17:\
/skesa:\
/megahit/megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin:\
/velvet/velvet-1.2.10:\
/flash/FLASH-1.2.11:\
/shovill/shovill-1.1.0se/bin:\
/pilon:\
/samclip"\
     LC_ALL=C

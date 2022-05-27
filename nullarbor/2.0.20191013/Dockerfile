FROM ubuntu:focal as app

# pulling a lot of these from the required versions here:
# https://github.com/tseemann/nullarbor/blob/041ded1748be0c650fb13f6685e205f0f2eef18d/bin/nullarbor.pl#L488
ARG NULLARBOR_VER="2.0.20191013"
ARG SHOVILL_VER="1.0.0"
ARG MEGAHIT_VER="1.1"
ARG SKESA_VER="2.3.0"
ARG SNIPPY_VER="4.2.0"
ARG PROKKA_VER="1.12"
ARG QUICKTREE_VER="2.4"
ARG IQTREE_VER="1.6"
ARG ROARY_VER="3.0"
ARG MLST_VER="2.10"
ARG ABRICATE_VER="0.8"
ARG SNP-DISTS_VER="0.6"
ARG TRIMMOMATIC_VER="0.36"
ARG SPADES_VER="3.12.0"
ARG KRAKEN_VER="1.0"
# might add kraken2 later?
ARG MASH_VER="2.1"
ARG CENTRIFUGE_VER="1.0"


LABEL base.image="ubuntu:focal"
LABEL container.version="1"
LABEL software="Nullarbor"
LABEL software.version="v2.0.20191013"
LABEL description="Reads to report for public health and clinical microbiology"
LABEL website="https://github.com/tseemann/shovill"
LABEL lisence="https://github.com/tseemann/shovill/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

ARG DEBIAN_FRONTEND="noninteractive"

# install dependencies, cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 python \
 wget \
 pigz \
 zlib1g-dev \
 make \
 gcc \
 g++ \
 libpthread-stubs0-dev \
 openjdk-11-jre \
 unzip \
 bzip2 \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 libssl-dev \
 libfindbin-libs-perl \
 libyaml-tiny-perl \
 libautobox-list-util-perl \
 bzip2 \
 gzip \
 libdatetime-perl \
 libxml-simple-perl \
 libdigest-md5-perl \
 bioperl \
 hmmer \
 libpath-tiny-perl \
 libmoo-perl \
 libfile-which-perl \
 libsvg-perl \
 libtext-csv-perl \
 liblist-moreutils-perl \
 libio-file-withpath-perl && \
 apt-get clean && apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# SPAdes
RUN wget https://github.com/ablab/spades/releases/download/v${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm SPAdes-${SPADES_VER}-Linux.tar.gz

# Seqtk 1.3
RUN wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz && \
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

# trimmomatic
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-${TRIMMOMATIC_VER}.zip && \
  unzip Trimmomatic-${TRIMMOMATIC_VER}.zip && \
  rm -rf Trimmomatic-${TRIMMOMATIC_VER}.zip && \
  chmod +x Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar && \
  echo "#!/bin/bash" >> trimmomatic && \
  echo "exec java -jar /Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar """"$""@"""" " >> trimmomatic && \
  chmod +x trimmomatic && \
  mv -v trimmomatic /usr/local/bin

# bwa (mem) 0.7.17
RUN wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2 && \
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
  wget https://github.com/ncbi/SKESA/releases/download/v${SKESA_VER}/skesa.centos6.10 && \
  mv skesa.centos6.10 skesa && \
  chmod +x skesa

# MEGAHIT 1.1.4 binary (I'm pretty sure these are binaries at this point)
# might have to change this version
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

# shovill
# extra perl module I had to install via apt-get: libfindbin-libs-perl
# create /data for working directory
RUN wget https://github.com/tseemann/shovill/archive/v${SHOVILL_VER}.tar.gz && \
  tar -xzf v${SHOVILL_VER}.tar.gz && \
  rm v${SHOVILL_VER}.tar.gz && \
  mkdir /data

# snippy
RUN wget https://github.com/tseemann/snippy/archive/v${SNIPPY_VER}.tar.gz && \
  tar -zxf v${SNIPPY_VER}.tar.gz && \
  rm v${SNIPPY_VER}.tar.gz


## PROKKA ## 
# bedtools (required by prokka)
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
 tar -zxf bedtools-2.29.0.tar.gz && \
 rm bedtools-2.29.0.tar.gz && \
 cd bedtools2 && \
 make

# so that barnnap tests pass
ENV PATH="${PATH}:/bedtools2/bin"

# install barrnap
RUN wget https://github.com/tseemann/barrnap/archive/0.9.tar.gz && \
    tar -zxf 0.9.tar.gz && \
    rm 0.9.tar.gz && \
    cd barrnap-0.9 && \
    make test

# install tbl2asn manually since the one included with prokka is expired. 
# Probably will have to do again in Dec 2021 unless Torsten removes it from prokka
RUN wget ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux64.tbl2asn.gz -O linux64.tbl2asn.gz && \
 gunzip linux64.tbl2asn.gz && \
 mv -v linux64.tbl2asn /usr/bin/tbl2asn && \
 chmod 755 /usr/bin/tbl2asn

# prokka
# perl modules installed via apt: libautobox-list-util-perl
RUN wget https://github.com/tseemann/prokka/archive/v${PROKKA_VER}.tar.gz && \
 tar -xzf v${PROKKA_VER}.tar.gz && \
 rm -rf v${PROKKA_VER}.tar.gz && \
 /prokka-${PROKKA_VER}/bin/prokka --setupdb && /prokka-${PROKKA_VER}/bin/prokka --listdb

## END PROKKA ##

# nullarbor
RUN wget https://github.com/tseemann/nullarbor/archive/refs/tags/v${NULLARBOR_VER}.tar.gz && \
 tar -xzf v${NULLARBOR_VER}.tar.gz && \
 rm v${NULLARBOR_VER}.tar.gz

# set /data as working directory
WORKDIR /data

# set $PATH's
ENV PATH="${PATH}:\
/SPAdes-${SPADES_VER}-Linux/bin:\
/kmc:\
/Lighter-1.1.1:\
/Trimmomatic-${TRIMMOMATIC_VER}:\
/bwa-0.7.17:\
/skesa:\
/megahit/megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin:\
/velvet/velvet-1.2.10:\
/flash/FLASH-1.2.11:\
shovill-1.1.0/bin:\
/pilon:\
/samclip:\
/nullarbor-${NULLARBOR_VER}/bin:\
/bedtools2/bin:\
/barrnap-0.9/bin:\
/prokka-${PROKKA_VER}/bin:\
/prokka-${PROKKA_VER}/binaries/common:\
/snippy-${SNIPPY_VER}/bin:\
/snippy-${SNIPPY_VER}/binaries/linux:\
/snippy-${SNIPPY_VER}/binaries/noarch"\
 LC_ALL=C

FROM app as test 

# print version and check dependencies
RUN nullarbor.pl --version && nullarbor.pl --check
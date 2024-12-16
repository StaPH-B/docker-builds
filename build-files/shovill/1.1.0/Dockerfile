# ephemeral environmental variables that go away after building the image
ARG SHOVILL_VER="1.1.0"
ARG SPADES_VER="3.15.5"
ARG SEQTK_VER="1.3"
ARG KMC_VER="3.1.1"
ARG LIGHTER_VER="1.1.1"
ARG TRIMMOMATIC_VER="0.39"
ARG BWA_VER="0.7.17"
# not sure if a more recent samtools is compatible or not, previously used samtools 1.10
ARG SAMTOOLS_VER="1.16.1"
ARG SKESA_VER="2.3.0"
ARG MEGAHIT_VER="1.1.4"
ARG VELVET_VER="1.2.10"
ARG FLASH_VER="1.2.11"
# also not sure if this upgraded pilon version is compatible, previously used 1.22
ARG PILON_VER="1.24"

FROM ubuntu:xenial as app

# reinstantiating variables so they are available in app FROM layer
ARG SHOVILL_VER
ARG SPADES_VER
ARG SEQTK_VER
ARG KMC_VER
ARG LIGHTER_VER
ARG TRIMMOMATIC_VER
ARG BWA_VER
ARG SAMTOOLS_VER
ARG SKESA_VER
ARG MEGAHIT_VER
ARG VELVET_VER
ARG FLASH_VER
ARG PILON_VER

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="3"
LABEL software="Shovill"
LABEL software.version="1.1.0"
LABEL description="faster than SPAdes de novo DBG genome assembler (with assembler options!)"
LABEL website="https://github.com/tseemann/shovill"
LABEL lisence="https://github.com/tseemann/shovill/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies, cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
  python \
  wget \
  ca-certificates \
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
  rm -rfv /var/lib/apt/lists/*

# SPAdes
RUN wget https://github.com/ablab/spades/releases/download/v${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm -v SPAdes-${SPADES_VER}-Linux.tar.gz

# Seqtk install
RUN mkdir -v seqtk && \ 
  cd seqtk && \
  wget https://github.com/lh3/seqtk/archive/v${SEQTK_VER}.tar.gz && \
  tar -zxf v${SEQTK_VER}.tar.gz && \
  rm -v v${SEQTK_VER}.tar.gz && \
  cd seqtk-${SEQTK_VER}/ && \
  make && \
  make install

# kmc
RUN mkdir kmc && \
  cd kmc && \
  wget https://github.com/refresh-bio/KMC/releases/download/v${KMC_VER}/KMC${KMC_VER}.linux.tar.gz && \
  tar -xzf KMC${KMC_VER}.linux.tar.gz && \
  rm -v KMC${KMC_VER}.linux.tar.gz  

# lighter
RUN wget https://github.com/mourisl/Lighter/archive/v${LIGHTER_VER}.tar.gz && \
  tar -zxf v${LIGHTER_VER}.tar.gz && \
  rm -rvf v${LIGHTER_VER}.tar.gz && \
  cd Lighter-${LIGHTER_VER} && \
  make

# trimmomatic
RUN mkdir trimmomatic && \
  cd trimmomatic && \
  wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-${TRIMMOMATIC_VER}.zip && \
  unzip Trimmomatic-${TRIMMOMATIC_VER}.zip && \
  rm -rf Trimmomatic-${TRIMMOMATIC_VER}.zip && \
  chmod +x Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar && \
  echo "#!/bin/bash" >> trimmomatic && \
  echo "exec java -jar /trimmomatic/Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar """"$""@"""" " >> trimmomatic && \
  chmod +x trimmomatic

# bwa (mem) install
RUN mkdir bwa && \
  cd bwa && \
  wget https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 && \
  tar -xjf bwa-${BWA_VER}.tar.bz2 && \
  rm bwa-${BWA_VER}.tar.bz2 && \
  cd bwa-${BWA_VER} && \
  make

# samtools install 
RUN mkdir samtools && \
  cd samtools && \
  wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
  rm samtools-${SAMTOOLS_VER}.tar.bz2 && \
  cd samtools-${SAMTOOLS_VER} && \
  ./configure && \
  make && \
  make install

# skesa 2.3.0 binary (skesa 2.4.0 binary works better on ubuntu:bionic, so not upgrading here)
RUN mkdir skesa && \
  cd skesa && \
  wget https://github.com/ncbi/SKESA/releases/download/v${SKESA_VER}/skesa.centos6.10 && \
  mv skesa.centos6.10 skesa && \
  chmod +x skesa

# MEGAHIT 1.1.4 binary (I'm pretty sure these are binaries at this point)
RUN mkdir megahit && \
  cd megahit && \
  wget https://github.com/voutcn/megahit/releases/download/v${MEGAHIT_VER}/megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin.tar.gz && \
  tar -xzf megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin.tar.gz && \
  rm megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin.tar.gz

# Velvet 1.2.10
RUN mkdir velvet && \
  cd velvet && \
  wget https://github.com/dzerbino/velvet/archive/v${VELVET_VER}.tar.gz && \
  tar -xzf v${VELVET_VER}.tar.gz && \
  rm -rf v${VELVET_VER}.tar.gz && \
  cd velvet-${VELVET_VER} && \
  make

# Flash 1.2.11
RUN mkdir flash && \
  cd flash && \
  wget https://sourceforge.net/projects/flashpage/files/FLASH-${FLASH_VER}.tar.gz && \
  tar -zxf FLASH-${FLASH_VER}.tar.gz && \
  rm -rf FLASH-${FLASH_VER}.tar.gz && \
  cd FLASH-${FLASH_VER} && \
  make

# pilon
RUN mkdir pilon && \
  cd pilon && \
  wget https://github.com/broadinstitute/pilon/releases/download/v${PILON_VER}/pilon-${PILON_VER}.jar && \
  chmod +x pilon-${PILON_VER}.jar && \
  echo "#!/bin/bash" >> pilon && \
  echo "exec java -jar /pilon/pilon-${PILON_VER}.jar """"$""@"""" " >> pilon && \
  chmod +x pilon

# Samclip (not going to pin a version, this is the recommended way of installing and there have not been updates since March 2020)
RUN mkdir samclip && \
  cd samclip && \
  wget https://raw.githubusercontent.com/tseemann/samclip/master/samclip && \
  chmod +x samclip

# aaannnddd finally install shovill v1.1.0 itself
# extra perl module I had to install via apt-get: libfindbin-libs-perl
# create /data for working directory
RUN wget https://github.com/tseemann/shovill/archive/v${SHOVILL_VER}.tar.gz && \
  tar -xzf v${SHOVILL_VER}.tar.gz && \
  rm v${SHOVILL_VER}.tar.gz && \
  mkdir /data

# set /data as final working directory
WORKDIR /data

# set $PATH's
ENV PATH="${PATH}:\
/SPAdes-${SPADES_VER}-Linux/bin:\
/kmc:\
/Lighter-${LIGHTER_VER}:\
/trimmomatic:\
/bwa/bwa-${BWA_VER}:\
/skesa:\
/megahit/megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin:\
/velvet/velvet-${VELVET_VER}:\
/flash/FLASH-${FLASH_VER}:\
/shovill-${SHOVILL_VER}/bin:\
/pilon:\
/samclip"\
     LC_ALL=C

# test layer
FROM app as test

# reinstantiating variable so it's available for cd cmd below
ARG SHOVILL_VER

# so that the below commands are run with /bin/bash shell and not /bin/sh - needed for bash-specific tricks below
SHELL ["/bin/bash", "-c"]

# test shamelessly stolen & modified from: https://github.com/tseemann/shovill/blob/master/.travis.yml
RUN cd /shovill-${SHOVILL_VER}/ && \
kmc && \
skesa --version && \
! shovill --doesnotexist && \
echo "TESTING SHOVILL + SPADES" && \
shovill --outdir out.spades --assembler spades --R1 test/R1.fq.gz --R2 test/R2.fq.gz --nostitch --noreadcorr --nocorr && \
grep '>' out.spades/contigs.fa && \
echo "TESTING SHOVILL + MEGAHIT" && \
shovill --outdir out.megahit --assembler megahit --R1 test/R1.fq.gz --R2 test/R2.fq.gz --trim && \
grep '>' out.megahit/contigs.fa && \
echo "TESTING SHOVILL + VELVET" && \
shovill --outdir out.velvet --assembler velvet --R1 test/R1.fq.gz --R2 test/R2.fq.gz --ram 4 --noreadcorr --nocorr && \
grep '>' out.velvet/contigs.fa && \
echo "TESTING SHOVILL + SKESA" && \
shovill --outdir out.skesa --assembler skesa --R1 test/R1.fq.gz --R2 test/R2.fq.gz --ram 4 --noreadcorr --nocorr && \
grep '>' out.velvet/contigs.fa

RUN shovill --help && shovill --check && shovill --version
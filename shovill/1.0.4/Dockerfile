FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Shovill"
LABEL software.version="1.0.4"
LABEL description="faster than SPAdes de novo DBG genome assembler (with assembler options!)"
LABEL website="https://github.com/tseemann/shovill"
LABEL lisence="https://github.com/tseemann/shovill/blob/master/LICENSE"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

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
  libfindbin-libs-perl

# get spades, unpack, remove tarball
RUN mkdir spades &&\
  cd spades &&\ 
  wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz &&\
  tar -xzf SPAdes-3.12.0-Linux.tar.gz &&\
  rm -r SPAdes-3.12.0-Linux.tar.gz

# get Seqtk
RUN mkdir seqtk &&\ 
  cd seqtk &&\
  wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz &&\
  tar -zxf v1.3.tar.gz &&\
  rm v1.3.tar.gz &&\
  cd seqtk-1.3/ &&\
  make &&\
  make install

# get Mash and the associated RefSeqSketches k=21 s=1000 database. Is db even needed?
RUN wget https://github.com/marbl/Mash/releases/download/v2.1/mash-Linux64-v2.1.tar && \
  tar -xvf mash-Linux64-v2.1.tar && \
  rm -rf mash-Linux64-v2.1.tar
  #### Commented out because I don't think the Mash database is needed
  #make database directory, store mash db there
  #mkdir /db && \
  #cd /db && \
  #wget https://gembox.cbcb.umd.edu/mash/RefSeqSketchesDefaults.msh.gz && \
  #gunzip RefSeqSketchesDefaults.msh.gz

# install lighter 1.1.1
RUN wget https://github.com/mourisl/Lighter/archive/v1.1.1.tar.gz &&\
  tar -zxf v1.1.1.tar.gz &&\
  rm -rf v1.1.1.tar.gz &&\
  cd Lighter-1.1.1 &&\
  make

# install trimmomatic
RUN mkdir trimmomatic &&\
  cd trimmomatic &&\
  wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip &&\
  unzip Trimmomatic-0.38.zip &&\
  rm -rf Trimmomatic-0.38.zip &&\
  chmod +x Trimmomatic-0.38/trimmomatic-0.38.jar &&\
  echo "#!/bin/bash" >> trimmomatic &&\
  echo "exec java -jar /trimmomatic/Trimmomatic-0.38/trimmomatic-0.38.jar """"$""@"""" " >> trimmomatic &&\
  chmod +x trimmomatic

# install bwa (mem)
RUN mkdir bwa &&\
  cd bwa &&\
  wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2 &&\
  tar -xjf bwa-0.7.17.tar.bz2 &&\
  rm bwa-0.7.17.tar.bz2 &&\
  cd bwa-0.7.17 &&\
  make

# install samtools 
RUN mkdir samtools &&\
  cd samtools &&\
  wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 &&\
  tar -xjf samtools-1.9.tar.bz2 &&\
  rm samtools-1.9.tar.bz2 &&\
  cd samtools-1.9 &&\
  ./configure &&\
  make &&\
  make install

# install skesa binary?(I think?)
RUN mkdir skesa &&\
  cd skesa &&\
  wget https://github.com/ncbi/SKESA/releases/download/v2.3.0/skesa.centos6.10 &&\
  mv skesa.centos6.10 skesa &&\
  chmod +x skesa

# install MEGAHIT binary (I'm pretty sure these are binaries at this point)
RUN mkdir megahit &&\
  cd megahit &&\
  wget https://github.com/voutcn/megahit/releases/download/v1.1.4/megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin.tar.gz &&\
  tar -xzf megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin.tar.gz &&\
  rm megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin.tar.gz

# install Velvet
RUN mkdir velvet &&\
  cd velvet &&\
  wget https://github.com/dzerbino/velvet/archive/v1.2.10.tar.gz &&\
  tar -xzf v1.2.10.tar.gz &&\
  rm -rf v1.2.10.tar.gz &&\
  cd velvet-1.2.10 &&\
  make

# install Flash
RUN mkdir flash &&\
  cd flash &&\
  wget https://sourceforge.net/projects/flashpage/files/FLASH-1.2.11.tar.gz &&\
  tar -zxf FLASH-1.2.11.tar.gz &&\
  rm -rf FLASH-1.2.11.tar.gz &&\
  cd FLASH-1.2.11 &&\
  make

# install pilon binary
RUN mkdir pilon &&\
  cd pilon &&\
  wget https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar &&\
  chmod +x pilon-1.22.jar &&\
  echo "#!/bin/bash" >> pilon &&\
  echo "exec java -jar /pilon/pilon-1.22.jar """"$""@"""" " >> pilon &&\
  chmod +x pilon

# Samclip
RUN mkdir samclip &&\
  cd samclip &&\
  wget https://raw.githubusercontent.com/tseemann/samclip/master/samclip &&\
  chmod +x samclip

# aaannnddd finally install shovill v1.0.4 itself
# extra perl module I had to install via apt-get: libfindbin-libs-perl
RUN mkdir shovill &&\
  cd shovill &&\
  wget https://github.com/tseemann/shovill/archive/v1.0.4.tar.gz &&\
  tar -xzf v1.0.4.tar.gz &&\
  rm v1.0.4.tar.gz

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

# set $PATH's
ENV PATH="${PATH}:\
/spades/SPAdes-3.12.0-Linux/bin:\
/mash-Linux64-v2.1:\
/Lighter-1.1.1:\
/trimmomatic:\
/bwa/bwa-0.7.17:\
/skesa:\
/megahit/megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin:\
/velvet/velvet-1.2.10:\
/flash/FLASH-1.2.11:\
/shovill/shovill-1.0.4/bin:\
/pilon:\
/samclip"

# set perl locale settings
ENV LC_ALL=C

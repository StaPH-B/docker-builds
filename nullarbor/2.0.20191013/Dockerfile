FROM ubuntu:focal as app

# pulling a lot of these from the required versions here:
# https://github.com/tseemann/nullarbor/blob/041ded1748be0c650fb13f6685e205f0f2eef18d/bin/nullarbor.pl#L488
ARG NULLARBOR_VER="2.0.20191013"
ARG SHOVILL_VER="1.1.0"
ARG MEGAHIT_VER="1.2.9"
ARG SKESA_VER="2.4.0"
ARG SNIPPY_VER="4.4.3"
ARG PROKKA_VER="1.14.6"
ARG QUICKTREE_VER="2.5"
ARG IQTREE_VER="2.2"
# roary installed via apt
#ARG ROARY_VER="3.0"
ARG MLST_VER="2.22.0"
ARG ABRICATE_VER="1.0.1"
ARG SNP_DISTS_VER="0.8.2"
ARG TRIMMOMATIC_VER="0.39"
ARG SPADES_VER="3.15.4"
ARG KRAKEN_VER="1.1.1"
# might add kraken2 later?
ARG MASH_VER="2.3"
ARG CENTRIFUGE_VER="1.0.4"
ARG IQTREE_VER="1.6.7"
ARG KRAKEN2_VER="2.1.2"


LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Nullarbor"
LABEL software.version="v2.0.20191013"
LABEL description="Reads to report for public health and clinical microbiology"
LABEL website="https://github.com/tseemann/nullarbor"
LABEL lisence="https://github.com/tseemann/nullarbor/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Frank Ambrosio"
LABEL maintainer2.email="frank.ambrosio@theiagen.com"

# to prevent apt from asking for a timezone for locale settings
ARG DEBIAN_FRONTEND="noninteractive"

# install dependencies, cleanup apt garbage
# roary via ubuntu:focal apt is 3.13.0
RUN apt-get update && apt-get install -y --no-install-recommends \
 git \
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
 libio-file-withpath-perl \
 roary=3.13.0+dfsg-1 \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 file \
 ncbi-blast+=2.9.0-2 \
 autoconf \
 automake \
 libtool \
 flex \
 bison && \
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

# skesa
RUN mkdir skesa && \
  cd skesa && \
  wget https://github.com/ncbi/SKESA/releases/download/${SKESA_VER}/skesa.centos.7.7 && \
  mv skesa.centos.7.7 skesa && \
  chmod +x skesa

# might have to change this version
RUN mkdir megahit && \
  cd megahit && \
  wget https://github.com/voutcn/megahit/releases/download/v${MEGAHIT_VER}/MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static.tar.gz && \
  tar -xzf MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static.tar.gz && \
  rm -v MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static.tar.gz

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
  rm -v v${SHOVILL_VER}.tar.gz && \
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

## ROARY ##
# DL Jellyfish, unpack, and install
RUN wget https://github.com/gmarcais/Jellyfish/releases/download/v1.1.12/jellyfish-1.1.12.tar.gz && \
 tar -zxf jellyfish-1.1.12.tar.gz && \
 rm -rf jellyfish-1.1.12.tar.gz && \
 cd jellyfish-1.1.12 && \
 ./configure --prefix=/opt/ && \
 make -j 4 && \
 make install

# DL Kraken1, unpack, and install
RUN wget https://github.com/DerrickWood/kraken/archive/v${KRAKEN_VER}.tar.gz && \
  tar -xzf v${KRAKEN_VER}.tar.gz && \
  rm -rf v${KRAKEN_VER}.tar.gz && \
  cd kraken-${KRAKEN_VER} && \
  mkdir /opt/kraken && \
  ./install_kraken.sh /opt/kraken/

# roary itself installed via apt
## END ROARY ##

## MLST ##
# any2fasta
RUN cd /usr/local/bin && \
  wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
  chmod +x any2fasta

# get mlst
RUN wget https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz &&\
 tar -xzf v${MLST_VER}.tar.gz &&\
 rm v${MLST_VER}.tar.gz && \
 /mlst-${MLST_VER}/bin/mlst --check && /mlst-${MLST_VER}/bin/mlst --list

## END MLST ##

# abricate
RUN wget https://github.com/tseemann/abricate/archive/v${ABRICATE_VER}.tar.gz && \
    tar -zxvf v${ABRICATE_VER}.tar.gz && \
    rm -rf v${ABRICATE_VER}.tar.gz

# snp-dists
RUN wget https://github.com/tseemann/snp-dists/archive/v${SNP_DISTS_VER}.tar.gz && \
 tar -xzf v${SNP_DISTS_VER}.tar.gz && \
 rm v${SNP_DISTS_VER}.tar.gz && \
 cd /snp-dists-${SNP_DISTS_VER} && \
 make && \
 make PREFIX=/usr/local install

# download mash binary
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
 tar -xvf mash-Linux64-v${MASH_VER}.tar && \
 rm -rf mash-Linux64-v${MASH_VER}.tar

# centrifuge
# this does not include building an index AKA database
RUN wget https://github.com/DaehwanKimLab/centrifuge/archive/refs/tags/v${CENTRIFUGE_VER}.tar.gz && \
 tar -xzf v${CENTRIFUGE_VER}.tar.gz && \
 rm -v v${CENTRIFUGE_VER}.tar.gz && \
 cd centrifuge-${CENTRIFUGE_VER} && \
 make && \
 make install prefix=/usr/local && \
 mkdir -v /centrifuge-db

# iqtree
RUN wget https://github.com/Cibiv/IQ-TREE/releases/download/v${IQTREE_VER}/iqtree-${IQTREE_VER}-Linux.tar.gz && \
 tar -xzf iqtree-${IQTREE_VER}-Linux.tar.gz && \
 rm iqtree-${IQTREE_VER}-Linux.tar.gz

# FastTree binary download; as of 2022-06-01 downloads version 2.1.11
RUN mkdir -v /FastTree && \
 wget http://www.microbesonline.org/fasttree/FastTree -P /FastTree && \
 chmod +x /FastTree/FastTree

# quicktree
RUN wget https://github.com/khowe/quicktree/archive/refs/tags/v${QUICKTREE_VER}.tar.gz && \
 tar -xzf v${QUICKTREE_VER}.tar.gz && \
 rm -v v${QUICKTREE_VER}.tar.gz && \
 cd /quicktree-${QUICKTREE_VER} && \
 make

# newick_utils
# no releases or tags, so manually setting to latest commit (da12115) to master branch
RUN git clone https://github.com/tjunier/newick_utils.git && \
 cd newick_utils && \
 git reset --hard da12115 && \
 autoreconf -fi && \
 ./configure && \
 make && \
 make check	&& \
 make install

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v${KRAKEN2_VER}.tar.gz && \
 tar -xzf v${KRAKEN2_VER}.tar.gz && \
 rm -rf v${KRAKEN2_VER}.tar.gz && \
 cd kraken2-${KRAKEN2_VER} && \
 ./install_kraken2.sh . && \
 mkdir -v /kraken2-db /kraken-db

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
/shovill-${SHOVILL_VER}/bin:\
/pilon:\
/samclip:\
/nullarbor-${NULLARBOR_VER}/bin:\
/bedtools2/bin:\
/barrnap-0.9/bin:\
/prokka-${PROKKA_VER}/bin:\
/prokka-${PROKKA_VER}/binaries/common:\
/snippy-${SNIPPY_VER}/bin:\
/snippy-${SNIPPY_VER}/binaries/linux:\
/snippy-${SNIPPY_VER}/binaries/noarch:\
/mlst-${MLST_VER}/bin:\
/abricate-${ABRICATE_VER}/bin:\
/mash-Linux64-v${MASH_VER}:\
/iqtree-${IQTREE_VER}-Linux/bin/:\
/FastTree:\
/quicktree-${QUICKTREE_VER}:\
/opt/kraken:\
/kraken2-${KRAKEN2_VER}"\
 LC_ALL=C\
 KRAKEN_DEFAULT_DB="/kraken-db"\
 KRAKEN2_DEFAULT_DB="/kraken2-db"\
 CENTRIFUGE_DEFAULT_DB="/centrifuge-db"

# test layer; may add more later once everything is installed
FROM app as test 

# print version and check dependencies
RUN nullarbor.pl --version

# make fake files to trick nullarbor dependency check
RUN touch ${KRAKEN_DEFAULT_DB}/database.idx ${KRAKEN_DEFAULT_DB}/database.kdb && \
 touch ${CENTRIFUGE_DEFAULT_DB}.1.cf ${CENTRIFUGE_DEFAULT_DB}.2.cf ${CENTRIFUGE_DEFAULT_DB}.3.cf

# uncomment for final checks
RUN nullarbor.pl --check
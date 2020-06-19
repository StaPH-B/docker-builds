FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="SeqSero2"
LABEL software.version="1.1.1"
LABEL description="Salmonella serotyping from genome sequencing data"
LABEL website="https://github.com/denglab/SeqSero2"
LABEL license="https://github.com/denglab/SeqSero2/blob/master/LICENSE"
LABEL maintainer1="Jake Garfin"
LABEL maintainer1.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
LABEL maintainer3="Kelsey Florek"
LABEL maintainer3.email="kelsey.florek@slh.wisc.edu"

# bedtools = 2.25.0 (seqsero2 readme lists 2.17.0)
# blast+ = 2.2.31 (seqsero2 readme lists 2.2.28)
# bwa = 0.7.12-r1039
# biopython = 1.73
# python = 3.5.2 (seqsero2 readme lists python3)
RUN apt-get update && apt-get install -y \
 python3 \
 python3-pip \
 python3-setuptools \
 bwa \
 ncbi-blast+ \
 bedtools \
 wget \
 zlib1g-dev \
 libbz2-dev \
 liblzma-dev \
 build-essential \
 libncurses5-dev \
 gcc \
 bzip2 \
 perl \
 make \
 libcurl4-gnutls-dev \
 libncurses5-dev \
 libssl-dev && \
 apt-get clean && apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# Tried to match dependency versions exactly as listed on SeqSero2 readme (20-05-21)
ENV samtoolsVer=1.8 \
    SalmIDVer=0.11 \
    SPAdesVer=3.9.0 \
    SeqSero2Ver=1.1.1 \
    sratoolkitVer=2.8.0

# sratoolkit
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/${sratoolkitVer}/sratoolkit.${sratoolkitVer}-ubuntu64.tar.gz && \
   tar -xzf sratoolkit.${sratoolkitVer}-ubuntu64.tar.gz && \
   rm -r sratoolkit.${sratoolkitVer}-ubuntu64.tar.gz

# samtools (installing from apt breaks SeqSero2 version check)
RUN wget https://github.com/samtools/samtools/releases/download/${samtoolsVer}/samtools-${samtoolsVer}.tar.bz2 && \
 tar -xjf samtools-${samtoolsVer}.tar.bz2 && \
 rm samtools-${samtoolsVer}.tar.bz2 && \
 cd samtools-${samtoolsVer} && \
 ./configure && \
 make && \
 make install

# SalmID
RUN wget https://github.com/hcdenbakker/SalmID/archive/${SalmIDVer}.tar.gz && \
 tar -xzf ${SalmIDVer}.tar.gz && \
 rm -rf ${SalmIDVer}.tar.gz

# SPAdes
RUN wget https://github.com/ablab/spades/releases/download/v${SPAdesVer}/SPAdes-${SPAdesVer}-Linux.tar.gz && \
 tar -xzf SPAdes-${SPAdesVer}-Linux.tar.gz && \
 rm -rf SPAdes-${SPAdesVer}-Linux.tar.gz

# SeqSero2
RUN wget https://github.com/denglab/SeqSero2/archive/v${SeqSero2Ver}.tar.gz && \
 tar -xzf v${SeqSero2Ver}.tar.gz && \
 rm -rf v${SeqSero2Ver}.tar.gz && \
 cd /SeqSero2-${SeqSero2Ver}/ && \
 python3 -m pip install -U pip && \
 python3 -m pip install . && \
 mkdir /data

# PATH edited to include /SeqSero2-1.1.0/bin in previous python3 command
# locale settings for singularity compatibility
ENV PATH="${PATH}:/SPAdes-${SPAdesVer}-Linux/bin:\
/SalmID-${SalmIDVer}:\
/sratoolkit.${sratoolkitVer}-ubuntu64/bin" \
    LC_ALL=C

WORKDIR /data

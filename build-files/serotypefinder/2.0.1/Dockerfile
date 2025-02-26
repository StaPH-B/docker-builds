ARG SEROTYPEFINDER_VER="2.0.1"
# important to get this commit due to line ending fix
# see here: https://bitbucket.org/genomicepidemiology/serotypefinder_db/commits/ada62c62a7fa74032448bb2273d1f7045c59fdda
ARG SEROTYPEFINDER_DB_COMMIT_HASH="ada62c62a7fa74032448bb2273d1f7045c59fdda"

FROM ubuntu:focal as app

# re-instantiating for use in the app layer
ARG SEROTYPEFINDER_VER
ARG SEROTYPEFINDER_DB_COMMIT_HASH

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2"
LABEL software="SerotypeFinder"
LABEL software.version="2.0.1"
LABEL description="Tool for identifying the serotype of E. coli from reads or assemblies"
LABEL website="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage 
# ncbi-blast+ v2.9.0 (ubuntu:focal), min required version is 2.8.1
# python3 v3.8.10, min required version is 3.5
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps \
 git \
 ncbi-blast+ \
 python3 \
 python3-pip \
 python3-setuptools \
 python3-dev \
 gcc \
 make \
 libz-dev \
 dos2unix \
 unzip && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install python dependencies
RUN pip3 install biopython==1.73 tabulate==0.7.7 cgecore==1.5.5

# Install kma
# apt deps: libz-dev (for compiling) 
RUN git clone --branch 1.0.1 --depth 1 https://bitbucket.org/genomicepidemiology/kma.git && \
 cd kma && \
 make && \
 mv -v kma* /usr/local/bin/

# download serotypefinder database using a specific commit hash to aid in reproducibility
# index database w/ kma
# NOTE: files HAVE to go into '/database' since that is the default location expected by serotyperfinder.py
# dos2unix on the FASTA files to ensure they have LF line endings (there's CRLF somewhere in those files despite the last commit to the db)
RUN mkdir /database && \
 git clone https://bitbucket.org/genomicepidemiology/serotypefinder_db.git /database && \
 cd /database && \
 git checkout ${SEROTYPEFINDER_DB_COMMIT_HASH} && \
 dos2unix *.fsa && \
 python3 INSTALL.py kma_index

# install serotypefinder; make /data
RUN git clone --branch ${SEROTYPEFINDER_VER} https://bitbucket.org/genomicepidemiology/serotypefinder.git && \
 mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="/serotypefinder:$PATH" \
 LC_ALL=C.UTF-8

# set final working directory for production docker image (app layer only)
WORKDIR /data

FROM app as test

# set working directory for test layer
WORKDIR /test

# download an example assembly; test with SerotypeFinder
# Escherichia coli complete genome (Unicycler assembly)
# GenBank Nucleotide entry: https://www.ncbi.nlm.nih.gov/nuccore/CP113091.1/
# BioSample:SAMN08799860
# expect O1:H7
RUN mkdir -v /test/asm-input-O1-H7 && \
 wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
 gunzip GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
 serotypefinder.py -i /test/GCA_012224845.2_ASM1222484v2_genomic.fna -x -o /test/asm-input-O1-H7 && \
 cat /test/asm-input-O1-H7/results_tab.tsv

# download Illumina reads for the same sample ^ and test reads as input into SerotypeFinder
RUN mkdir /test/reads-input-O1-H7 && \
 wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_1.fastq.gz && \
 wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_2.fastq.gz && \
 serotypefinder.py -i SRR6903006_1.fastq.gz SRR6903006_2.fastq.gz -x -o /test/reads-input-O1-H7 && \
 cat /test/reads-input-O1-H7/results_tab.tsv

# test using FASTA supplied with serotypefinder code
# expect O1:H9
RUN mkdir -p /test/serotypefinder-test-fsa && \
 serotypefinder.py -i /serotypefinder/test.fsa -x -o /test/serotypefinder-test-fsa && \
 cat /test/serotypefinder-test-fsa/results_tab.tsv

RUN serotypefinder.py --help

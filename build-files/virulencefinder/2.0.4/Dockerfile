ARG VIRULENCEFINDER_VER="2.0.1"
# Database not properly versioned, so using most recent commit made on 2023-05-03
# see here: https://bitbucket.org/genomicepidemiology/virulencefinder_db/commits/f678bdc15283aed3a45f66050d2eb3a6c9651f3f
ARG VIRULENCEFINDER_DB_COMMIT_HASH="f678bdc15283aed3a45f66050d2eb3a6c9651f3f"

FROM ubuntu:focal as app

# re-instantiating for use in the app layer
ARG VIRULENCEFINDER_VER
ARG VIRULENCEFINDER_DB_COMMIT_HASH

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="VirulenceFinder"
LABEL software.version="${VIRULENCEFINDER_VER}"
LABEL description="Tool for identifying the virulence genes in E. coli, Enterococcus, Staphylococcus aureus, & Listeria from reads or assemblies"
LABEL website="https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/"
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

# download VIRULENCEFINDER database using a specific commit hash to aid in reproducibility
# index database w/ kma
# NOTE: files HAVE to go into '/database' since that is the default location expected by serotyperfinder.py
# dos2unix on the FASTA files to ensure they have LF line endings
RUN mkdir /database && \
 git clone https://bitbucket.org/genomicepidemiology/virulencefinder_db.git /database && \
 cd /database && \
 git checkout ${VIRULENCEFINDER_DB_COMMIT_HASH} && \
 dos2unix *.fsa && \
 python3 INSTALL.py kma_index

# install virulencefinder to specific tag/version; make /data
RUN git clone --branch ${VIRULENCEFINDER_VER} https://bitbucket.org/genomicepidemiology/virulencefinder.git && \
 mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="/virulencefinder:${PATH}" \
 LC_ALL=C.UTF-8

# set final working directory for production docker image (app layer only)
WORKDIR /data

# default command is to pull up help options for virulencefinder
CMD [ "virulencefinder.py", "-h"]

### START OF TEST STAGE ###
FROM app as test

# set working directory for test layer
WORKDIR /test

# download an example assembly; test with VirulenceFinder
# Escherichia coli complete genome (Unicycler assembly)
# GenBank Nucleotide entry: https://www.ncbi.nlm.nih.gov/nuccore/CP113091.1/
# BioSample:SAMN08799860
RUN mkdir -v /test/asm-input && \
 wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
 gunzip GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
 virulencefinder.py -i /test/GCA_012224845.2_ASM1222484v2_genomic.fna -x -o /test/asm-input && \
 cat /test/asm-input/results_tab.tsv

# download Illumina reads for the same sample ^ and test reads as input into VirulenceFinder
RUN mkdir /test/reads-input && \
 wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_1.fastq.gz && \
 virulencefinder.py -i SRR6903006_1.fastq.gz -mp kma -x -o /test/reads-input && \
 cat /test/reads-input/results_tab.tsv

# test using FASTA supplied with VirulenceFinder code; print help options
# expect to see hits to astA and 2 stx genes; unfortunately it finds astA and 3 stx genes (that don't match)
# issue created here: https://bitbucket.org/genomicepidemiology/virulencefinder/issues/11/test-results-do-not-match-expected-results
RUN cd /virulencefinder/test && \
 virulencefinder.py -i test.fsa -o . -mp blastn -x -q && \
 virulencefinder.py --help

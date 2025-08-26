ARG VIRULENCEFINDER_VER="3.2.0"
ARG VIRULENCEFINDER_DB_VER="4ad9c8dd6eb4adedc99c03f46796e5f5c225b004"
# Database sometimes is not properly versioned, so using most recent commit made on 2025-07-04
# see here: https://bitbucket.org/genomicepidemiology/virulencefinder_db/commits/

FROM staphb/kma:1.5.2 AS kma

FROM ubuntu:jammy AS app

# re-instantiating for use in the app layer
ARG VIRULENCEFINDER_VER
ARG VIRULENCEFINDER_DB_VER
ARG KMA_VER

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="VirulenceFinder"
LABEL software.version="${VIRULENCEFINDER_VER}"
LABEL description="Tool for identifying the virulence genes in E. coli, Enterococcus, Staphylococcus aureus, & Listeria from reads or assemblies"
LABEL website="https://bitbucket.org/genomicepidemiology/virulencefinder"
LABEL license="https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"

# install dependencies; cleanup apt garbage 
# ncbi-blast+ v2.12.0 (ubuntu:jammy), min required version is 2.8.1
# python3 v3.10.12, min required version is 3.10
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    ncbi-blast+ \
    python3-pip \
    git \
    python-is-python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 10

COPY --from=kma /usr/local/bin/*    /usr/local/bin/

# download VIRULENCEFINDER database
# index database w/ kma
# NOTE: files HAVE to go into '/database' since that is the default location expected by virulencefinder
RUN mkdir /database && \
    wget https://git@bitbucket.org/genomicepidemiology/virulencefinder_db/get/${VIRULENCEFINDER_DB_VER}.tar.gz && \
    tar -C /database --strip-components=1 -xvf ${VIRULENCEFINDER_DB_VER}.tar.gz && \
    rm ${VIRULENCEFINDER_DB_VER}.tar.gz && \
    cd /database && \
    python3 INSTALL.py kma_index non_interactive

# install virulencefinder to specific tag/version; make /data
RUN pip3 install --no-cache-dir virulencefinder==${VIRULENCEFINDER_VER} && \
    mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="/virulencefinder:${PATH}" \
    LC_ALL=C.UTF-8 \
    CGE_BLASTN=/usr/bin/blastn \
    CGE_VIRULENCEFINDER_DB=/database

# set final working directory for production docker image (app layer only)
WORKDIR /data

# default command is to pull up help options for virulencefinder
CMD [ "python", "-m", "virulencefinder", "-h" ]

### START OF TEST STAGE ###
FROM app AS test

ARG VIRULENCEFINDER_VER

RUN python -m virulencefinder -h

# set working directory for test layer
WORKDIR /test

# download an example assembly; test with VirulenceFinder
# Escherichia coli complete genome (Unicycler assembly)
# GenBank Nucleotide entry: https://www.ncbi.nlm.nih.gov/nuccore/CP113091.1/
# BioSample:SAMN08799860
RUN mkdir asm-input && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
    gunzip GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
    python -m virulencefinder -h && \
    which blastn && \
    head -n 5 /test/GCA_012224845.2_ASM1222484v2_genomic.fna && \
    python -m virulencefinder -ifa /test/GCA_012224845.2_ASM1222484v2_genomic.fna --extended_output -o asm-input && \
    ls asm-input && \
    cat asm-input/results_tab.tsv

# download Illumina reads for the same sample ^ and test reads as input into VirulenceFinder
RUN mkdir /test/reads-input && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_2.fastq.gz && \
    python -m virulencefinder -ifq SRR6903006_1.fastq.gz SRR6903006_2.fastq.gz --extended_output -o /test/reads-input && \
    cat /test/reads-input/results_tab.tsv

# test using FASTA supplied with VirulenceFinder code; print help options
# expect to see hits to astA and 2 stx genes; unfortunately it finds astA and 3 stx genes (that don't match)
# issue created here: https://bitbucket.org/genomicepidemiology/virulencefinder/issues/11/test-results-do-not-match-expected-results
RUN wget https://git@bitbucket.org/genomicepidemiology/virulencefinder/get/${VIRULENCEFINDER_VER}.tar.gz && \
    tar -xvf ${VIRULENCEFINDER_VER}.tar.gz && \
    mv genomicepidemiology-virulencefinder-* virulencefinder

RUN cd virulencefinder/tests && \
    python -m virulencefinder -ifa data/test.fsa -o . && \
    ls

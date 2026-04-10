FROM python:3.12-slim AS app

ARG MLST_VER="2.33.0"
# mlst requires any2fasta 0.6.0 or higher: https://github.com/tseemann/mlst/blob/master/environment.yml
ARG ANY2FASTA_VER="0.8.1"
# mlst requires blast 2.16.0 or higher
ARG BLAST_VER="2.17.0"
ARG MLSTDB_VER="1.1.1"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="mlst"
LABEL software.version="${MLST_VER}}"
LABEL description="Scan contig files against traditional PubMLST typing schemes."
LABEL website="https://github.com/tseemann/mlst"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL maintainer="Inês Mendes"
LABEL maintainer.email="ines.mendes@theiagen.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Raheel Ahmed"
LABEL maintainer3.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    libmoo-perl \
    liblist-moreutils-perl \
    libjson-perl \
    libfile-which-perl \
    bioperl \
    gzip \
    file \
    procps \
    zlib1g \
    libgomp1 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get any2fasta; move binary to /usr/local/bin which is already in $PATH
RUN wget -q https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VER}.tar.gz && \
    tar -xzf v${ANY2FASTA_VER}.tar.gz && \
    rm -v v${ANY2FASTA_VER}.tar.gz && \
    chmod -v +x any2fasta-${ANY2FASTA_VER}/any2fasta && \
    mv -v any2fasta-${ANY2FASTA_VER}/any2fasta /usr/local/bin

# install blast; soft link all binaries to /usr/local/bin
RUN wget -q https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    rm -v ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    ln -vs /ncbi-blast-${BLAST_VER}+/bin/* /usr/local/bin/

# get mlst
RUN wget -q https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz && \
    tar -xzf v${MLST_VER}.tar.gz && \
    rm -v v${MLST_VER}.tar.gz

# get mlstdb
RUN pip install https://github.com/MDU-PHL/mlstdb/archive/refs/tags/v${MLSTDB_VER}.tar.gz

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:" \
LC_ALL=C.UTF-8

# check dependencies and list available schemes
RUN mlst --check && mlst --list

RUN mlstdb --help && mlstdb --version

WORKDIR /data

# default command is to pull up help options; can be overridden of course
CMD ["mlst", "--help"]




FROM app AS test

ARG MLST_VER
# EXE is a variable used in bats tests, see: https://github.com/tseemann/mlst/blob/master/.github/workflows/CI.yml
ARG EXE="bin/barrnap --threads 4"

# Create custom database directory
RUN mkdir -p /opt/custom_mlst/pubmlst

# Unfortunately, Providencia stuartii entries have been gated behind PubMLST's API. 
# I generated the following pubmlst and blast folders using mlstdb update --input pstuartii_scheme.tab as needed for the following test #3.
# Copy the pre-built mlstdb directories
COPY pubmlst/ /opt/mlst_data/pubmlst/
COPY blast/ /opt/mlst_data/blast/

RUN apt-get update && apt-get install -y --no-install-recommends \
 git && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN mlst --help && mlst --version
 
RUN mlstdb --help && mlstdb --version

 # install (recent version of) bats for testing framework since version in apt for ubuntu:jammy does not include the bats "--abort" option
RUN git clone https://github.com/bats-core/bats-core.git && \
cd bats-core && \
./install.sh /usr/local

# run mlst's own test suite via bats
RUN cd /mlst-${MLST_VER}/ && \
bats -T --abort test/test.sh

# downloading an E. coli (from CT) with a known newer sequence type ST15199 which was designated on 2023-10-16
# MLST scheme info here (from Enterobase): https://pubmlst.org/bigsdb?page=profileInfo&db=pubmlst_escherichia_seqdef&scheme_id=1&profile_id=15199
# E. coli genome: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_032604515.1/
# BioSample: SAMN37796909
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/032/604/515/GCA_032604515.1_PDT001925635.1/GCA_032604515.1_PDT001925635.1_genomic.fna.gz &&\
    gunzip GCA_032604515.1_PDT001925635.1_genomic.fna.gz &&\
    mlst --scheme ecoli_achtman_4 GCA_032604515.1_PDT001925635.1_genomic.fna | tee Ecoli.tsv && \
    echo "Checking for ST15199 in the mlst results now..." && \
    grep "15199" Ecoli.tsv

# Test for Serretia scheme (ST349)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/065/325/GCF_001065325.1_ASM106532v1/GCF_001065325.1_ASM106532v1_genomic.fna.gz &&\
    gunzip GCF_001065325.1_ASM106532v1_genomic.fna.gz &&\
    mlst GCF_001065325.1_ASM106532v1_genomic.fna | tee Serretia.tsv && \
    echo "Checking for ST349 in the Serretia results now..." && \
    grep '349' Serretia.tsv

# Providencia stuartii (ST19 by Providencia spp. scheme, ST15 by P. stuartii scheme)
# checking both typical TSV output and JSON output for expected ST19 and ST 15 results
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/558/855/GCF_001558855.2_ASM155885v2/GCF_001558855.2_ASM155885v2_genomic.fna.gz &&\
    gunzip GCF_001558855.2_ASM155885v2_genomic.fna.gz && \
    mlst --scheme providencia GCF_001558855.2_ASM155885v2_genomic.fna | tee Providencia.tsv && \
    echo "Checking for ST19 in the Providencia results TSV now..." && \
    grep '19' Providencia.tsv && \
    mlst --datadir /opt/mlst_data/pubmlst \
    --blastdb /opt/mlst_data/blast/mlst.fa \
    --scheme pstuartii GCF_001558855.2_ASM155885v2_genomic.fna --json out.json && \
    echo "Checking JSON output for ST15 in the Pstuartii results JSON now..." && \
    grep '"sequence_type" : "15"' out.json

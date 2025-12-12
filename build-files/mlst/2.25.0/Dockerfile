FROM ubuntu:jammy AS app

ARG MLST_VER="2.25.0"
ARG ANY2FASTA_VER="0.4.2"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="mlst"
LABEL software.version="${MLST_VER}"
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL website="https://github.com/tseemann/mlst"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL maintainer="Inês Mendes"
LABEL maintainer.email="ines.mendes@theiagen.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install dependencies via apt; cleanup apt garbage
# blast from ubuntu:jammy is v2.12.0 (as of 2023-07-05)
# deps needed specifically for db download scripts: libfile-which-perl, curl, parallel
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 gzip \
 file \
 ncbi-blast+ \
 libfile-which-perl \
 parallel \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get any2fasta; move binary to /usr/local/bin which is already in $PATH
RUN echo "Downloading and installing any2fasta v${ANY2FASTA_VER}..." && \
wget -q https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VER}.tar.gz && \
tar xzf v${ANY2FASTA_VER}.tar.gz && \
rm -v v${ANY2FASTA_VER}.tar.gz && \
chmod +x any2fasta-${ANY2FASTA_VER}/any2fasta && \
mv -v any2fasta-${ANY2FASTA_VER}/any2fasta /usr/local/bin

# get mlst
RUN echo "Downloading and installing mlst v${MLST_VER}..." && \
wget -q https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz && \
tar -xzf v${MLST_VER}.tar.gz && \
rm -v v${MLST_VER}.tar.gz

# add providencia scheme
COPY ./providencia/ /mlst-${MLST_VER}/db/pubmlst/providencia/

RUN echo "providencia\tProvidencia" >> /mlst-${MLST_VER}/db/scheme_species_map.tab && \
echo "Contents of /mlst-${MLST_VER}/db/scheme_species_map.tab after adding Providencia scheme:" && \
cat /mlst-${MLST_VER}/db/scheme_species_map.tab && \
echo "Now building blast db for all pubMLST schemes included..." && \
./mlst-${MLST_VER}/scripts/mlst-make_blast_db

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:" \
    LC_ALL=C.UTF-8

# check dependencies and list available schemes
RUN mlst --check && mlst --list

WORKDIR /data

# default command is to pull up help options; can be overridden of course
CMD ["mlst", "--help"]

### start of test stage ###
# using app stage as base image for test stage
FROM app AS test

# copy in test script; run script
# test commands stolen shamelessly from https://github.com/tseemann/mlst/blob/master/.travis.yml
COPY mlst-tests.sh .
RUN bash mlst-tests.sh

# downloading an E. coli (from CT) with a known newer sequence type ST15199 which was designated on 2023-10-16
# MLST scheme info here (from Enterobase): https://pubmlst.org/bigsdb?page=profileInfo&db=pubmlst_escherichia_seqdef&scheme_id=1&profile_id=15199
# E. coli genome: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_032604515.1/
# BioSample: SAMN37796909
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/032/604/515/GCA_032604515.1_PDT001925635.1/GCA_032604515.1_PDT001925635.1_genomic.fna.gz &&\
    gunzip GCA_032604515.1_PDT001925635.1_genomic.fna.gz &&\
    mlst GCA_032604515.1_PDT001925635.1_genomic.fna | tee Ecoli.tsv && \
    echo "Checking for ST15199 in the mlst results now..." && \
    grep "15199" Ecoli.tsv

# Test for Serretia scheme (ST349)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/065/325/GCF_001065325.1_ASM106532v1/GCF_001065325.1_ASM106532v1_genomic.fna.gz &&\
    gunzip GCF_001065325.1_ASM106532v1_genomic.fna.gz &&\
    mlst GCF_001065325.1_ASM106532v1_genomic.fna | tee Serretia.tsv && \
    echo "Checking for ST349 in the Serretia results now..." && \
    grep '349' Serretia.tsv

# Providencia (ST19)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/558/855/GCF_001558855.2_ASM155885v2/GCF_001558855.2_ASM155885v2_genomic.fna.gz &&\
    gunzip GCF_001558855.2_ASM155885v2_genomic.fna.gz &&\
    mlst GCF_001558855.2_ASM155885v2_genomic.fna | tee Providencia.tsv

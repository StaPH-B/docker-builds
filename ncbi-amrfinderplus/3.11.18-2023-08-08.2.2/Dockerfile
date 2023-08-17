FROM ubuntu:jammy as app

ARG AMRFINDER_VER="3.11.18"
ARG AMRFINDER_DB_VER="2023-08-08.2"
ARG BLAST_VER="2.14.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version="${AMRFINDER_VER}"
LABEL description="NCBI resistance gene detection tool"
LABEL website="https://github.com/ncbi/amr"
LABEL license="https://github.com/ncbi/amr/blob/master/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Anders Goncalves da Silva"
LABEL maintainer3.email="andersgs@gmail.com"
LABEL maintainer4="Erin Young"
LABEL maintainer4.email="eriny@utah.gov"
LABEL maintainer5="Holly McQueary"
LABEL maintainer5.email="holly.c.mcqueary@mass.gov"

# ncbi-blast+ installed via apt is v2.12.0 - DISABLING so that we can manually install v2.14.0
# see here for reason why I'm manualy installing 2.14.0 instead of using apt-get: https://github.com/ncbi/amr/releases/tag/amrfinder_v3.11.8

# hmmer installed via apt is v3.3.2
# removed because likely unnecessary since we are not compiling from source: make g++
# libgomp1 required for makeblastdb
RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  wget \ 
  curl \
  libgomp1 \
  hmmer \
  procps \
  gzip && \
  apt-get autoclean && \
  rm -rf /var/lib/apt/lists/*

# download and install amrfinderplus pre-compiled binaries; make /data
RUN mkdir amrfinder && cd /amrfinder && \
  wget https://github.com/ncbi/amr/releases/download/amrfinder_v${AMRFINDER_VER}/amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
  tar zxf amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
  rm amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
  mkdir /data

# install ncbi-blast linux binaries
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  rm -v ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz

# set PATH and locale settings for singularity compatibiliity, set amrfinder and manually-installed blast as higher priority in PATH
ENV PATH="/amrfinder:/ncbi-blast-${BLAST_VER}+/bin:$PATH" \
  LC_ALL=C

# download databases and index them
# done in this manner to pin the database version instead of pulling the latest version with `amrfinder -u` 
# softlink is required for `amrfinder -l` and typical `amrfinder` use cases to work properly
RUN mkdir -p /amrfinder/data/${AMRFINDER_DB_VER} && \
  wget -q -P /amrfinder/data/${AMRFINDER_DB_VER} ftp://ftp.ncbi.nlm.nih.gov/pathogen/Antimicrobial_resistance/AMRFinderPlus/database/3.11/${AMRFINDER_DB_VER}/* && \
  amrfinder_index /amrfinder/data/${AMRFINDER_DB_VER} && \
  ln -s /amrfinder/data/${AMRFINDER_DB_VER} /amrfinder/data/latest

# set final working directory
WORKDIR /data

# default command is to print help options
CMD [ "amrfinder", "--help" ]

## Test stage
FROM app as test

# list database version and available --organism options
RUN amrfinder -l

# run recommended tests from amrfinder
RUN amrfinder --threads 1 --plus -p /amrfinder/test_prot.fa -g  /amrfinder/test_prot.gff -O Escherichia > test_prot.got && \
  diff /amrfinder/test_prot.expected test_prot.got && \
  amrfinder --threads 1 --plus -n /amrfinder/test_dna.fa -O Escherichia > test_dna.got && \
  diff /amrfinder/test_dna.expected test_dna.got && \
  amrfinder --threads 1 --plus -n /amrfinder/test_dna.fa -p /amrfinder/test_prot.fa -g /amrfinder/test_prot.gff -O Escherichia > test_both.got && \
  diff /amrfinder/test_both.expected test_both.got

# run amrfinder on Salmonella, without and with --organism option
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
  gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz && \
  amrfinder --threads 1 --plus --nucleotide GCA_010941835.1_PDT000052640.3_genomic.fna --output test1.txt && \
  amrfinder --threads 1 --plus --nucleotide GCA_010941835.1_PDT000052640.3_genomic.fna --organism Salmonella --output test2.txt && \
  cat test1.txt test2.txt

# run amrfinder on Klebesiella oxytoca using --organism/-O flag
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/003/812/925/GCA_003812925.1_ASM381292v1/GCA_003812925.1_ASM381292v1_genomic.fna.gz && \
  gzip -d GCA_003812925.1_ASM381292v1_genomic.fna.gz && \
  amrfinder --threads 1 --plus --name GCA_003812925.1 -n GCA_003812925.1_ASM381292v1_genomic.fna  -O Klebsiella_oxytoca -o GCA_003812925.1-amrfinder.tsv 

# test that gunzip is installed
RUN gunzip --help
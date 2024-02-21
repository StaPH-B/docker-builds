# base image
FROM python:3.9-slim as app

ARG STARAMR_VER="0.10.0"
ARG MLST_VER="2.23.0"
ARG ANY2FASTA_VERSION=0.4.2

LABEL base.image="python:3.9-slim"
LABEL dockerfile.version="1"
LABEL software="staramr"
LABEL software.version="${STARAMR_VER}"
LABEL description="staramr scans bacterial genome contigs for AMR genes and plasmids"
LABEL website="https://github.com/phac-nml/staramr"
LABEL license="https://github.com/phac-nml/staramr/blob/master/LICENSE"
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"

# install dependencies via apt; cleanup apt garbage
# ncbi-blast+ is v2.9.0 in ubuntu:focal (as of August 2022)
RUN apt-get update && apt-get install -y --no-install-recommends \
  git \
  wget \
  libmoo-perl \
  liblist-moreutils-perl \
  libjson-perl \
  gzip \
  file \
  ncbi-blast+ \
  procps \
  ca-certificates && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# any2fasta
RUN wget -q https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VERSION}.tar.gz && \
    tar -xvf v${ANY2FASTA_VERSION}.tar.gz && \
    rm v${ANY2FASTA_VERSION}.tar.gz && \
    cd any2fasta-${ANY2FASTA_VERSION} && \
    chmod +x any2fasta

# mlst 
# apt dependencies: wget libmoo-perl liblist-moreutils-perl libjson-perl gzip file
# also requires blast 2.9.0 or greater
RUN wget -q https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz && \
  tar -xzf v${MLST_VER}.tar.gz && \
  rm v${MLST_VER}.tar.gz

# staramr; make /data
RUN wget -q https://github.com/phac-nml/staramr/archive/refs/tags/${STARAMR_VER}.tar.gz && \
  pip install ${STARAMR_VER}.tar.gz && \
  rm -rf ${STARAMR_VER}.tar.gz && \
  mkdir /data

# set $PATH and locale settings for singularity
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:/any2fasta-${ANY2FASTA_VERSION}/" \
    LC_ALL=C 

# update staramr default databases and print db info
RUN staramr db update -d && staramr db info

CMD staramr --help

WORKDIR /data

##### staramr db information in container at time of docker image build #####
# 6.719 resfinder_db_dir              = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/resfinder
# 6.719 resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
# 6.719 resfinder_db_commit           = 97d1fe0cd0a119172037f6bdb29f8a1c7c6e6019
# 6.719 resfinder_db_date             = Sun, 28 Jan 2024 15:59
# 6.719 pointfinder_db_dir            = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/pointfinder
# 6.719 pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
# 6.719 pointfinder_db_commit         = ce3c9aa002e9b57bf07412ae03c8a23ff1a2f95a
# 6.719 pointfinder_db_date           = Mon, 15 Jan 2024 10:24
# 6.719 pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
# 6.719 pointfinder_organisms_valid   = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, salmonella
# 6.719 plasmidfinder_db_dir          = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/plasmidfinder
# 6.719 plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
# 6.719 plasmidfinder_db_commit       = 81c11f4f2209ff12cb74b486bad4c5ede54418ad
# 6.719 plasmidfinder_db_date         = Mon, 04 Dec 2023 13:21
# 6.719 mlst_version                  = 2.23.0
# 6.719 pointfinder_gene_drug_version = 072621.2
# 6.719 resfinder_gene_drug_version   = 072621

FROM app as test

RUN staramr --help && staramr --version

# download the FASTA file for ${GENBANK_ACCESSION} 
# Salmonella Enterica isolate from PHE-UK: https://www.ncbi.nlm.nih.gov/assembly/GCA_010941835.1/
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
  gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz

# run staramr on the second genome mentioned on staramr's documentation; print resulting TSVs
RUN staramr search -o /data/staramr-test-Salmonella \
  --pointfinder-organism salmonella \
  --plasmidfinder-database-type enterobacteriales \
  /data/GCA_010941835.1_PDT000052640.3_genomic.fna

# installing bsdmainutils for installing "column" command
RUN apt-get update && apt-get install -y --no-install-recommends bsdmainutils

# neatly print out resulting/output TSVs
RUN column -t /data/staramr-test-Salmonella/mlst.tsv && echo && \
  column -t /data/staramr-test-Salmonella/pointfinder.tsv && echo && \
  column -t /data/staramr-test-Salmonella/plasmidfinder.tsv && echo && \
  column -t /data/staramr-test-Salmonella/resfinder.tsv && echo && \
  column -t /data/staramr-test-Salmonella/detailed_summary.tsv && echo && \
  column -t /data/staramr-test-Salmonella/summary.tsv

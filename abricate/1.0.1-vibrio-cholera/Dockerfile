ARG ABRICATE_VER="1.0.1"

FROM ubuntu:focal as app

# For easy upgrade later. ARG varibles only persist during docker image build time
ARG ABRICATE_VER
ARG ANY2FASTA_VERSION="0.4.2"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Abricate"
LABEL software.version="1.0.1"
LABEL description="Mass screening of contigs for AMR or virulence genes"
LABEL website="https://github.com/tseemann/abricate"
LABEL license="https://github.com/tseemann/abricate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"
LABEL maintainer2="Inês Mendes"
LABEL maintainer2.email="ines.mendes@theiagen.com"

# install dependencies
# removed: emboss
# ncbi-blast+ version in apt for ubuntu:focal = v2.9.0 
RUN apt-get update && apt-get install -y --no-install-recommends \
  bioperl \
  gzip \
  unzip \
  liblist-moreutils-perl \
  libjson-perl \
  libtext-csv-perl \
  libfile-slurp-perl \
  liblwp-protocol-https-perl \
  libwww-perl \
  libpath-tiny-perl \
  git \
  ncbi-blast+ \
  wget && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get any2fasta
RUN wget https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VERSION}.tar.gz && \
  tar -xvf v${ANY2FASTA_VERSION}.tar.gz && \
  rm v${ANY2FASTA_VERSION}.tar.gz && \
  cd any2fasta-${ANY2FASTA_VERSION} && \
  chmod +x any2fasta && \
  cp any2fasta /usr/local/bin

# download abricate; make /data; check dependencies
RUN wget https://github.com/tseemann/abricate/archive/v${ABRICATE_VER}.tar.gz && \
  tar -zxvf v${ABRICATE_VER}.tar.gz && \
  rm -rf v${ABRICATE_VER}.tar.gz && \
  mkdir /data && \
  /abricate-${ABRICATE_VER}/bin/abricate --check

# set $PATH
# set perl locale settings for singularity compatibility
ENV PATH="/abricate-${ABRICATE_VER}/bin:\
$PATH"\
  LC_ALL=C

# add custom database; rename FASTA file as 'sequences'; index database with --setupdb
COPY vibrio_v1.0.0.fasta /
RUN mkdir -v /abricate-${ABRICATE_VER}/db/vibrio && \
  cp -v /vibrio_v1.0.0.fasta /abricate-${ABRICATE_VER}/db/vibrio/sequences && \
  abricate --setupdb && \
  abricate --list

# final working directory is /data
WORKDIR /data

# testing layer starts here
FROM app as test

# Grab test Vcholerae genome, uncompress, and save to /data
RUN wget -O - https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/083/565/GCA_018083565.2_PDT000793508.2/GCA_018083565.2_PDT000793508.2_genomic.fna.gz \
  | gunzip -c > /data/GCA_018083565.2_PDT000793508.2_genomic.fna

# to ensure this env variable is set in test layer
ARG ABRICATE_VER

# so that the below commands are run with /bin/bash shell and not /bin/sh - needed for bash-specific tricks below
SHELL ["/bin/bash", "-c"]

# tests shamelessly stolen and modified from: https://github.com/tseemann/abricate/blob/master/.travis.yml
RUN set -x && \
cd /abricate-${ABRICATE_VER}/ && \
abricate --version && \
abricate --help && \
abricate --check && \
abricate --list && \
! abricate --doesnotexist  && \
! abricate --threads 0 && \
! (abricate test/assembly.fa | grep '~~~') && \
abricate test/assembly.fa > 1.tab && \
abricate test/assembly.fa.gz > 2.tab && \
abricate test/assembly.gbk > 3.tab && \
abricate test/assembly.gbk.gz > 4.tab && \
abricate --nopath test/assembly.gbk.gz | grep '^assembly.gbk.gz' && \
abricate --summary {1,2,3,4}.tab > summary.tab && \
abricate --summary 1.tab 2.tab 1.tab 2>&1 | grep 'duplicate' && \
abricate --summary <(cat 1.tab 2.tab 3.tab) | wc -l | grep -w 4 && \
abricate test/assembly.txt |& grep ERROR && \
abricate not_exist.embl |& grep ERROR && \
abricate --threads `nproc` test/assembly.fa.bz2 | grep -i FOSFOMYCIN && \
abricate --threads `nproc` test/assembly.fa.bz2 | grep -i lactam && \
for DB in `abricate --list | cut -f1 | tail -n +2`; do abricate --db ${DB} test/assembly.fa > /dev/null ; done && \
abricate-get_db --help && \
abricate-get_db --db ncbi --dbdir . && \
! grep 'FUSIDIC ACID' ncbi/sequences && \
abricate --threads `nproc` --fofn test/fofn.txt

# vibrio-specific abricate test
# grep to find the 5 expected genes in the output TSV; error if not found
RUN abricate --db vibrio /data/GCA_018083565.2_PDT000793508.2_genomic.fna | tee /data/abricate_vibrio.tsv && \
  echo && \
  echo "grepping for expected genes in abricate output now..." && \
  grep 'ctxA' /data/abricate_vibrio.tsv && \
  grep 'toxR' /data/abricate_vibrio.tsv && \
  grep 'tcpA_ElTor' /data/abricate_vibrio.tsv && \
  grep 'ompW' /data/abricate_vibrio.tsv && \
  grep 'wbeN_O1' /data/abricate_vibrio.tsv
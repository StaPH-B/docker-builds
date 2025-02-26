FROM ubuntu:jammy as app

ARG KAPTIVE_VER="2.0.8"
# note: blast version 2.15 causes errors
ARG blastVer="2.3.0"
ARG VP_GENOMOSEROTYPING_VER="1.0"
# so that apt doesn't try to ask for user input
ARG BIOPYTHON_VER="1.81"

ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Kaptive"
LABEL software.version="${KAPTIVE_VER}"
LABEL description="Report information about surface polysaccharide loci for Klebsiella pneumoniae species complex and Acinetobacter baumannii genome assemblies"
LABEL website="https://github.com/klebgenomics/Kaptive/"
LABEL license="https://github.com/klebgenomics/Kaptive/blob/master/LICENSE"
LABEL website.VPdatabase="https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping"
LABEL license.VPdatabase="https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping/blob/main/LICENSE"
LABEL maintainer="Tamas Stirling"
LABEL maintainer.email="stirling.tamas@gmail.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

# install some dependencies via apt; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
  locales \
  python3 \
  python3-pip \
  python3-setuptools \
  software-properties-common \
  wget \
  ca-certificates \
  procps \
  unzip && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# set locale
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# ncbi-blast+
RUN wget -q ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
  tar -zxpf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
  rm -v ncbi-blast-${blastVer}+-x64-linux.tar.gz

# kaptive
RUN wget -q https://github.com/klebgenomics/Kaptive/archive/refs/tags/v${KAPTIVE_VER}.tar.gz && \
  tar -xzf v${KAPTIVE_VER}.tar.gz && \
  rm -vf v${KAPTIVE_VER}.tar.gz && \
  mv -v /Kaptive-${KAPTIVE_VER} /kaptive

# install biopython globally via system pip
RUN pip3 install biopython==${BIOPYTHON_VER}

# download Vibrio parahemolyticus database; rename directory to static location
RUN wget -q https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping/archive/refs/tags/${VP_GENOMOSEROTYPING_VER}.tar.gz && \
  tar -xzf ${VP_GENOMOSEROTYPING_VER}.tar.gz && \
  rm -v ${VP_GENOMOSEROTYPING_VER}.tar.gz && \
  mv -v vibrio_parahaemolyticus_genomoserotyping-${VP_GENOMOSEROTYPING_VER}/*gbk /kaptive/reference_database/. && \
  rm -rf vibrio_parahaemolyticus_genomoserotyping-${VP_GENOMOSEROTYPING_VER}

# set $PATH, with /kaptive at the highest priority
ENV PATH="/kaptive:/ncbi-blast-${blastVer}+/bin:${PATH}"

# final working directory is /data
WORKDIR /data

# default command is to print help options
CMD [ "kaptive.py", "--help"]

# test layer
FROM app as test

WORKDIR /test1

# test with A. baumannii; testing both k and o locus
RUN echo "downloading an A. baumannii genome & testing Kaptive..." && \
  wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/486/705/GCA_016486705.1_PDT000751301.1/GCA_016486705.1_PDT000751301.1_genomic.fna.gz && \
  gzip -d GCA_016486705.1_PDT000751301.1_genomic.fna.gz && \
  kaptive.py -a GCA_016486705.1_PDT000751301.1_genomic.fna -k /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk  -o /test1/Abaum && \
  kaptive.py -a GCA_016486705.1_PDT000751301.1_genomic.fna -k /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk -o /test1/Abaum

WORKDIR /test2

# test with K. pneumoniae; testing both k and o locus
RUN echo "downloading an K. pneumoniae genome & testing Kaptive..." && \
  wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/022/268/055/GCA_022268055.1_PDT000434809.1/GCA_022268055.1_PDT000434809.1_genomic.fna.gz && \
  gzip -d GCA_022268055.1_PDT000434809.1_genomic.fna.gz && \
  kaptive.py -a GCA_022268055.1_PDT000434809.1_genomic.fna -k /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk -o /test2/kpneu && \
  kaptive.py -a GCA_022268055.1_PDT000434809.1_genomic.fna -k /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk -o /test2/kpneu

WORKDIR /test3

### test with at 2 Vibrio parahaemolyticus genomes with a known serotype. These 2 are pulled from the publication describing custom database ##
# GCA_001558495.2 - expect OL1 and KL1
# GCA_001728135.1 - expect OL4 KL53
# more info on test genome here: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_001558495.2/
# strain: ATCC17802
# more info on 2nd test genome here: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_001728135.1/
# strain: CDC_K5009W
RUN echo "downloading an 2 V. parahaemolyticus genomes & testing Kaptive..." && \
  wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/558/495/GCF_001558495.2_ASM155849v2/GCF_001558495.2_ASM155849v2_genomic.fna.gz && \
  wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/728/135/GCF_001728135.1_ASM172813v1/GCF_001728135.1_ASM172813v1_genomic.fna.gz && \
  gzip -d GCF_001558495.2_ASM155849v2_genomic.fna.gz && \
  gzip -d GCF_001728135.1_ASM172813v1_genomic.fna.gz && \
  kaptive.py -a *.fna -k /kaptive/reference_database/VibrioPara_Kaptivedb_K.gbk -o /test3/Vparahaemolyticus && \
  kaptive.py -a *.fna -k /kaptive/reference_database/VibrioPara_Kaptivedb_O.gbk -o /test3/Vparahaemolyticus

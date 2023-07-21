FROM ubuntu:focal as app

ARG KAPTIVE_VER="2.0.7"
ARG blastVer="2.3.0"
ARG VP_GENOMOSEROTYPING_VER="1.0"
# so that apt doesn't try to ask for user input
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
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

# install some dependencies via apt; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
  locales \
  python3 \
  python3-pip \
  python3-setuptools \
  software-properties-common \
  wget \
  ca-certificates \
  procps && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# set locale
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# ncbi-blast+
RUN wget "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz" && \
  tar -zxpf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
  rm -v ncbi-blast-${blastVer}+-x64-linux.tar.gz
 
# kaptive
RUN wget "https://github.com/klebgenomics/Kaptive/archive/refs/tags/v${KAPTIVE_VER}.tar.gz" && \
  tar -xzf v${KAPTIVE_VER}.tar.gz && \
  rm -vf v${KAPTIVE_VER}.tar.gz && \
  mv -v /Kaptive-${KAPTIVE_VER} /kaptive
 
# install biopython globally via system pip
RUN pip3 install biopython

# download Vibrio parahemolyticus database; rename directory to static location
RUN wget https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping/archive/refs/tags/${VP_GENOMOSEROTYPING_VER}.tar.gz && \
tar -xzf ${VP_GENOMOSEROTYPING_VER}.tar.gz && \
rm -v ${VP_GENOMOSEROTYPING_VER}.tar.gz && \
mv -v vibrio_parahaemolyticus_genomoserotyping-${VP_GENOMOSEROTYPING_VER} /vibrio_parahaemolyticus_genomoserotyping

# set $PATH, with /kaptive at the highest priority
ENV PATH="/kaptive:/ncbi-blast-${blastVer}+/bin:${PATH}"

# final working directory is /data
WORKDIR /data

# test layer
FROM app as test

# set working directory as /test for test stage
WORKDIR /test

# install curl and unzip for downloading and unzipping genomes from NCBI
RUN apt-get update && apt-get install --no-install-recommends -y curl unzip

# test with A. baumannii; testing both k and o locus
RUN echo "downloading an A. baumannii genome & testing Kaptive..." && \
mkdir /test/Abaum && \
wget -q -P /test/Abaum "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/486/705/GCA_016486705.1_PDT000751301.1/GCA_016486705.1_PDT000751301.1_genomic.fna.gz" && \
gunzip -qc /test/Abaum/GCA_016486705.1_PDT000751301.1_genomic.fna.gz > /test/Abaum/GCA_016486705.1_PDT000751301.1_genomic.fna && \
kaptive.py -a /test/Abaum/GCA_016486705.1_PDT000751301.1_genomic.fna -k /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk -o /test/Abaum && \
kaptive.py -a /test/Abaum/GCA_016486705.1_PDT000751301.1_genomic.fna -k /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk -o /test/Abaum

# test with K. pneumoniae; testing both k and o locus
RUN echo "downloading an K. pneumoniae genome & testing Kaptive..." && \
mkdir /test/Kpneumo && \
wget -q -P /test/Kpneumo "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/022/268/055/GCA_022268055.1_PDT000434809.1/GCA_022268055.1_PDT000434809.1_genomic.fna.gz" && \
gunzip -qc /test/Kpneumo/GCA_022268055.1_PDT000434809.1_genomic.fna.gz >/test/Kpneumo/GCA_022268055.1_PDT000434809.1_genomic.fna && \
kaptive.py -a /test/Kpneumo/GCA_022268055.1_PDT000434809.1_genomic.fna -k /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk -o /test/Kpneumo && \
kaptive.py -a /test/Kpneumo/GCA_022268055.1_PDT000434809.1_genomic.fna -k /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk -o /test/Kpneumo

### test with at 2 Vibrio parahaemolyticus genomes with a known serotype. These 2 are pulled from the publication describing custom database ##
# GCA_001558495.2 - expect OL1 and KL1
# GCA_001728135.1 - expect OL4 KL53
# more info on test genome here: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_001558495.2/
# strain: ATCC17802
# more info on 2nd test genome here: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_001728135.1/
# strain: CDC_K5009W
RUN echo "downloading an 2 V. parahaemolyticus genomes & testing Kaptive..." && \
curl --silent -OJX GET "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/GCF_001558495.2/download?include_annotation_type=GENOME_FASTA,GENOME_GFF,RNA_FASTA,CDS_FASTA,PROT_FASTA,SEQUENCE_REPORT&filename=GCF_001558495.2.zip" -H "Accept: application/zip" && \
curl --silent -OJX GET "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/GCF_001728135.1/download?include_annotation_type=GENOME_FASTA,GENOME_GFF,RNA_FASTA,CDS_FASTA,PROT_FASTA,SEQUENCE_REPORT&filename=GCF_001728135.1.zip" -H "Accept: application/zip" && \
unzip -q GCF_001558495.2.zip -d GCF_001558495.2 && \
unzip -q GCF_001728135.1.zip -d GCF_001728135.1 && \
mkdir -v /test/Vparahaemolyticus && \
mv -v GCF*/*/*/*/GCF*_genomic.fna /test/Vparahaemolyticus && \
kaptive.py -a /test/Vparahaemolyticus/*.fna -k /vibrio_parahaemolyticus_genomoserotyping/VibrioPara_Kaptivedb_K.gbk -o /test/Vparahaemolyticus && \
kaptive.py -a /test/Vparahaemolyticus/*.fna -k /vibrio_parahaemolyticus_genomoserotyping/VibrioPara_Kaptivedb_O.gbk -o /test/Vparahaemolyticus

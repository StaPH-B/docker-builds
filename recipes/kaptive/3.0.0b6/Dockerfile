FROM ubuntu:jammy AS app

# for easy upgrade later. ARG variables only persist during image build time
ARG MINIMAP2_VER="2.28"
ARG MASH_VER="2.3"
ARG KAPTIVE_VER="3.0.0b6"
ARG VP_GENOMOSEROTYPING_VER="1.0"

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

# install prerequisites. Cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    wget \
    ca-certificates \
    bzip2 \
    procps \
    curl && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# mash; update UID and GID of mash files; make /data
# UID and GID changes because the original owner is UID: 1081147385 and GID: 1360859114 which does NOT play well with systems that limits GIDs and UIDs
RUN wget -q https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
        tar -xvf mash-Linux64-v${MASH_VER}.tar --no-same-owner && \
        rm -rf mash-Linux64-v${MASH_VER}.tar && \
        chown root:root /mash-Linux64-v${MASH_VER}/* 

# install minimap2 binary; make /data
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | \
    tar -jxvf - --no-same-owner

# install kaptive
RUN pip install --no-cache-dir kaptive==${KAPTIVE_VER}

# move databases
RUN wget -q https://github.com/klebgenomics/Kaptive/releases/download/v${KAPTIVE_VER}/kaptive-${KAPTIVE_VER}.tar.gz && \
    tar -vxf kaptive-${KAPTIVE_VER}.tar.gz --no-same-owner && \
    mkdir -p /data /kaptive/ && \
    mv /kaptive-${KAPTIVE_VER}/reference_database /kaptive/reference_database && \
    rm -rf kaptive-${KAPTIVE_VER}.tar.gz kaptive-${KAPTIVE_VER}

# download Vibrio parahemolyticus database; mv gbk files to where the other references are
RUN wget -q https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping/archive/refs/tags/${VP_GENOMOSEROTYPING_VER}.tar.gz && \
    tar -xzf ${VP_GENOMOSEROTYPING_VER}.tar.gz && \
    rm -v ${VP_GENOMOSEROTYPING_VER}.tar.gz && \
    mv -v vibrio_parahaemolyticus_genomoserotyping-${VP_GENOMOSEROTYPING_VER}/*gbk /kaptive/reference_database/. && \
    rm -rf vibrio_parahaemolyticus_genomoserotyping-${VP_GENOMOSEROTYPING_VER}

# set PATH
ENV PATH="/mash-Linux64-v${MASH_VER}:/minimap2-${MINIMAP2_VER}_x64-linux:${PATH}"

# set working directory
WORKDIR /data

# default command is to print help options
CMD [ "kaptive", "--help" ]

# test layer
FROM app AS test

RUN kaptive --help && kaptive --version

WORKDIR /test1

# test with A. baumannii; testing both k and o locus
RUN echo "downloading an A. baumannii genome & testing Kaptive..." && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/486/705/GCA_016486705.1_PDT000751301.1/GCA_016486705.1_PDT000751301.1_genomic.fna.gz && \
    gzip -d GCA_016486705.1_PDT000751301.1_genomic.fna.gz && \
    kaptive assembly /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk GCA_016486705.1_PDT000751301.1_genomic.fna -o abau_k.txt && head abau_k.txt && \
    kaptive assembly /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk GCA_016486705.1_PDT000751301.1_genomic.fna -o abau_oc.txt && head abau_oc.txt

WORKDIR /test2
# test with K. pneumoniae; testing both k and o locus
RUN echo "downloading an K. pneumoniae genome & testing Kaptive..." && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/022/268/055/GCA_022268055.1_PDT000434809.1/GCA_022268055.1_PDT000434809.1_genomic.fna.gz && \
    gzip -d GCA_022268055.1_PDT000434809.1_genomic.fna.gz && \
    kaptive assembly /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk GCA_022268055.1_PDT000434809.1_genomic.fna -o kpneu_k.txt && \
    kaptive assembly /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk GCA_022268055.1_PDT000434809.1_genomic.fna -o kpneu_o.txt && \
    head kpneu_k.txt kpneu_o.txt

WORKDIR /test3
# test with recommended usage in documentatation
RUN echo "downloading an K. pneumoniae genome & testing Kaptive..." && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/022/268/055/GCA_022268055.1_PDT000434809.1/GCA_022268055.1_PDT000434809.1_genomic.fna.gz && \
    gzip -d GCA_022268055.1_PDT000434809.1_genomic.fna.gz && \
    kaptive assembly kpsc_k assemblies/*.fna -o kaptive_results.tsv && \
    head kaptive_results.tsv

WORKDIR /test4

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
    kaptive assembly /kaptive/reference_database/VibrioPara_Kaptivedb_K.gbk *.fna -o Vparahaemolyticus_K.txt && \
    kaptive assembly /kaptive/reference_database/VibrioPara_Kaptivedb_O.gbk *.fna -o Vparahaemolyticus_O.txt && \
    head Vparahaemolyticus_K.txt Vparahaemolyticus_O.txt
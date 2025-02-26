FROM ubuntu:xenial as app

# for easy upgrade later. ARG variables only persist during build time.
ARG SKAVER="1.0"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="SKA"
LABEL software.version="1.0"
LABEL description="Split Kmer Analysis Toolkit"
LABEL website="https://github.com/simonrharris/SKA"
LABEL license="https://github.com/simonrharris/SKA/blob/master/LICENSE"
LABEL maintainer="Holly Halstead"
LABEL maintainer.email="holly.halstead@doh.wa.gov"

# install dependencies and cleanup apt garbage
RUN apt-get update && apt-get -y --no-install-recommends install \
 wget \
 unzip \
 ca-certificates \
 zlib1g-dev \
 make \
 g++ \
 unzip \
 python3=3.5.1-3 \
 rsync && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean


# DL SKA, unpack, and install
RUN wget https://github.com/simonrharris/SKA/archive/v${SKAVER}.tar.gz && \
 tar -xzf v${SKAVER}.tar.gz && \
 rm -rf v${SKAVER}.tar.gz && \
 ls && \
 mv SKA-${SKAVER} SKA && \
 cd SKA && \
 make && \
 make install && \
 mkdir /data


WORKDIR /data

COPY generate_ska_alignment.py .

FROM app as test


RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/815/GCF_000195815.1_ASM19581v1/GCF_000195815.1_ASM19581v1_genomic.fna.gz && \
gunzip GCF_000195815.1_ASM19581v1_genomic.fna.gz && \
mv GCF_000195815.1_ASM19581v1_genomic.fna cdip_reference.fasta && \

wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/014/826/095/GCF_014826095.1_ASM1482609v1/GCF_014826095.1_ASM1482609v1_genomic.fna.gz && \
gunzip GCF_014826095.1_ASM1482609v1_genomic.fna.gz && \

wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/843/135/GCF_002843135.1_ASM284313v1/GCF_002843135.1_ASM284313v1_genomic.fna.gz && \
gunzip GCF_002843135.1_ASM284313v1_genomic.fna.gz && \

for f in *fna; do echo "${f%.fna}    ${f}"; done > input_list.txt && \

python3 generate_ska_alignment.py --reference cdip_reference.fasta --fasta input_list.txt --out cdip.aln && \
ls cdip.aln && \
ska --version

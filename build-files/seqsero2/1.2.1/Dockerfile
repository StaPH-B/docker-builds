FROM ubuntu:bionic as app

# for easy upgrade later. ARG variables only persist during build time
ARG SEQSERO2_VER="1.2.1"
ARG SPADES_VER="3.15.5"
ARG SAMTOOLS_VER="1.9"
ARG SALMID_VER="0.122"

# Metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL software="SeqSero2"
LABEL software.version="1.2.1"
LABEL description="Salmonella serotyping from genome sequencing data"
LABEL website="https://github.com/denglab/SeqSero2"
LABEL license="https://github.com/denglab/SeqSero2/blob/master/LICENSE"
LABEL maintainer1="Jake Garfin"
LABEL maintainer1.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Kelsey Florek"
LABEL maintainer3.email="kelsey.florek@slh.wisc.edu"

# python = 2.7.17
# python3 = 3.6.9
# biopython = 1.73
# bedtools = 2.26.0 
# sra-toolkit = 2.8.2
# bwa = 0.7.17
# ncbi-blast+ = 2.6.0
RUN apt-get update && apt-get install -y --no-install-recommends \
 python3 \
 python3-pip \
 python3-setuptools \
 bwa \
 ncbi-blast+ \
 sra-toolkit \
 bedtools \
 wget \
 ca-certificates \
 unzip \
 zlib1g-dev \
 libbz2-dev \
 liblzma-dev \
 build-essential \
 libncurses5-dev && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install samtools 
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
 tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
 rm -v samtools-${SAMTOOLS_VER}.tar.bz2 && \
 cd samtools-${SAMTOOLS_VER} && \
 ./configure && \
 make && \
 make install

# Install salmID 
RUN wget https://github.com/hcdenbakker/SalmID/archive/${SALMID_VER}.tar.gz && \
 tar -xzf ${SALMID_VER}.tar.gz && \
 rm -rvf ${SALMID_VER}.tar.gz

# install SPAdes binary
RUN wget http://cab.spbu.ru/files/release${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm -rv SPAdes-${SPADES_VER}-Linux.tar.gz

# Install SeqSero2; make /data
RUN wget https://github.com/denglab/SeqSero2/archive/v${SEQSERO2_VER}.tar.gz && \
 tar -xzf v${SEQSERO2_VER}.tar.gz && \
 rm -vrf v${SEQSERO2_VER}.tar.gz && \
 cd /SeqSero2-${SEQSERO2_VER}/ && \
 python3 -m pip install . && \
 mkdir /data

# PATH edited to include /SeqSero2-1.1.0/bin in previous python3 command
ENV PATH="${PATH}:/SPAdes-${SPADES_VER}-Linux/bin:/SalmID-${SALMID_VER}:/samtools-${SAMTOOLS_VER}" \
    LC_ALL=C

WORKDIR /data

FROM app as test

WORKDIR /test

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

# download an example assembly; test with SeqSero2
# Salmonella enterica serovar Infantis genome: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCA_007765495.1/
# BioSample:SAMN07684583
ARG GENBANK_ACCESSION="GCA_007765495.1"
RUN datasets download genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
    mkdir -v ${GENBANK_ACCESSION}-download && \
    unzip ${GENBANK_ACCESSION}.zip -d ${GENBANK_ACCESSION}-download && \
    rm ${GENBANK_ACCESSION}.zip && \
    mv -v ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}*.fna ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna && \
    SeqSero2_package.py \
      -i ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna \
      -t 4 \
      -m k \
      -d ${GENBANK_ACCESSION}-seqsero2-assembly-kmer-mode \
      -n ${GENBANK_ACCESSION} \
      -p 2 && \
    grep 'Infantis' ${GENBANK_ACCESSION}-seqsero2-assembly-kmer-mode/SeqSero_result.txt

# testing reads as input for the same Salmonella isolate
# specifically the "allele" mode which does micro assembly first using SPAdes
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_2.fastq.gz && \
    SeqSero2_package.py \
      -i SRR6082043_1.fastq.gz SRR6082043_2.fastq.gz \
      -t 2 \
      -m a \
      -d SRR6082043-seqsero2-reads-allele-mode \
      -n SRR6082043 \
      -p 2 && \
    grep 'Infantis' SRR6082043-seqsero2-reads-allele-mode/SeqSero_result.txt

# print help options, check dependencies, print version
RUN SeqSero2_package.py --help && SeqSero2_package.py --check && SeqSero2_package.py --version
# Base Image
FROM ubuntu:xenial

# Metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="emm-typing-tool"
LABEL software.version="0.0.1"
LABEL description="Assign emm type and subtype by querying the CDC M-type specific database "
LABEL website="https://github.com/phe-bioinformatics/emm-typing-tool"
LABEL license="https://raw.githubusercontent.com/phe-bioinformatics/emm-typing-tool/master/LICENCE"
LABEL maintainer="Jake Garfin"
LABEL maintainer.email="jake.garfin@state.mn.us"


RUN apt-get update && apt-get install -y \
  python=2.7.12-1~16.04 \
  python-pip=8.1.1-2ubuntu0.4 \
  wget \
  zlib1g-dev \
  ncbi-blast+=2.2.31-4 \
  build-essential \
  libncurses5-dev \
  bzip2 \
  unzip \
  git

# Install bowtie2
RUN wget 'https://downloads.sourceforge.net/project/bowtie-bio/bowtie2/2.2.9/bowtie2-2.2.9-linux-x86_64.zip' && \
  unzip bowtie2-2.2.9-linux-x86_64.zip && \
  rm bowtie2-2.2.9-linux-x86_64.zip
  
# Install samtools
RUN wget 'https://downloads.sourceforge.net/project/samtools/samtools/0.1.19/samtools-0.1.19.tar.bz2' && \
  tar -xvf samtools-0.1.19.tar.bz2 && \
  rm samtools-0.1.19.tar.bz2 && \
  cd samtools-0.1.19 && make && \
  chmod -R 777 /samtools-0.1.19

# Install emboss
RUN wget 'ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz' && \
  tar -xvf EMBOSS-6.6.0.tar.gz && \
  rm EMBOSS-6.6.0.tar.gz && \
  cd EMBOSS-6.6.0/ && \
  ./configure --without-x && make && \
  chmod -R 777 emboss

# Install python packages
RUN pip install --upgrade pip && \
  python -m pip install pyyaml==5.1.2 numpy==1.16.4 lxml==4.4.1 biopython==1.74

# Install PHE emm-typing-tool
RUN git clone https://github.com/phe-bioinformatics/emm-typing-tool.git

# Setup emm database
RUN mkdir /db && cd /db && \
  wget 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/006/785/GCA_000006785.2_ASM678v2/GCA_000006785.2_ASM678v2_genomic.fna.gz' && \
  gunzip GCA_000006785.2_ASM678v2_genomic.fna.gz && \
  mv GCA_000006785.2_ASM678v2_genomic.fna reference.seq && \
  makeblastdb -in reference.seq -dbtype nucl -out reference && \
  wget 'ftp://ftp.cdc.gov/pub/infectious_diseases/biotech/tsemm/trimmed.tfa' && \
  cp /emm-typing-tool/edit_allele_file.sh . && \
  sh edit_allele_file.sh && \
  mkdir /data

ENV PATH="${PATH}:/samtools-0.1.19:/bowtie2-2.2.9:/EMBOSS-6.6.0/emboss:/emm-typing-tool"

WORKDIR /data
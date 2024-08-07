FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during image build
ARG SAMTOOLSVER=1.17
ARG HTSLIBVER=$SAMTOOLSVER
ARG IVARVER=1.4.1

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="iVar"
LABEL software.version=${IVARVER}
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL modified.from="https://github.com/andersen-lab/ivar/blob/master/Dockerfile"
LABEL original.maintainer="Kathik G"
LABEL original.maintainer.email="gkarthik@scripps.edu"

# install dependencies, cleanup apt garbage.
# bedtools version=2.30.0
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  procps \
  autoconf \
  autotools-dev \
  automake \
  zlib1g-dev \
  python3 \
  wget \
  libbz2-dev \
  liblzma-dev \
  libncurses-dev \
  git \
  bedtools \
  python3-pip && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# installing htslib
RUN wget -q https://github.com/samtools/htslib/releases/download/${HTSLIBVER}/htslib-${HTSLIBVER}.tar.bz2 && \
  tar xvf htslib-${HTSLIBVER}.tar.bz2 && \
  rm htslib-${HTSLIBVER}.tar.bz2 && \
  cd htslib-${HTSLIBVER}/ && \
  ./configure && \
  make && \
  make install

# installing samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
  rm samtools-${SAMTOOLSVER}.tar.bz2 && \
  cd samtools-${SAMTOOLSVER} && \
  ./configure && \
  make && \
  make install
  
# installing iVar; make /data
RUN wget -q https://github.com/andersen-lab/ivar/archive/v${IVARVER}.tar.gz && \
  tar -xf v${IVARVER}.tar.gz && \
  rm -rf v${IVARVER}.tar.gz && \
  cd ivar-${IVARVER} && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install && \
  mkdir /data

ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib"

# set /data as working directory
WORKDIR /data

FROM app as test

WORKDIR /test

RUN ivar version && samtools --version

# getting files
RUN wget -q https://github.com/StaPH-B/docker-builds/blob/master/tests/SARS-CoV-2/SRR13957123.sorted.bam?raw=true -O SRR13957123.sorted.bam && \
  samtools view -s 0.25 -b SRR13957123.sorted.bam | samtools sort -o SRR13957123.subsampled.bam - && samtools index SRR13957123.subsampled.bam && \
  wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta -O MN908947.3.fasta && \
  wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.primer.bed && \
  wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_1.fastq.gz?raw=true -O SRR13957123_1.fastq.gz && \
  wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_2.fastq.gz?raw=true -O SRR13957123_2.fastq.gz

# primer trimming
RUN ivar trim -e -i SRR13957123.subsampled.bam -b nCoV-2019.primer.bed -p SRR13957123.primertrim && \
  samtools sort SRR13957123.primertrim.bam -o SRR13957123.primertrim.sorted.bam

# creating a consensus - using smaller -d for github actions
RUN samtools mpileup -A -d 40 -B -Q 0 --reference MN908947.3.fasta SRR13957123.primertrim.sorted.bam | \
  ivar consensus -q 20 -t 0.6 -n N -m 20 -p SRR13957123.consensus && \
  wc -c SRR13957123.consensus*

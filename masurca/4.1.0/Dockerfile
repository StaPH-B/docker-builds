FROM ubuntu:focal as app

ARG MASURCA_VER="4.1.0"
ARG MINIMAP2_VER="2.24"
ARG BWA_VER="0.7.17"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="masurca"
LABEL software.version="${MASURCA_VER}"
LABEL description="Genome Assembly and Analysis"
LABEL website="https://github.com/alekseyzimin/masurca"
LABEL license="https://github.com/alekseyzimin/masurca/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  python \
  build-essential \
  curl \
  wget \
  gcc \
  zlib1g-dev \
  bzip2 \
  libboost-dev \
  libbz2-dev \
  liblzma-dev \
  numactl \
  procps && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf -

# install bwa
RUN mkdir /bwa && \
  cd /bwa && \
  wget https://github.com/lh3/bwa/releases/download/v$BWA_VER/bwa-$BWA_VER.tar.bz2 && \
  tar -xjf bwa-$BWA_VER.tar.bz2 && \
  rm bwa-$BWA_VER.tar.bz2 && \
  cd bwa-$BWA_VER && \
  make

# install masurca suite
RUN mkdir /data && \
  wget https://github.com/alekseyzimin/masurca/releases/download/v$MASURCA_VER/MaSuRCA-$MASURCA_VER.tar.gz && \
  tar -xvf MaSuRCA-$MASURCA_VER.tar.gz && \
  rm MaSuRCA-$MASURCA_VER.tar.gz

WORKDIR /MaSuRCA-$MASURCA_VER

# even in 4.0.9 there's the evil cp at the end of .install.sh
RUN bash /MaSuRCA-$MASURCA_VER/install.sh 2>/dev/null ; exit 0

ENV PATH="${PATH}:/MaSuRCA-${MASURCA_VER}/Flye/bin:/MaSuRCA-${MASURCA_VER}/bin:/minimap2-${MINIMAP2_VER}_x64-linux:/bwa/bwa-${BWA_VER}" \
  LC_ALL=C

# WORKDIR sets working directory
WORKDIR /data

FROM app as test

# testing POLCA
RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
  wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
  wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
  polca.sh -a SRR13957123.consensus.fa -r 'SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz' && \
  test -f SRR13957123.consensus.fa.PolcaCorrected.fa

# testing hybrid assembly
RUN wget -q https://github.com/rrwick/Unicycler/raw/69e712eb95c4b9f8a46aade467260260a9ce7a91/sample_data/short_reads_1.fastq.gz && \
  wget -q https://github.com/rrwick/Unicycler/raw/69e712eb95c4b9f8a46aade467260260a9ce7a91/sample_data/short_reads_2.fastq.gz && \
  wget -q https://github.com/rrwick/Unicycler/raw/69e712eb95c4b9f8a46aade467260260a9ce7a91/sample_data/long_reads_low_depth.fastq.gz && \
  masurca -t 2 -i short_reads_1.fastq.gz,short_reads_2.fastq.gz -r long_reads_low_depth.fastq.gz

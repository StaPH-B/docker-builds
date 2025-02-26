# global arg variables
ARG SHIGATYPER_VER="2.0.5"
ARG SAMTOOLSVER="1.9"
ARG BCFTOOLSVER="1.9"
ARG MINIMAP2_VER="2.24"

### start of builder stage ###
FROM ubuntu:jammy as builder

# re-instantiate these variables
ARG SHIGATYPER_VER
ARG SAMTOOLSVER
ARG BCFTOOLSVER
ARG MINIMAP2_VER

# so that apt doesn't ask for input
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 git \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 zlib1g-dev \
 libssl-dev \
 gcc \
 make \
 python3 \
 python3-setuptools \
 bzip2 \
 gnuplot \
 ca-certificates \
 gawk \
 curl \
 build-essential && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# shigatyper depends on samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
  rm -v samtools-${SAMTOOLSVER}.tar.bz2 && \
  cd samtools-${SAMTOOLSVER} && \
  ./configure && \
  make && \
  make install 

# shigatyper depends on bcftools
RUN wget https://github.com/samtools/bcftools/releases/download/${BCFTOOLSVER}/bcftools-${BCFTOOLSVER}.tar.bz2 && \
  tar -xjf bcftools-${BCFTOOLSVER}.tar.bz2 && \
  rm -v bcftools-${BCFTOOLSVER}.tar.bz2 && \
  cd bcftools-${BCFTOOLSVER} && \
  make && \
  make install

# shigatyper depends on minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxf -

# set the environment
ENV PATH="${PATH}:/minimap2-${MINIMAP2_VER}_x64-linux" \
  LC_ALL=C

### start of app stage ###
# using fresh ubuntu:jammy image as base for app stage
FROM ubuntu:jammy as app

# re-instantiate thes variables
ARG SHIGATYPER_VER
ARG MINIMAP2_VER

# LABELS must be contained in `app` stage to pass the GHActions checks
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="shigatyper"
LABEL software.version="${SHIGATYPER_VER}"
LABEL description="Determine Shigella serotype using Illumina (single or paired-end) or Oxford Nanopore reads!"
LABEL website="https://github.com/CFSAN-Biostatistics/shigatyper"
LABEL license="https://github.com/CFSAN-Biostatistics/shigatyper/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"

# copy in samtools and bcftools executables into app stage
COPY --from=builder /usr/local/bin/* /usr/local/bin

# copy in minimap2 executable into app stage
COPY --from=builder /minimap2-${MINIMAP2_VER}_x64-linux /usr/local/bin

# ensuring samtools & bcftools dependencies are present (dependencies for running tools, not for compiling/installing tools)
RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    zlib1g \
    libncurses5 \
    bzip2 \
    liblzma-dev \
    libcurl4-gnutls-dev \
    python3 \
    python3-setuptools \ 
    wget \
    ca-certificates \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get shigatyper code; install; index fasta file
# FYI - samtools faidx cmd has a * in the path due to version inconsistencies
RUN wget https://github.com/CFSAN-Biostatistics/shigatyper/archive/refs/tags/${SHIGATYPER_VER}.tar.gz && \
  tar -xf ${SHIGATYPER_VER}.tar.gz && \
  rm -v ${SHIGATYPER_VER}.tar.gz && \
  cd shigatyper-${SHIGATYPER_VER} && \
  python3 setup.py install && \
  samtools faidx /usr/local/lib/python3.10/dist-packages/ShigaTyper-*-py3.10.egg/resources/ShigellaRef5.fasta

# ensuring final working directory is /data
WORKDIR /data

# default command is to pull up help options; can be overridden of course
CMD ["shigatyper", "--help"]

### start of test stage ###
# using app stage as base image for test stage
FROM app as test

# fetch test data from ENA FTP
# SRR8186675 = https://www.ncbi.nlm.nih.gov/biosample/SAMN10040549 , expect Shigella boydii serotype 12
# SRR7738178 = https://www.ncbi.nlm.nih.gov/biosample/SAMN09878976 , expect Shigella sonnei (I think Form II?)
# SRR8186651 = https://www.ncbi.nlm.nih.gov/biosample/SAMN10052840 , expect Shigella flexneri serotype 3a
RUN  echo "downloading test FASTQ files from ENA's FTP, please be patient..." && \
  wget -q -P /data ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR818/005/SRR8186675/SRR8186675_1.fastq.gz && \
  wget -q -P /data ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR818/005/SRR8186675/SRR8186675_2.fastq.gz && \
  wget -q -P /data ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR773/008/SRR7738178/SRR7738178_1.fastq.gz && \
  wget -q -P /data ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR773/008/SRR7738178/SRR7738178_2.fastq.gz && \
  wget -q -P /data ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR818/001/SRR8186651/SRR8186651_1.fastq.gz && \
  wget -q -P /data/ ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR818/001/SRR8186651/SRR8186651_2.fastq.gz

# actually run shigatyper on test fastq files; ls to see output filenames
RUN shigatyper --R1 /data/SRR8186675_1.fastq.gz --R2 /data/SRR8186675_2.fastq.gz --name SRR8186675 && \
  shigatyper --R1 /data/SRR7738178_1.fastq.gz --R2 /data/SRR7738178_2.fastq.gz --name SRR7738178 && \
  shigatyper --R1 /data/SRR8186651_1.fastq.gz --R2 /data/SRR8186651_2.fastq.gz --name SRR8186651 && \
  echo && \
  ls -lh && \
  shigatyper --version

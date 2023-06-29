# global arg variables
ARG SHIGEIFINDER_VER="1.3.5"
ARG SAMTOOLS_VER="1.10"
ARG BWA_VER="0.7.17"

### start of builder stage ###
FROM ubuntu:focal as builder

# re-instantiate these variables
ARG SHIGEIFINDER_VER
ARG SAMTOOLS_VER
ARG BWA_VER

# so that apt/tzdata doesn't ask for a timezone during build. Variable will not be in environment after building
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies via apt (a lot of this is for compiling C code); cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    gcc \
    g++ \
    zlib1g-dev \
    wget \
    ca-certificates \
    procps \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    bzip2 \
    gawk \
    gnuplot && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install bwa
RUN mkdir /bwa && \
    cd /bwa && \
    wget https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 && \
    tar -xjf bwa-${BWA_VER}.tar.bz2 && \
    rm -v bwa-${BWA_VER}.tar.bz2 && \
    cd bwa-${BWA_VER} && \
    make

# install samtools; no need to add to PATH, 'make install' does this for us
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    rm samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install

### start of app stage ###
# using fresh ubuntu:jammy image as base for app stage
FROM ubuntu:focal as app

# re-instantiate these variables
ARG SHIGEIFINDER_VER
ARG SAMTOOLS_VER
ARG BWA_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="ShigEiFinder"
LABEL software.version="${SHIGEIFINDER_VER}"
LABEL description="Cluster informed Shigella and EIEC serotyping tool from Illumina reads and assemblies"
LABEL website="https://github.com/LanLab/ShigEiFinder"
LABEL license="https://github.com/LanLab/ShigEiFinder/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"

# copy in samtools executables into app stage
COPY --from=builder /usr/local/bin/* /usr/local/bin

# copy in bwa executable
COPY --from=builder /bwa/bwa-${BWA_VER}/bwa /usr/local/bin

# install dependencies via apt; cleanup apt garbage
# ncbi-blast+ from apt is v2.9.0 (min ver requirement for ShigEiFinder)
# python version is 3.8.10
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    python3-setuptools \
    wget \
    ca-certificates \
    procps \
    libncurses5-dev \
    libbz2-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    bzip2 \
    ncbi-blast+ \
    unzip && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install ShigEiFinder; make /data
RUN wget https://github.com/LanLab/ShigEiFinder/archive/refs/tags/v${SHIGEIFINDER_VER}.tar.gz && \
    tar -xvf v${SHIGEIFINDER_VER}.tar.gz && \
    rm -v v${SHIGEIFINDER_VER}.tar.gz && \
    cd ShigEiFinder-${SHIGEIFINDER_VER} && \
    python3 setup.py install && \
    mkdir /data

# set locale settings for singularity compatibility. Set PATH to include bwa
ENV LC_ALL=C

# final working directory is /data
WORKDIR /data

### start of test stage ###
# using app stage as base image for test stage
FROM app as test

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
    chmod +x datasets && \
    mv -v datasets /usr/local/bin

# downloading a couple of representative genomes (FASTA) and run them through ShigEiFinder
# Shigella sonnei genome: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCA_019947675.1/
# BioSample: SAMN21386344
ARG GENBANK_ACCESSION="GCA_019947675.1"
RUN datasets download genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
    mkdir -v ${GENBANK_ACCESSION}-download && \
    unzip ${GENBANK_ACCESSION}.zip -d ${GENBANK_ACCESSION}-download && \
    rm ${GENBANK_ACCESSION}.zip && \
    mv -v ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}*.fna ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna && \
    shigeifinder -i ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna \
      --hits \
      -t 2 \
      --output shigeifinder.${GENBANK_ACCESSION}.out && \
    head -n 2 shigeifinder.${GENBANK_ACCESSION}.out

# Shigella flexneri 2a str. 301
# https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/198214/
ARG GENBANK_ACCESSION="GCF_000006925.2"
RUN datasets download genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
    mkdir -v ${GENBANK_ACCESSION}-download && \
    unzip ${GENBANK_ACCESSION}.zip -d ${GENBANK_ACCESSION}-download && \
    rm ${GENBANK_ACCESSION}.zip && \
    mv -v ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}*.fna ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna && \
    shigeifinder -i ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna \
      --hits \
      -t 2 \
      --output shigeifinder.${GENBANK_ACCESSION}.out && \
    head -n 2 shigeifinder.${GENBANK_ACCESSION}.out

# test with Shigella Sonnei FASTQs and run through ShigEiFinder (test bwa & samtools)
# https://www.ncbi.nlm.nih.gov/sra/SRX17216573[accn]
# https://www.ncbi.nlm.nih.gov/biosample/SAMN30499774
### NOTE: ENA FTP CAN BE SLOW TO DOWNLOAD FROM, HAVE PATIENCE. ALSO, SHIGEIFINDER RUNS MUCH SLOWER ON FASTQ FILES COMPARED TO FASTA FILES
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR212/091/SRR21205791/SRR21205791_1.fastq.gz && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR212/091/SRR21205791/SRR21205791_2.fastq.gz && \
    shigeifinder -r \
      -i SRR21205791_1.fastq.gz  SRR21205791_2.fastq.gz \
      --hits \
      --dratio \
      -t 2 \
      --output shigeifinder.SRR21205791.out && \
    head -n 2 shigeifinder.SRR21205791.out

# testing single end mode with same sample as above ^
RUN shigeifinder -r \
      -i SRR21205791_1.fastq.gz  \
      --hits \
      --dratio \
      --single_end \
      -t 2 \
      --output shigeifinder.SRR21205791.single-end.out && \
    head -n 2 shigeifinder.SRR21205791.single-end.out

# check dependencies and print help options
RUN shigeifinder --check && \
    shigeifinder --help && \
    shigeifinder --version
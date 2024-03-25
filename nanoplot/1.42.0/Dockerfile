FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during image build time.
ARG NANOPLOT_VER="1.42.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="nanoplot"
LABEL software.version="${NANOPLOT_VER}"
LABEL description="Plotting suite for Oxford Nanopore sequencing data and alignments"
LABEL website="https://github.com/wdecoster/NanoPlot"
LABEL license="https://github.com/wdecoster/NanoPlot/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Kate Prussing"
LABEL maintainer2.email="catharine.prussing@health.ny.gov"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

# install dependencies via apt; cleanup apt garbage; set locale to en_US.UTF-8
RUN apt-get update && apt-get install -y zlib1g-dev \
    bzip2 \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libncurses5-dev \
    libssl-dev \
    python3 \
    python3-pip \
    python3-setuptools \
    locales && \
    locale-gen en_US.UTF-8 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# for singularity compatibility
ENV LC_ALL=C

# install NanoPlot via pypi using pip3; make /data directory
RUN pip3 install matplotlib psutil requests NanoPlot==${NANOPLOT_VER} && \
    mkdir /data

WORKDIR /data

CMD NanoPlot --help

# testing layer
FROM app as test

# print help options and version
RUN NanoPlot --help && NanoPlot --version

# install wget for downloading test data
RUN apt-get update && apt-get install -y wget

# download ONT data for a Salmonella isolate, run NanoPlot on the FASTQ file
# Go here for more info: https://www.ebi.ac.uk/ena/browser/view/SRR19787768?show=reads
RUN wget https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR197/068/SRR19787768/SRR19787768_1.fastq.gz && \
    NanoPlot --fastq SRR19787768_1.fastq.gz --log --N50 -o /data/nanoplot-test && \
    ls -lh /data/nanoplot-test && \
    cat /data/nanoplot-test/NanoStats.txt

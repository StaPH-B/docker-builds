FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during build time.
ARG K2VER="2.1.3"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="2"
LABEL software="Kraken2"
LABEL software.version="${K2VER}"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# install dependencies and cleanup apt garbage
RUN apt-get update && apt-get -y --no-install-recommends install \
    wget \
    ca-certificates \
    zlib1g-dev \
    make \
    g++ \
    rsync \
    cpanminus \
    ncbi-blast+ && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# perl module required for kraken2-build
RUN cpanm Getopt::Std

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v${K2VER}.tar.gz && \
    tar -xzf v${K2VER}.tar.gz && \
    rm -rf v${K2VER}.tar.gz && \
    cd kraken2-${K2VER} && \
    ./install_kraken2.sh . && \
    mkdir /data /kraken2-db

ENV PATH="/kraken2-${K2VER}/:$PATH" \
    LC_ALL=C

# default command is to pull up help options
CMD [ "kraken2", "--help" ]

WORKDIR /data

### start of test stage ###
FROM app as test 

# print help and versions
RUN kraken2 --help && \
    kraken2-build --help && \
    kraken2 --version && \
    blastn -version && \
    dustmasker -version && \
    segmasker -version

# set working dir and download test k2 database inside
WORKDIR /kraken2-db
RUN wget https://genome-idx.s3.amazonaws.com/kraken/k2_viral_20230605.tar.gz && \
    tar -zxf k2_viral_20230605.tar.gz

# set working dir for running test commands below
WORKDIR /test

# download and classify SARS-CoV-2 reads
RUN wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_1.fastq.gz?raw=true -O SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_2.fastq.gz?raw=true -O SRR13957123_2.fastq.gz && \
    kraken2 --paired --classified-out cseqs#.fq --db /kraken2-db SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz --report kraken2_report.txt && \
    cat kraken2_report.txt



##### NO DATABASE INCLUDED WITH THIS DOCKER IMAGE #####
## User will need to mount a directory from their host machine that contains kraken2 database files 
## to a directory in the container (/kraken2-db exists for this purpose, but feel free to use another location)
## A list of created Kraken2 databases can be found at https://benlangmead.github.io/aws-indexes/k2

# DL MiniKraken2_8GB database. Built from RefSeq bacteria, archaea, viral, and human libraries.
# --strip-components=1 used so that the *.k2d files end up inside /kraken2-db and not another directory
#RUN mkdir /kraken2-db && \
# cd /kraken2-db && \
# wget --no-check-certificate https://genome-idx.s3.amazonaws.com/kraken/minikraken2_v2_8GB_201904.tgz && \
# tar -zxf --strip-components=1 minikraken2_v2_8GB_201904.tgz && \
# rm -rf minikraken2_v2_8GB_201904.tgz

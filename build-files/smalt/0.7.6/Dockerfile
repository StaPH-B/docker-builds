FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time
ARG SMALT_VER="0.7.6"
ARG SAMTOOLSVER="1.15"

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Smalt"
LABEL software.version="0.7.6"
LABEL description="SMALT aligns DNA sequencing reads with a reference genome."
LABEL website="https://www.sanger.ac.uk/tool/smalt-0/"
LABEL license="https://www.sanger.ac.uk/tool/smalt-0/"
LABEL maintainer1="Jill Hagey"
LABEL maintainer.email1="jvhagey@gmail.com"

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
        ca-certificates=20210119~20.04.2 \
        autoconf=2.69-11.1 \
        automake=1:1.16.1-4ubuntu6 \
        pkg-config=0.29.1-0ubuntu4 \
        gcc=4:9.3.0-1ubuntu2 \
        libtool=2.4.6-14 \
        libcurl4-openssl-dev=7.68.0-1ubuntu2.7 \
        libncurses5-dev=6.2-0ubuntu2 \
        zlib1g-dev=1:1.2.11.dfsg-2ubuntu1.3 \
        libbz2-dev=1.0.8-2 \
        liblzma-dev=5.2.4-1ubuntu1.1 \
        make=4.2.1-1.2 \
        gawk=1:5.0.1+dfsg-1 \
        unzip=6.0-25ubuntu1 \
        wget=1.20.3-1ubuntu2 && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Installing samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
    rm samtools-${SAMTOOLSVER}.tar.bz2 && \
    cd samtools-${SAMTOOLSVER} && \
    ./configure && \
    make && \
    make install

# Installing bambamc
RUN wget -O bambamc.zip https://github.com/gt1/bambamc/archive/refs/heads/master.zip && \
    unzip bambamc.zip && \
    rm bambamc.zip && \
    cd bambamc-master && \
    mv configure.in configure.ac && \
    autoreconf -i -f && \
    ./configure --prefix=/bambamc && \
    make && \
    make install && \
    make clean

ARG BAMBAMC_INSTALL_DIR="/bambamc"
ENV LD_LIBRARY_PATH="/bambamc/lib"
ENV PKG_CONFIG_DIR="/bambamc/lib/pkgconfig/"

# Installing smalt
RUN wget -O smalt-${SMALT_VER}.tar.gz \
    http://sourceforge.net/projects/smalt/files/smalt-${SMALT_VER}.tar.gz/download &&\
    tar -zxvf smalt-${SMALT_VER}.tar.gz && \
    rm smalt-${SMALT_VER}.tar.gz && \
    cd smalt-${SMALT_VER} && \
    ./configure --with-bambamc=yes BAMBAMC_CFLAGS="-I$BAMBAMC_INSTALL_DIR/include" BAMBAMC_LIBS="-L$BAMBAMC_INSTALL_DIR/lib -lbambamc" && \
    make && \
    make install && \
    mkdir /data

# set perl locale settings
# Required by most tools that use perl with singularity so we can use container with both docker and singularity
ENV LC_ALL=C

# Add path to programs
ENV PATH="${PATH}:/smalt-${SMALT_VER}"
ENV PATH="${PATH}:/samtools-${SAMTOOLSVER}"
WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# Run Smalt
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/819/615/GCF_000819615.1_ViralProj14015/GCF_000819615.1_ViralProj14015_genomic.fna.gz
RUN smalt index -k 13 -s 6 test_PhiX174 GCF_000819615.1_ViralProj14015_genomic.fna.gz

# Check validity of outputs
RUN cmp /data/test_PhiX174.smi /data/PhiX174.smi  && cmp /data/test_PhiX174.sma /data/PhiX174.sma

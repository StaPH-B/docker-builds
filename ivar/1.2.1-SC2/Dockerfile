FROM ubuntu:18.04

LABEL base.image="ubuntu:18.04"
LABEL dockerfile.version="3"
LABEL software="iVar"
LABEL software.version="1.2.1"
LABEL comments="Clone of ivar v1.2.1 pre-release most recent commit as of 05/09/2020"
LABEL artic.primer.comment="Dockerfile contains artic primer bed file from sept 17 2020 commit. see notes in Dockerfile"
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin@libuitsci.com"
LABEL modified.from="https://github.com/andersen-lab/ivar/blob/master/Dockerfile"
LABEL original.maintainer="Kathik G"
LABEL original.maintainer.email="gkarthik@scripps.edu"

RUN apt-get update
RUN apt-get install -y build-essential autoconf zlib1g-dev python3 wget libbz2-dev liblzma-dev libncurses-dev git bedtools python3-pip vim nano

# Artic ncov2019 (most recent commit as of 09/17/2020)
RUN git clone -n https://github.com/artic-network/artic-ncov2019.git && \
    cd artic-ncov2019 && \
    # this commit is when the nCov-2019.primer.bed file was last changed. Sept 17 2020
    git checkout 87449a03f5d85230a2a9214064adf2e2cc2abd51 && \
    mkdir /reference && \
    mv -v primer_schemes/nCoV-2019/V1/nCoV-2019.primer.bed /reference/ARTIC-V1.bed && \
    mv -v primer_schemes/nCoV-2019/V2/nCoV-2019.primer.bed /reference/ARTIC-V2.bed && \
    mv -v primer_schemes/nCoV-2019/V3/nCoV-2019.primer.bed /reference/ARTIC-V3.bed && \
    mv -v primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta /reference

# Seqtk
RUN mkdir seqtk &&\
    cd seqtk &&\
    wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz && \
    tar -zxf v1.3.tar.gz && \
    rm v1.3.tar.gz && \
    cd seqtk-1.3/ && \
    make && \
    make install
# Minimap2
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
    tar -xvf minimap2-2.17_x64-linux.tar.bz2 && \
    rm minimap2-2.17_x64-linux.tar.bz2
# HTSlib
RUN cd root/ &&\
    wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 &&\
    tar xvf htslib-1.9.tar.bz2 &&\
    cd htslib-1.9/ &&\
    ./configure &&\
    make &&\
    make install &&\
    cd ../ &&\
    rm htslib-1.9.tar.bz2
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
# SAMtools
RUN cd root &&\
    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 &&\
    tar xvf samtools-1.9.tar.bz2 &&\
    cd samtools-1.9/ &&\
    ./configure &&\
    make &&\
    make install &&\
    cd ../ &&\
    rm samtools-1.9.tar.bz2
# iVar v1.2.1
RUN cd root/ &&\
    wget https://github.com/andersen-lab/ivar/archive/v1.2.1.tar.gz &&\
    tar -xvf v1.2.1.tar.gz &&\
    rm -rf v1.2.1.tar.gz &&\
    cd ivar-1.2.1 &&\
    ./autogen.sh &&\
    ./configure &&\
    make &&\
    make install
# bwa
RUN mkdir bwa &&\
    cd bwa &&\
    wget https://github.com/lh3/bwa/archive/v0.7.17.tar.gz &&\
    tar xvf v0.7.17.tar.gz &&\
    rm v0.7.17.tar.gz &&\ 
    cd bwa-0.7.17/ &&\
    make
    
ENV PATH="/bwa/bwa-0.7.17:/minimap2-2.17_x64-linux:${PATH}"
# Snakemake
RUN pip3 install pandas snakemake

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

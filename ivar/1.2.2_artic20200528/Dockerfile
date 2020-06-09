FROM ubuntu:18.04

LABEL base.image="ubuntu:18.04"
LABEL container.version="1"
LABEL software="iVar"
LABEL software.version="1.2.2"
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL comments="Contains iVar 1.2.2 as well as compatible artic V3 primer schemes"
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL modified.from="https://github.com/andersen-lab/ivar/blob/master/Dockerfile"
LABEL original.maintainer="Kathik G"
LABEL original.maintainer.email="gkarthik@scripps.edu"

RUN apt-get update
RUN apt-get install -y build-essential autoconf zlib1g-dev python3 wget libbz2-dev liblzma-dev libncurses-dev git bedtools python3-pip vim nano

# Artic ncov2019 (most recent commit was 05/28/2020 as of 06/01/2020)
RUN git clone -n https://github.com/artic-network/artic-ncov2019.git &&\
    cd artic-ncov2019 &&\
    git checkout ef3f1ce9f66d49ec7caa67e0425e556bd67c53de
# Turn primer bedfiles into bedfiles reprenting amiplicons (alt primers are ignored)
RUN for artic_version in "V1" "V2"; do \
    cat /artic-ncov2019/primer_schemes/nCoV-2019/$artic_version/nCoV-2019.bed | \
    	awk '{ if ($0 ~ "LEFT") { print $1 "\t" $2 } else {print $3 "\t" $4 "\t" $5 }}' | \
	paste - - | \
	sed 's/_RIGHT//g' > /artic-ncov2019/primer_schemes/nCoV-2019/$artic_version/nCoV-2019_amplicon.bed ; \
	done && \
    cat /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.bed | \
    	grep -v "alt" | \
	awk '{ if ($0 ~ "LEFT") { print $1 "\t" $2 } else {print $3 "\t" $4 "\t" $5 }}' | \
	paste - - | \
	sed 's/_RIGHT//g' > /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019_amplicon.bed
# Get gff file for reference genome
RUN mkdir /reference && \
     wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/858/895/GCF_009858895.2_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz -P /reference && \
     gunzip /reference/GCF_009858895.2_ASM985889v3_genomic.gff.gz
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
# iVar v1.2.2
RUN cd root/ &&\
    wget https://github.com/andersen-lab/ivar/archive/v1.2.2.tar.gz &&\
    tar -xvf v1.2.2.tar.gz &&\
    rm -rf v1.2.2.tar.gz &&\
    cd ivar-1.2.2 &&\
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

# indexing the reference sequences
RUN for artic_version in "V1" "V2" "V3" ; do \
    bwa index /artic-ncov2019/primer_schemes/nCoV-2019/$artic_version/nCoV-2019.reference.fasta && \
    samtools faidx /artic-ncov2019/primer_schemes/nCoV-2019/$artic_version/nCoV-2019.reference.fasta ; done

# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

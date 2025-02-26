## Builder ##
FROM ubuntu:jammy as blat

ARG BLAT_VER="35"
ARG MACHTYPE="x86_64-pc-linux-gnu"

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    unzip \
    libpng-dev

RUN wget https://genome-test.gi.ucsc.edu/~kent/src/blatSrc${BLAT_VER}.zip &&\
    unzip blatSrc${BLAT_VER}.zip  &&\
    cd blatSrc &&\
    mkdir -p bin/${MACHTYPE} &&\
    mkdir -p lib/${MACHTYPE} &&\
    make HOME=$PWD MACHTYPE=${MACHTYPE} C_INCLUDE_PATH=/usr/include LIBRARY_PATH=/usr/lib CFLAGS="-fcommon" &&\
    mv bin/${MACHTYPE}/* /usr/local/bin/

## App ##
FROM ubuntu:jammy as app 

ARG PYMLST_VER="2.1.5"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pyMLST"
LABEL software.version="${PYMLST_VER}"
LABEL description="A Python Mlst Local Search Tool"
LABEL website="https://github.com/bvalot/pyMLST"
LABEL license="https://github.com/bvalot/pyMLST/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

#install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y\
    mafft \
    kma \
    python3-pip \
    python3-biopython &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get blat from builder
COPY --from=blat /usr/local/bin/* /usr/local/bin/

# install pymlst
RUN pip3 install --no-cache pymlst==${PYMLST_VER}

CMD pyMLST -h && claMLST -h && wgMLST -h

ENV LC_ALL=C

WORKDIR /data

## Test ##
FROM app as test

# checking CMD line
RUN pyMLST -h && claMLST -h && wgMLST -h

RUN apt-get update && apt-get install --no-install-recommends -y wget

# download assemblies for test
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/032/604/515/GCA_032604515.1_PDT001925635.1/GCA_032604515.1_PDT001925635.1_genomic.fna.gz \
    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/032/847/695/GCA_032847695.1_PDT001947824.1/GCA_032847695.1_PDT001947824.1_genomic.fna.gz \
    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/034/261/675/GCA_034261675.1_PDT002019551.2/GCA_034261675.1_PDT002019551.2_genomic.fna.gz \
    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/037/026/425/GCA_037026425.1_PDT002098409.1/GCA_037026425.1_PDT002098409.1_genomic.fna.gz &&\
    gunzip *.fna.gz

# classical MLST
RUN claMLST import MLST_DB escherichia spp. -m achtman &&\
    claMLST search MLST_DB GCA_032604515.1_PDT001925635.1_genomic.fna

#cg/wgMLST
# initiliaze db
RUN wgMLST import WGMLST_DB Escherichia coli
# add assemblies
RUN wgMLST add WGMLST_DB GCA_032604515.1_PDT001925635.1_genomic.fna -s 2023BM00142 &&\
    wgMLST add WGMLST_DB GCA_032847695.1_PDT001947824.1_genomic.fna -s 2023BM00149 &&\
    wgMLST add WGMLST_DB GCA_034261675.1_PDT002019551.2_genomic.fna -s 2023BM00164 &&\
    wgMLST add WGMLST_DB GCA_037026425.1_PDT002098409.1_genomic.fna -s 2024BM00013
# check db and calculate cgMLST distances
RUN wgMLST stats WGMLST_DB &&\
    wgMLST distance WGMLST_DB

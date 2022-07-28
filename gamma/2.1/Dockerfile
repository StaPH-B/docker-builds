# base image
FROM ubuntu:bionic as app

# for easy upgrade later. ARG variables only persist during image build time
ARG GAMMA_VER="2.1"
ARG HMMR_VER="3.3"
ARG AMR_VER="3.10.18"

# metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="GAMMA"
LABEL software.version="v2.1"
LABEL description="Gene Allele Mutation Microbial Assessment"
LABEL website="https://github.com/rastanton/GAMMA/"
LABEL license="Apache 2.0"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="jvhagey@gmail.com"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
    rsync \
    unzip \
    tar \
    python3.7 \
    python3-pip \
    gzip \
    wget \
    git \
    curl \
    make \
    g++ \
    ncbi-blast+ \
    hmmer && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

#install biopython
RUN pip3 install biopython cgecore tabulate

# hmmer 3.3 since amrfinder requires 3.2 or higher (apt version is 3.1)
# apt dependencies: make, g++
RUN wget http://eddylab.org/software/hmmer/hmmer-${HMMR_VER}.tar.gz && \
 tar xzf hmmer-${HMMR_VER}.tar.gz && \
 rm hmmer-${HMMR_VER}.tar.gz && \
 cd hmmer-${HMMR_VER} && \
 ./configure && \
 make && \
 make install

# install amrfinder
RUN mkdir amrfinder && cd /amrfinder && \
    wget https://github.com/ncbi/amr/releases/download/amrfinder_v${AMR_VER}/amrfinder_binaries_v${AMR_VER}.tar.gz && \
    tar zxf amrfinder_binaries_v${AMR_VER}.tar.gz && \
    rm amrfinder_binaries_v${AMR_VER}.tar.gz

# install blat
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat && \
    chmod +x blat && \
    mv blat /bin/blat && \
    mkdir /data

# download ARG-ANNOT database (https://github.com/rastanton/GAMMA/issues/6)
RUN wget http://backup.mediterranee-infection.com/arkotheque/client/ihumed/_depot_arko/articles/691/argannot-nt_doc.fasta && \
 mv -v argannot-nt_doc.fasta arg-annot.fasta

# install RStanton AR Genes Fasta File
RUN wget https://github.com/stjacqrm/gb_files/archive/988d9c83d055e026ae62c6398ca6b8a3cde46cc0.zip && \
    unzip 988d9c83d055e026ae62c6398ca6b8a3cde46cc0.zip && \
    rm 988d9c83d055e026ae62c6398ca6b8a3cde46cc0.zip && \
    mv gb_files-988d9c83d055e026ae62c6398ca6b8a3cde46cc0 gb_files

#install GAMMA
RUN wget https://github.com/rastanton/GAMMA/archive/refs/tags/v${GAMMA_VER}.tar.gz && \
    tar zxf v${GAMMA_VER}.tar.gz && \
    rm v${GAMMA_VER}.tar.gz && \
    mv GAMMA-${GAMMA_VER} GAMMA && \
    cd GAMMA && \
    chmod +x GAMMA.py && \
    chmod +x GAMMA-S.py

ENV PATH="${PATH}:/bin/blat:/amrfinder:/gb_files:/GAMMA:/GAMMA/GAMMA.py:/arg-annot.fasta" LC_ALL=C

# download databases
RUN cd /amrfinder && ./amrfinder -u

WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# Run amrfinder
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/008/632/635/GCF_008632635.1_ASM863263v1/GCF_008632635.1_ASM863263v1_genomic.fna.gz
RUN gunzip GCF_008632635.1_ASM863263v1_genomic.fna.gz
RUN GAMMA-S.py GCF_008632635.1_ASM863263v1_genomic.fna db.fasta GCF_008632635.1

# Check validity of outputs
RUN echo GCF_008632635.1.gamma
RUN cmp /data/test_GCF_008632635.1.gamma /data/GCF_008632635.1.gamma && cmp /data/test_GCF_008632635.1.psl /data/GCF_008632635.1.psl

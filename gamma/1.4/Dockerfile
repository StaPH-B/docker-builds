# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL container.version="1"
LABEL software="centroid"
LABEL software.version="v1.4"
LABEL description="Gene Allele Mutation Microbial Assessment"
LABEL website="https://github.com/rastanton/GAMMA/tree/v1.4"
LABEL license=""
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
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
RUN pip3 install biopython cgecore

RUN pip3 install tabulate biopython cgecore

RUN pip3 install tabulate biopython

# hmmer 3.3 since amrfinder requires 3.2 or higher (apt version is 3.1)
# apt dependencies: make, g++
RUN wget http://eddylab.org/software/hmmer/hmmer-3.3.tar.gz && \
 tar xzf hmmer-3.3.tar.gz && \
 rm hmmer-3.3.tar.gz && \
 cd hmmer-3.3 && \
 ./configure && \
 make && \
 make install

# install amrfinder
RUN mkdir amrfinder && cd /amrfinder && \
    wget https://github.com/ncbi/amr/releases/download/amrfinder_v3.10.18/amrfinder_binaries_v3.10.18.tar.gz && \
    tar zxf amrfinder_binaries_v3.10.18.tar.gz && \
    rm amrfinder_binaries_v3.10.18.tar.gz

# install blat
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat && \
    chmod +x blat && \
    mv blat /bin/blat && \
    mkdir /data

# install ARG-ANNOT
RUN wget https://www.mediterranee-infection.com/wp-content/uploads/2019/03/arg-annot-v4-nt-may2018.txt && \
    mv arg-annot-v4-nt-may2018.txt arg-annot.fasta

# install RStanton AR Genes Fasta File
RUN wget https://github.com/stjacqrm/gb_files/archive/988d9c83d055e026ae62c6398ca6b8a3cde46cc0.zip && \
    unzip 988d9c83d055e026ae62c6398ca6b8a3cde46cc0.zip && \
    rm 988d9c83d055e026ae62c6398ca6b8a3cde46cc0.zip && \
    mv gb_files-988d9c83d055e026ae62c6398ca6b8a3cde46cc0 gb_files

#install GAMMA
RUN wget https://github.com/rastanton/GAMMA/archive/refs/tags/v1.4.tar.gz && \
    tar zxf v1.4.tar.gz && \
    rm v1.4.tar.gz && \
    mv GAMMA-1.4 GAMMA && \
    cd GAMMA && \
    chmod +x GAMMA.py

ENV PATH="${PATH}:/bin/blat:/amrfinder:/gb_files:/GAMMA:/GAMMA/GAMMA.py:/arg-annot.fasta" LC_ALL=C

# download databases
RUN cd /amrfinder && ./amrfinder -u

WORKDIR /data

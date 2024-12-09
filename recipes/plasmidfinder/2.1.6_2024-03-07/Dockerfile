FROM ubuntu:focal as app

ARG PLASMIDFINDER_VER="2.1.6"
# There is a plasmidfinder database version (2.1), but that hasn't been updated in... awhile
# Instead, I think we should do what we do for the other *finder tools and use the latest commit
# see here: https://bitbucket.org/genomicepidemiology/plasmidfinder_db/commits/3e77502f23c4f0230e0644e47e1b649d2378495f
ARG DB_COMMIT_HASH="3e77502f23c4f0230e0644e47e1b649d2378495f"
ARG KMA_VER="1.4.14"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="plasmidfinder"
LABEL software.version="${PLASMIDFINDER_VER}"
LABEL description="Identifies plasmids in total or partial sequenced isolates of bacteria."
LABEL website="https://bitbucket.org/genomicepidemiology/plasmidfinder"
LABEL license="https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/README.md"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# ARG so that this variable only persists at image build time
ARG DEBIAN_FRONTEND noninteractive

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
# ncbi-blast v2.6.0 via debian:stretch apt
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    git \
    ncbi-blast+ \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-dev \
    gcc \
    make \
    libz-dev \
    dos2unix \
    unzip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install python dependencies
RUN pip3 install biopython==1.73 tabulate==0.7.7 cgecore==1.5.5

# Install kma
RUN git clone --branch ${KMA_VER} --depth 1 https://bitbucket.org/genomicepidemiology/kma.git && \
    cd kma && \
    make && \
    mv -v kma* /usr/local/bin/

RUN wget https://bitbucket.org/genomicepidemiology/plasmidfinder/get/${PLASMIDFINDER_VER}.tar.gz && \
    mkdir plasmidfinder && \
    tar -xvf ${PLASMIDFINDER_VER}.tar.gz -C plasmidfinder --strip-components 1 && \
    rm ${PLASMIDFINDER_VER}.tar.gz

ENV PATH="${PATH}:/plasmidfinder"

RUN chmod +x plasmidfinder/plasmidfinder.py 

RUN mkdir /database && \
    git clone https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git /database && \
    cd /database && \
    git checkout ${DB_COMMIT_HASH} && \
    dos2unix *.fsa && \
    python3 INSTALL.py kma_index

CMD plasmidfinder.py -h

WORKDIR /data

FROM app as test

RUN plasmidfinder.py -h

RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz && \
    gzip -d ERR1937840.fastq.gz && mkdir test && \
    plasmidfinder.py -i ERR1937840.fastq -o test

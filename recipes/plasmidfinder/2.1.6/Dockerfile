# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM debian:stretch as app

#https://bitbucket.org/genomicepidemiology/plasmidfinder/issues/10/version-number
# ARG sets environment variables during the build stage
ARG PLASMIDFINDER_VER="2.1.6"
ARG PLASMIDFINDER_DB_VER="2.1"
ARG KMA_VER="1.0.1"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="debian:stretch"
LABEL dockerfile.version="3"
LABEL software="plasmidfinder"
LABEL software.version="${PLASMIDFINDER_VER}"
LABEL description="Identifies plasmids in total or partial sequenced isolates of bacteria."
LABEL website="https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/README.md"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# ARG so that this variable only persists at image build time
ARG DEBIAN_FRONTEND noninteractive

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
# ncbi-blast v2.6.0 via debian:stretch apt
RUN apt-get update -y && apt-get install -y \
    apt-utils \
    wget \
    python3-pip \
    ncbi-blast+ \
    gzip \
    procps \
    libz-dev && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install python dependencies
RUN pip3 install --upgrade pip && \
    python3 -m pip install tabulate && \
    pip3 install -U biopython==1.73 cgecore

# Install kma
RUN wget https://bitbucket.org/genomicepidemiology/kma/get/${KMA_VER}.tar.gz && \
    mkdir kma && \
    tar -xvf ${KMA_VER}.tar.gz -C kma --strip-components 1 && \
    rm ${KMA_VER}.tar.gz && \
    cd kma && make && \
    mv kma* /bin/

RUN wget https://bitbucket.org/genomicepidemiology/plasmidfinder/get/${PLASMIDFINDER_VER}.tar.gz && \
    mkdir plasmidfinder && \
    tar -xvf ${PLASMIDFINDER_VER}.tar.gz -C plasmidfinder --strip-components 1 && \
    rm ${PLASMIDFINDER_VER}.tar.gz

ENV PATH="${PATH}:/plasmidfinder"

RUN chmod 755 plasmidfinder/plasmidfinder.py 

RUN wget https://bitbucket.org/genomicepidemiology/plasmidfinder_db/get/${PLASMIDFINDER_DB_VER}.tar.gz && \
    mkdir plasmidfinder_db && \
    tar -xvf ${PLASMIDFINDER_DB_VER}.tar.gz -C plasmidfinder_db --strip-components 1 && \
    rm ${PLASMIDFINDER_DB_VER}.tar.gz && \
    cd plasmidfinder_db && \
    python3 INSTALL.py kma_index && \
    cd .. && \
    mv plasmidfinder_db database

WORKDIR /data

FROM app as test

RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz && \
    gzip -d ERR1937840.fastq.gz && mkdir test && \
    plasmidfinder.py -i ERR1937840.fastq -o test

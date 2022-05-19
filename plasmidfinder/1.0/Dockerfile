# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM debian:stretch as app

#https://bitbucket.org/genomicepidemiology/plasmidfinder/issues/10/version-number
# ARG sets environment variables during the build stage
ARG PLASMIDFINDER_VER="2.1"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="debian:stretch"
LABEL dockerfile.version="1"
LABEL software="plasmidfinder"
LABEL software.version=$PLASMIDFINDER_VER
LABEL description="Identifies plasmids in total or partial sequenced isolates of bacteria."
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"


ENV DEBIAN_FRONTEND noninteractive,Teletype

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN set -xe && \
    apt-get update -y && apt-get install -y \
    git \
    apt-utils \
    wget \
    python3-pip \
    ncbi-blast+ \
    gzip \
    libz-dev
    #rm -rf /var/cache/apt/* /var/lib/apt/lists/*

# Install python dependencies
RUN pip3 install --upgrade pip && \
    python3 -m pip install tabulate && \
    pip3 install -U biopython==1.73 cgecore

# Install kma
RUN git clone --branch 1.0.1 --depth 1 https://bitbucket.org/genomicepidemiology/kma.git
RUN cd kma && make && \
    mv kma* /bin/

RUN git clone https://bitbucket.org/genomicepidemiology/plasmidfinder.git && \
    cp plasmidfinder/plasmidfinder.py /usr/src/plasmidfinder.py && \
    mv plasmidfinder/test/database/ /database && \
    mv plasmidfinder/test* /test/

RUN chmod 755 /usr/src/plasmidfinder.py && \
    chmod 755 test/test.sh

RUN git clone https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git && \
    cd plasmidfinder_db && \
    python3 INSTALL.py kma_index && \
    cd .. && \
    rm -rf database && \
    mv plasmidfinder_db database

ENV PATH $PATH:/usr/src

WORKDIR /data

FROM app as test

RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz
RUN gzip -d ERR1937840.fastq.gz && chmod 755 ERR1937840.fastq && mkdir test && \
    plasmidfinder.py -i ERR1937840.fastq -o test

FROM ubuntu:jammy as app

ARG RASUSA_VER="0.8.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="rasusa"
LABEL software.version="${RASUSA_VER}"
LABEL description="Randomly subsample sequencing reads to a specified coverage."
LABEL website="https://github.com/mbhall88/rasusa"
LABEL license="https://github.com/mbhall88/rasusa/blob/master/LICENSE"
LABEL maintainer="Jake Garfin"
LABEL maintainer.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

# install wget and cleanup apt garbage
RUN apt-get update && apt-get -y install --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

# install rasusa
RUN wget -q https://github.com/mbhall88/rasusa/releases/download/${RASUSA_VER}/rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl.tar.gz && \
    tar -xvf rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl.tar.gz && \
    rm -rf rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl.tar.gz && \
    mkdir /data

# set PATH and perl locale settings
ENV PATH="${PATH}:/rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl/" \
    LC_ALL=C

WORKDIR /data

CMD rasusa --help

FROM app as test 

# print version and help options
RUN rasusa --version && rasusa --help

# cannot run rust-based test, since rust isn't installed, but just testing basic command on SC2 reads in our repo
# inputs FASTQs each have 80867 reads
# output FASTQs should have 40434 reads in each (about 1/2 of input)
# -s 1 is for setting a specific seed
# -O is for gzip compression on output FASTQs
RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    rasusa -i SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz -n 40434 -s 1 -O g -o SRR13957123_downsampled_1.fastq.gz SRR13957123_downsampled_2.fastq.gz && \
    ls -lh

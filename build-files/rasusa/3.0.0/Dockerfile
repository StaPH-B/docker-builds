FROM ubuntu:noble AS app

ARG RASUSA_VER="3.0.0"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Rasusa"
LABEL software.version="${RASUSA_VER}}"
LABEL description="Randomly subsample sequencing reads to a specified coverage."
LABEL website="https://github.com/mbhall88/rasusa"
LABEL license="https://github.com/mbhall88/rasusa/blob/master/LICENSE"
LABEL maintainer="Jake Garfin"
LABEL maintainer.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"
LABEL maintainer4="Raheel Ahmed"
LABEL maintainer4.email="raheelsyedahmed@gmail.com"

WORKDIR /opt

# Install dependencies via apt-get & autoclean
RUN apt-get update && apt-get -y install --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

# install rasusa and set up /data work directory
RUN wget -q https://github.com/mbhall88/rasusa/releases/download/${RASUSA_VER}/rasusa-${RASUSA_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    tar -xvf rasusa-${RASUSA_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    rm -rf rasusa-${RASUSA_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    mkdir /data

# set PATH and perl locale settings
ENV PATH="${PATH}:/opt/rasusa-${RASUSA_VER}-x86_64-unknown-linux-gnu/" \
    LC_ALL=C

CMD [ "rasusa", "--help" ]

WORKDIR /data


FROM app AS test 

# print version and help options
RUN rasusa --version && rasusa --help

# cannot run rust-based test, since rust isn't installed, but just testing basic command on SC2 reads in our repo
# inputs FASTQs each have 80867 reads
# output FASTQs should have 40434 reads in each (about 1/2 of input)
# -s 1 is for setting a specific seed
# -O is for gzip compression on output FASTQs
RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    rasusa reads --num 40434 -s 1 -O g -o SRR13957123_downsampled_1.fastq.gz -o SRR13957123_downsampled_2.fastq.gz SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz && \
    ls -lh

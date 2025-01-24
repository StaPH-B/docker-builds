ARG ANY2FASTA_VERSION=0.4.2

# base image
FROM ubuntu:focal as app

# version to build with
ARG ANY2FASTA_VERSION

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2"
LABEL software="any2fasta"
LABEL software.version="0.4.2"
LABEL description="Turns files into fastas."
LABEL website="https://github.com/tseemann/any2fasta"
LABEL license="https://github.com/tseemann/any2fasta/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    perl \
    zip \
    unzip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install any2fasta
RUN wget https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VERSION}.tar.gz && \
    tar -xvf v${ANY2FASTA_VERSION}.tar.gz && \
    rm v${ANY2FASTA_VERSION}.tar.gz && \
    cd any2fasta-${ANY2FASTA_VERSION} && \
    chmod +x any2fasta

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/any2fasta-${ANY2FASTA_VERSION}:$PATH" \
    LC_ALL=C

# set working directory
WORKDIR /data

#######################
##### NEXT STAGE! #####
#######################

# running a 'test' in the 'test' stage
FROM app as test

ARG ANY2FASTA_VERSION

# check version and print help options
RUN any2fasta -v && \
    any2fasta -h && \
    any2fasta -h | grep github

WORKDIR /test

RUN echo "move test data here..." && \
    mv /any2fasta-${ANY2FASTA_VERSION}/test.* .

RUN echo "running any2fasta on test data..." && \
    any2fasta /dev/null 2>&1 | grep 'ERROR' && \
    any2fasta test.noseq.gff 2>&1 | grep 'ERROR' && \
    any2fasta test.gbk | grep -m 3 '^>' && \
    any2fasta test.gff | grep -m 3 '^>' && \
    any2fasta test.fna | grep -m 3 '^>' && \
    any2fasta test.gfa | grep -m 3 '^>' && \
    any2fasta test.fq  | grep -m 3 '^>' && \
    any2fasta test.embl | grep -m 3 '^>' && \
    any2fasta test.clw  | grep -m 3 '^>' && \
    any2fasta test.sth  | grep -m 3 '^>' && \
    any2fasta test.fna | grep 'CRYANT' && \
    any2fasta -n test.fna | grep 'CNNANT' && \
    any2fasta test.gfa | grep '^>24292$' && \
    any2fasta test.fq | grep '^>ERR1163317.999' && \
    any2fasta test.sth | grep '^>O83071' && \
    any2fasta test.clw | grep '^>gene03' && \
    any2fasta -l test.gbk | grep 'taagaatgagtagaaggttttga' && \
    any2fasta -u test.gbk | grep 'TAAGAATGAGTAGAAGGTTTTGA' && \
    any2fasta -u test.embl | grep 'K02675' && \
    any2fasta -q -l -n test.fq | wc -l | grep '^2000$' && \
    any2fasta - < test.gbk  | grep -m 1 -F 'NZ_AHMY02000074' && \
    gzip -c test.gbk | any2fasta - | grep -m 1 -F 'NZ_AHMY02000074' && \
    bzip2 -c test.gbk | any2fasta - | grep -m 1 -F 'NZ_AHMY02000074' && \
    zip test.gbk.zip test.gbk && \
    any2fasta test.gbk.zip | grep -m 1 -F 'NZ_AHMY02000074'

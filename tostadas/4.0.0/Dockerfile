FROM ubuntu:jammy as app

ARG TOSTADAS_VER="4.0.0"
ARG TABLE2ASN_RELEASE_DATE="2023-10-05"

USER root

WORKDIR /

LABEL authors="Jessica Rowell and Ankush Gupta"
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="3"
LABEL software="tostadas"
LABEL software.version=$TOSTADAS_VER
LABEL description="Image for the TOSTADAS: Toolkit for Open Sequence Triage, Annotation and DAtabase Submission pipeline"
LABEL website="https://github.com/CDCgov/tostadas"
LABEL license="https://github.com/CDCgov/tostadas/LICENSE"
LABEL maintainer="Jessica Rowell"
LABEL maintainer.email="jerowell@deloitte.com"
LABEL maintainer2="Kyle O'Connell"
LABEL maintainer2.email="kyoconnell@deloitte.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download tostadas repo, move to /tostadas, and create /data
RUN wget https://github.com/CDCgov/tostadas/archive/refs/tags/v${TOSTADAS_VER}.tar.gz && \
    tar -xvf v${TOSTADAS_VER}.tar.gz && \
    rm v${TOSTADAS_VER}.tar.gz && \
    mv tostadas-${TOSTADAS_VER} tostadas && \
    mkdir /data

# use mamba to install conda packages
RUN micromamba env create -f tostadas/environment.yml && \
    micromamba clean -a -y && \
    echo "source activate tostadas" > ~/.bashrc && \
    rm -rf /tostadas

RUN wget -q https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${TABLE2ASN_RELEASE_DATE}/by_program/table2asn/linux64.table2asn.gz && \
    gunzip linux64.table2asn.gz && \
    mv linux64.table2asn table2asn && \
    chmod +x table2asn

ENV PATH=/opt/conda/envs/tostadas/bin:/opt/conda/envs/env/bin:$PATH \
    LC_ALL=C.UTF-8

WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
###### Step 2. Set up the testing stage.                                 #####
###### The docker image is built to the 'test' stage before merging, but #####
###### the test stage (or any stage after 'app') will be lost.           #####
###### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app as test
ARG TABLE2ASN_RELEASE_DATE="2023-10-05"

RUN liftoff --version && \
    samtools --version && \
    python --version && \
    table2asn -help

ARG FILES="table2asn_readme.txt \
    SubmissionTemplate.sbt \
    short.fsa"

RUN for file in ${FILES}; do wget -q https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${TABLE2ASN_RELEASE_DATE}/documentation/${file}; done && \
    table2asn -t SubmissionTemplate.sbt -i short.fsa -o helicase.sqn
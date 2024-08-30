FROM mambaorg/micromamba:1.5.8 as app

ARG TOSTADAS_VER="3.1.0"

USER root

WORKDIR /

LABEL authors="Cole and Ankush Gupta"
LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="2"
LABEL software="tostadas"
LABEL software.version=$TOSTADAS_VER
LABEL description="Image for the TOSTADAS: Toolkit for Open Sequence Triage, Annotation and DAtabase Submission pipeline"
LABEL website="https://github.com/CDCgov/tostadas"
LABEL license="https://github.com/CDCgov/tostadas/LICENSE"
LABEL maintainer="Ankush Gupta"
LABEL maintainer.email="ankushkgupta@deloitte.com"
LABEL maintainer2="Kyle O'Connell"
LABEL maintainer2.email="kyoconnell@deloitte.com"
LABEL maintainer3="Cole Tindall"
LABEL maintainer3.email="ctindall@deloitte.com"

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

RUN liftoff --version && \
    samtools --version && \
    python --version

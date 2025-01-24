FROM nfcore/base:2.1 as app
# nfcore/base is Debian

# comes with warning about conda version
# ==> WARNING: A newer version of conda exists. <==
#   current version: 4.9.2
#   latest version: 22.11.1
#
# Please update conda by running
#
#     $ conda update -n base -c defaults conda

ARG TOSTADAS_VER="0.2.0-beta"

LABEL authors="Cole and Ankush Gupta"
LABEL base.image="nfcore/base:2.1"
LABEL dockerfile.version="1"
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

# download tostadas repo, move to /tostadas, and create /data
RUN wget https://github.com/CDCgov/tostadas/archive/refs/tags/v${TOSTADAS_VER}.tar.gz && \
    tar -xvf v${TOSTADAS_VER}.tar.gz && \
    rm v${TOSTADAS_VER}.tar.gz && \
    mv tostadas-${TOSTADAS_VER} tostadas && \
    mkdir /data

# install mamba
RUN conda install mamba -n base -c conda-forge

# use mamba to install conda packages
RUN mamba env create -f tostadas/environment.yml && \
    mamba clean -a -y && \
    echo "source activate tostadas" > ~/.bashrc && \
    rm -rf /tostadas

ENV PATH=/opt/conda/envs/tostadas/bin:/opt/conda/envs/env/bin:$PATH \
    LC_ALL=C.UTF-8

WORKDIR /data

FROM app as test

RUN mamba list && conda list

RUN liftoff --version && \
    samtools --version && \
    python --version

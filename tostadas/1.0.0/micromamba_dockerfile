FROM mambaorg/micromamba:1.1.0 as app

ARG TOSTADAS_VER="0.2.0-beta"

LABEL authors="Cole and Ankush Gupta"
LABEL base.image="mambaorg/micromamba:1.1.0"
LABEL dockerfile.version="1"
LABEL software="tostadas"
LABEL software.version=$TOSTADAS_VER
LABEL description="Image for the TOSTADAS: Toolkit for Open Sequence Triage, Annotation and DAtabase Submission pipeline"
LABEL website="https://github.com/CDCgov/tostadas"
LABEL license="https://github.com/CDCgov/tostadas/LICENSE"
LABEL maintainer="Ankush Gupta"
LABEL maintainer.email="ankushkgupta@deloitte.com"
LABEL maintainer2="Kyle O'Connell"
LABEL maintainer2.email=""
LABEL maintainer3="Cole Tindall"
LABEL maintainer3.email=""

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download tostadas repo, move to /tostadas, and create /data
RUN wget https://github.com/CDCgov/tostadas/archive/refs/tags/v${TOSTADAS_VER}.tar.gz && \
    tar -xvf v${TOSTADAS_VER}.tar.gz && \
    rm v${TOSTADAS_VER}.tar.gz && \
    mv tostadas-${TOSTADAS_VER} tostadas && \
    mkdir /data

RUN micromamba create -f tostadas/environment.yml && \
    micromamba clean -a -y && \
    rm -rf /tostadas

ENV ENV_NAME="tostadas"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

ENV PATH=/opt/conda/envs/tostadas/bin:/opt/conda/envs/env/bin:$PATH \
    LC_ALL=C.UTF-8

WORKDIR /data

FROM app as test

RUN liftoff --version && \
    samtools --version && \
    python --version

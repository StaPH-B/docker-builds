FROM mambaorg/micromamba:0.24.0 as app

USER root

WORKDIR /

#metadata
LABEL base.image="FROM mambaorg/micromamba:0.24.0"
LABEL dockerfile.version="1"
LABEL software="ncov-recombinant"
LABEL software.version="v0.6.1"
LABEL description="SARS-CoV-2 recombinant sequence detection"
LABEL website="https://github.com/ktmeaton/ncov-recombinant"
LABEL license="https://github.com/ktmeaton/ncov-recombinant/blob/master/LICENSE"
LABEL maintainer="Wes Hottel"
LABEL maintainer.email="wesley-hottel@uiowa.edu"

#Install dependencies
RUN apt-get update && apt-get install -y python \ 
  git \
  wget && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

#Clone ncov-recombinant repository 
RUN git clone https://github.com/ktmeaton/ncov-recombinant.git &&\
cd ncov-recombinant

#Install ncov-recombinant
RUN micromamba create -n ncov-recombinant-env -f ncov-recombinant/workflow/envs/environment.yaml &&\
micromamba clean -a -y

#Set environment
ENV PATH="/opt/conda/envs/ncov-recombinant-env/bin:/opt/conda/envs/env/bin:${PATH}" \
 LC_ALL=C.UTF-8

WORKDIR /data

#Test install using postive controls included as part of repo
FROM app as test 

WORKDIR /ncov-recombinant

ENV ENV_NAME="ncov-recombinant-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN snakemake --profile /ncov-recombinant/profiles/controls-positive

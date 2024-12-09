FROM mambaorg/micromamba:1.2.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building
WORKDIR /

ARG EMMTYPER_VER="0.2.0"

LABEL base.image="mambaorg/micromamba:1.2.0"
LABEL dockerfile.version="1"
LABEL software="emmtyper"
LABEL software.version=${EMMTYPER_VER}
LABEL description="Conda environment for emmtyper. emmtyper is a command line tool for emm-typing of Streptococcus pyogenes using a de novo or complete assembly."
LABEL website="https://github.com/MDU-PHL/emmtyper"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/MDU-PHL/emmtyper/blob/master/LICENSE"
LABEL maintainer="Henry Kunerth"
LABEL maintainer.email="henrykunerth@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*
 
# set the environment
ENV PATH="$PATH" \
 LC_ALL=C.UTF-8

#install emmtyper and dependencies
RUN micromamba create -n emmtyper && \
    eval "$(micromamba shell hook --shell=bash)" && \
    micromamba activate emmtyper && \
    micromamba install --yes --name emmtyper -c conda-forge -c bioconda -c defaults emmtyper \
    emmtyper=${EMMTYPER_VER} && \
    micromamba clean --all --yes


ENV ENV_NAME="emmtyper"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

FROM app as test

ENV ENV_NAME="emmtyper"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN wget 'ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/006/785/GCA_000006785.2_ASM678v2/GCA_000006785.2_ASM678v2_genomic.fna.gz' && \
	gunzip GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	mv GCA_000006785.2_ASM678v2_genomic.fna test_data.fasta
RUN emmtyper test_data.fasta && \
	emmtyper -w pcr test_data.fasta -o test_out && \
	head -10 test_out

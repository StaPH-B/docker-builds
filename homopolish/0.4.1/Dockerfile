FROM mambaorg/micromamba:1.3.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /


# ARG sets environment variables during the build stage
ARG HOMOPOLISH_VER="0.4.1"


LABEL base.image="mambaorg/micromamba:1.3.0"
LABEL dockerfile.version="1"
LABEL software="homopolish"
LABEL software.version=${HOMOPOLISH_VER}
LABEL description="Genome polisher  developed for Nanopore and extended for PacBioCLR"
LABEL website="https://github.com/ythuang0522/homopolish"
LABEL license="https://github.com/ythuang0522/homopolish/blob/master/LICENSE"
LABEL maintainer="Shelby Bennett"
LABEL maintainer.email="shelby.bennett@dgs.virginia.com"

# RUN executes code during the build
# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get -y --no-install-recommends install \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# create conda enviornement homopolish called homopolish from bioconda recipe; clean up conda garbage
RUN micromamba create -n homopolish -c conda-forge -c bioconda -c defaults homopolish=${HOMOPOLISH_VER} && \
 micromamba clean -a -y

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/homopolish/bin:/opt/conda/envs/env/bin:${PATH}" \
 LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

# create test layer to ensure program was sucessfully installed
FROM app as test

# ensure mamba/conda enviornment is activated during the test

ENV ENV_NAME="homopolish"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Grab test S.enterica genome from NCBI and run homopolish
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz && \
gzip -d GCF_000006945.2_ASM694v2_genomic.fna.gz && \ 
homopolish polish -a GCF_000006945.2_ASM694v2_genomic.fna -g Salmonella_enterica -m R9.4.pkl -o test1 && \ 
cat test1/*.fasta

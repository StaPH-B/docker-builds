FROM mambaorg/micromamba:0.22.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags.
# thankfully pangolearn github tag is simply a date
ARG PANGOLIN_VER="v3.1.20"
ARG PANGOLEARN_VER="2022-02-28"
ARG SCORPIO_VER="v0.3.16"
ARG CONSTELLATIONS_VER="v0.1.4"
ARG USHER_VER="0.5.2"
ARG PANGO_DESIGNATION_VER="v1.2.132"

# metadata labels
LABEL base.image="mambaorg/micromamba:0.22.0"
LABEL dockerfile.version="1"
LABEL software="pangolin"
LABEL software.version=${PANGOLIN_VER}
LABEL description="Conda environment for Pangolin. Pangolin: Software package for assigning SARS-CoV-2 genome sequences to global lineages."
LABEL website="https://github.com/cov-lineages/pangolin"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/cov-lineages/pangolin/blob/master/LICENSE.txt"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 git \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the pangolin repo
RUN wget "https://github.com/cov-lineages/pangolin/archive/${PANGOLIN_VER}.tar.gz" && \
 tar -xf ${PANGOLIN_VER}.tar.gz && \
 rm ${PANGOLIN_VER}.tar.gz && \
 mv -v pangolin-* pangolin

# set the environment
ENV PATH="$PATH" \
 LC_ALL=C.UTF-8

# modify environment.yml to pin specific versions during install
# create the conda environment using modified environment.yml and set as default
RUN sed -i "s|usher.*|usher=${USHER_VER}|" /pangolin/environment.yml && \
 sed -i "s|pangoLEARN.git|pangoLEARN.git@${PANGOLEARN_VER}|" /pangolin/environment.yml && \
 sed -i "s|scorpio.git|scorpio.git@${SCORPIO_VER}|" /pangolin/environment.yml && \
 sed -i "s|constellations.git|constellations.git@${CONSTELLATIONS_VER}|" /pangolin/environment.yml && \
 sed -i "s|pango-designation.git|pango-designation.git@${PANGO_DESIGNATION_VER}|" /pangolin/environment.yml && \
 micromamba create -n pangolin -y -f /pangolin/environment.yml

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /pangolin
RUN pip install . && \
 micromamba clean -a -y && \
 mkdir /data && \
 pangolin --all-versions && \
 usher --version

WORKDIR /data

# hardcode pangolin executable into the PATH variable
ENV PATH="$PATH:/opt/conda/envs/pangolin/bin/"

# new base for testing
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

ADD https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa /test-data/SRR13957123.consensus.fa 

RUN pangolin /test-data/SRR13957123.consensus.fa -o /test-data/SRR13957123-plearn && \
 pangolin /test-data/SRR13957123.consensus.fa -o /test-data/SRR13957123-pusher --usher && \
 cat /test-data/SRR13957123-p*/*.csv

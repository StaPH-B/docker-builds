FROM mambaorg/micromamba:0.22.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags.
# using pangolin-data github tag, NOT what is in the GH release title "v1.2.133"
ARG PANGOLIN_VER="v4.0.6"
ARG PANGOLIN_DATA_VER="v1.9"
ARG SCORPIO_VER="v0.3.17"
ARG CONSTELLATIONS_VER="v0.1.10"
ARG USHER_VER="0.5.4"

# metadata labels
LABEL base.image="mambaorg/micromamba:0.22.0"
LABEL dockerfile.version="4"
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
# create the conda environment using modified environment.yml
RUN sed -i "s|usher.*|usher=${USHER_VER}|" /pangolin/environment.yml && \
 sed -i "s|scorpio.git|scorpio.git@${SCORPIO_VER}|" /pangolin/environment.yml && \
 sed -i "s|pangolin-data.git|pangolin-data.git@${PANGOLIN_DATA_VER}|" /pangolin/environment.yml && \
 sed -i "s|constellations.git|constellations.git@${CONSTELLATIONS_VER}|" /pangolin/environment.yml && \
 micromamba create -n pangolin -y -f /pangolin/environment.yml

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /pangolin

# run pip install step; download optional pre-computed assignment hashes for UShER (useful for running on large batches of samples)
# best to skip using the assigment-cache if running on one sample for speed
# print versions
##### NOTE: 'pangolin --all-versions' does not accurately print the pangolin-data or pangolin-assignment version as it prints the version in 
##### /pangolin-data/pangolin-data/__init__.py instead of the GH tag (which is actually used for downloading)
##### See here for more info/explanation: https://github.com/cov-lineages/pangolin/issues/393
RUN pip install . && \
 pangolin --add-assignment-cache && \
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

# test on test sequences supplied with Pangolin code
RUN pangolin /pangolin/pangolin/test/test_seqs.fasta --analysis-mode usher -o /data/test_seqs-output-pusher && \
 cat /data/test_seqs-output-pusher/lineage_report.csv 

# test functionality of assignment-cache option
RUN pangolin --use-assignment-cache /pangolin/pangolin/test/test_seqs.fasta

# download B.1.1.7 genome from Utah
ADD https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa /test-data/SRR13957123.consensus.fa

# test on a B.1.1.7 genome
RUN pangolin /test-data/SRR13957123.consensus.fa --analysis-mode usher -o /test-data/SRR13957123-pusher && \
 cat /test-data/SRR13957123-pusher/lineage_report.csv

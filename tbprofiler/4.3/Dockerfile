# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM --platform=linux/x86_64 mambaorg/micromamba:0.24.0 as app

USER root
WORKDIR /
ARG TBPROFILER_VER="4.3"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="micromamba:0.24.0"
LABEL dockerfile.version="1"
LABEL software="tbprofiler"
LABEL software.version=$TBPROFILER_VER
LABEL description="The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database."
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# RUN executes code during the build
# Install dependencies via apt-get

RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

 RUN micromamba install --yes --name base --channel conda-forge --channel bioconda  \
     tb-profiler && \
     micromamba clean --all --yes

ARG MAMBA_DOCKERFILE_ACTIVATE=1
WORKDIR /data

FROM app as test

ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN tb-profiler version

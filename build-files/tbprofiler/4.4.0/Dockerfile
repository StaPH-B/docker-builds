# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM --platform=linux/x86_64 mambaorg/micromamba:0.24.0 as app

USER root
WORKDIR /
ARG TBPROFILER_VER="4.4.0"
ARG TBDB_VER="c2fb9a2"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="micromamba:0.24.0"
LABEL dockerfile.version="2"
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
     tb-profiler=${TBPROFILER_VER} && \
    micromamba clean --all --yes


ARG MAMBA_DOCKERFILE_ACTIVATE=1
# Version of database can be confirmed at ./TBProfiler-${TBPROFILER_VER}/db/tbdb.version.json
RUN tb-profiler update_tbdb

ENV MAMBA_DOCKERFILE_ACTIVATE=1
WORKDIR /data

ENV PATH="/opt/conda/bin:${PATH}"


FROM app as test

RUN mkdir test_run && \
    cd test_run && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_2.fastq.gz && \
    tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 4 -p ERR1664619 --txt

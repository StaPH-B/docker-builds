# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM mambaorg/micromamba:1.3.0 as app

USER root
WORKDIR /
ARG TBPROFILER_VER="4.4.2"
# this version is the shortened commit hash on the `master` branch here https://github.com/jodyphelan/tbdb/
# this was the latest commit as of 2023-02-17
ARG TBDB_VER="5f3c51e"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="micromamba:1.3.0"
LABEL dockerfile.version="1"
LABEL software="tbprofiler"
LABEL software.version="${TBPROFILER_VER}"
LABEL description="The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database."
LABEL website="https://github.com/jodyphelan/TBProfiler/"
LABEL license="https://github.com/jodyphelan/TBProfiler/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"
LABEL maintainer2="Curtis kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install tb-profiler via bioconda; install into 'base' conda env
 RUN micromamba install --yes --name base --channel conda-forge --channel bioconda  \
     tb-profiler=${TBPROFILER_VER} && \
     micromamba clean --all --yes

# this ARG is so that the conda env is activated for running the following command
ARG MAMBA_DOCKERFILE_ACTIVATE=1
# Version of database can be confirmed at /opt/conda/share/tbprofiler/tbdb.version.json
# can also run 'tb-profiler list_db' to find the same version info
RUN tb-profiler update_tbdb --commit ${TBDB_VER}

# ensure conda environment is always active for the user
ENV MAMBA_DOCKERFILE_ACTIVATE=1
WORKDIR /data

# hardcode 'base' env bin into PATH, so conda env does not have to be "activated" at run time
ENV PATH="/opt/conda/bin:${PATH}"

# test stage
FROM app as test

# download some TB FASTQs and run through tb-profiler
RUN mkdir test_run && \
    cd test_run && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_2.fastq.gz && \
    tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 2 -p ERR1664619 --txt

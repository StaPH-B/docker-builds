FROM mambaorg/micromamba:2.5.0-ubuntu22.04 AS app

ARG BYGUL_SOFTWARE_VERSION="4.0.5"

USER root
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Bygul"
LABEL software.version=${BYGUL_SOFTWARE_VERSION}
LABEL description="Bygul: Amplicon & Metagenomics Read Simulator"
LABEL website="https://github.com/andersen-lab/Bygul"
LABEL license="https://github.com/andersen-lab/Bygul/blob/main/LICENSE"
LABEL maintainer="Maryam Ahmadi Jeshvaghane | ANDERSEN LAB | Scripps research institute"
LABEL maintainer.email="mahmadi@scripps.edu"

# Ensure Conda bin directory is primary in PATH
ENV PATH="/opt/conda/envs/bygul-env/bin:${PATH}" \
    LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1

# Install Bygul and simulation backends (wgsim, mason) from Bioconda
RUN micromamba create -n bygul-env -c conda-forge -c bioconda \
        bygul=${BYGUL_SOFTWARE_VERSION} && \
    micromamba clean -a -y -f && \
    mkdir /data


# NOTE: this will download the latest version of the `freyja/data/usher_barcodes.csv` file from GitHub
RUN bygul simulate-proportions --help

# set working directory to /data
WORKDIR /data

RUN pwd
# make directory editable
RUN chmod -R 777 /data

# default command is to pull up help options
CMD [ "bygul", "--help" ]

# new base for testing
FROM app AS test

RUN bygul --help && bygul --version

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    git && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -P /data https://raw.githubusercontent.com/andersen-lab/Bygul/refs/heads/main/bygul/tests/data/ATM-2FFMD73N3.fasta && \
    wget -P /data https://raw.githubusercontent.com/andersen-lab/Bygul/refs/heads/main/bygul/tests/data/CA-SEARCH-43254.fasta && \
    wget -P /data https://raw.githubusercontent.com/andersen-lab/Bygul/refs/heads/main/bygul/tests/data/ARTIC_V4-1.bed


# Run Bygul
RUN bygul simulate-proportions --genomes /data/ATM-2FFMD73N3.fasta,/data/CA-SEARCH-43254.fasta --primers /data/ARTIC_V4-1.bed --outdir /data/results

# Check validity of outputs
RUN head /data/results/reads_1.fastq | \
    grep "@" > /data/results/test_bygul.txt

RUN bygul check-primers /data/ATM-2FFMD73N3.fasta /data/ARTIC_V4-1.bed --outdir /data/results

# Check validity of outputs
RUN head /data/results/amplicon_stats.csv | \
    grep "ATM-2FFMD73N3" > /data/results/test_bygul.txt


# print bygul version
RUN bygul --version

# list installed deps
RUN micromamba list -n bygul-env

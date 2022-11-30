FROM mambaorg/micromamba:1.0.0 as app

# Version arguments
# ARG variables only persist during build time
ARG PASTY_VERSION="1.0.0"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:1.0.0"
LABEL dockerfile.version="1"
LABEL software="pasty"
LABEL software.version="${PASTY_VERSION}"
LABEL description="In silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies"
LABEL website="https://github.com/rpetit3/pasty"
LABEL license="https://github.com/rpetit3/pasty/blob/main/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="curtis.kapsak@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install pasty into the base conda/micromamba environment, pinning the version
# clean up conda garbage
RUN micromamba install --name base -c conda-forge -c bioconda -c defaults pasty=${PASTY_VERSION} && \
 micromamba clean -a -y

# set the environment, add base conda/micromamba bin directory into path
# set locale settings to UTF-8
ENV PATH="/opt/conda/bin/:\
${PATH}" \
 LC_ALL=C.UTF-8

# set final working directory to /data
WORKDIR /data

# new base for testing
FROM app as test

# # so that mamba/conda env is active when running below commands
ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# # so that all test inputs & outputs are kept in /test
WORKDIR /test

# download test data from pasty repo
RUN wget -q https://github.com/rpetit3/pasty/raw/main/test/NT-GCF_000292685.fna.gz && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/O1-GCA_000705235.fna.gz && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/O2-GCF_000006765.fna.gz && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/O6-GCF_000817165.fna.gz && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/O7-GCF_000647615.fna.gz && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/empty.fasta && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/not-a-fasta.fasta && \
    wget -q https://github.com/rpetit3/pasty/raw/main/test/poor.fasta 

# shamelessly stolen and modified from https://github.com/rpetit3/pasty/blob/main/.github/workflows/test-pasty.yml
RUN echo "O1-GCA_000705235" && \
    pasty --assembly /test/O1-GCA_000705235.fna.gz --prefix O1-GCA_000705235 && \
    cat O1-GCA_000705235.tsv && \
    cat O1-GCA_000705235.details.tsv && \
    echo "O2-GCF_000006765" && \
    pasty --assembly /test/O2-GCF_000006765.fna.gz --prefix O2-GCF_000006765 --outdir O2 && \
    cat O2/O2-GCF_000006765.tsv && \
    cat O2/O2-GCF_000006765.details.tsv  && \
    echo "O6-GCF_000817165" && \
    pasty --assembly /test/O6-GCF_000817165.fna.gz --prefix O6-GCF_000817165 && \
    cat O6-GCF_000817165.tsv && \
    cat O6-GCF_000817165.details.tsv && \
    echo "O7-GCF_000647615" && \
    pasty --assembly /test/O7-GCF_000647615.fna.gz --prefix O7-GCF_000647615 && \
    cat O7-GCF_000647615.tsv && \
    cat O7-GCF_000647615.details.tsv && \
    echo "NT-GCF_000292685" && \
    pasty --assembly /test/NT-GCF_000292685.fna.gz --prefix NT-GCF_000292685 && \
    cat NT-GCF_000292685.tsv && \
    cat NT-GCF_000292685.details.tsv && \
    echo "empty" && \
    pasty --assembly /test/empty.fasta --prefix empty && \
    cat empty.tsv && \
    cat empty.details.tsv && \
    echo "not-a-fasta" && \
    pasty --assembly /test/not-a-fasta.fasta --prefix not-a-fasta && \
    cat not-a-fasta.tsv && \
    cat not-a-fasta.details.tsv && \
    echo "poor" && \
    pasty --assembly /test/poor.fasta --prefix poor --outdir poor && \
    cat poor/poor.tsv && \
    cat poor/poor.details.tsv

# print help and version info; check dependencies
RUN pasty --help && \
    pasty --version

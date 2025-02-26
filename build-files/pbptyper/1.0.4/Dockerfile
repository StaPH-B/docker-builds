FROM mambaorg/micromamba:0.24.0 as app

# Version arguments
# ARG variables only persist during build time
ARG PBPTYPER_VERSION="1.0.4"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:0.24.0"
LABEL dockerfile.version="1"
LABEL software="pbptyper"
LABEL software.version="${PBPTYPER_VERSION}"
LABEL description="In silico Penicillin Binding Protein (PBP) typer for Streptococcus pneumoniae assemblies"
LABEL website="https://github.com/rpetit3/pbptyper"
LABEL license="https://github.com/rpetit3/pbptyper/blob/main/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="curtis.kapsak@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install pbptyper into the base conda/micromamba environment, pinning the version
# clean up conda garbage
RUN micromamba install --name base -c conda-forge -c bioconda -c defaults pbptyper=${PBPTYPER_VERSION} && \
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

# download test data from pbptyper repo
RUN wget https://github.com/rpetit3/pbptyper/raw/main/test/SRR2912551.fna.gz && \
    wget https://github.com/rpetit3/pbptyper/raw/main/test/SRR8654742.fna && \
    wget https://github.com/rpetit3/pbptyper/blob/main/test/empty.fasta && \
    wget https://github.com/rpetit3/pbptyper/blob/main/test/not-a-fasta.fasta && \
    wget https://github.com/rpetit3/pbptyper/blob/main/test/not-spn.fna.gz && \
    wget https://github.com/rpetit3/pbptyper/blob/main/test/poor.fasta

# shamelessly stolen and modified from https://github.com/rpetit3/pbptyper/blob/main/.github/workflows/test-pbptyper.yml
RUN echo "SRR2912551" && \
    pbptyper --assembly /test/SRR2912551.fna.gz --prefix SRR2912551 && \
    cat SRR2912551.tsv && \
    head SRR2912551-1A.tblastn.tsv && \
    head SRR2912551-2B.tblastn.tsv && \
    head SRR2912551-2X.tblastn.tsv && \
    echo "SRR8654742" && \
    pbptyper --assembly /test/SRR8654742.fna --prefix SRR8654742 && \
    cat SRR8654742.tsv && \
    head SRR8654742-1A.tblastn.tsv && \
    head SRR8654742-2B.tblastn.tsv && \
    head SRR8654742-2X.tblastn.tsv && \
    echo "not-spn" && \
    pbptyper --assembly /test/not-spn.fna.gz --prefix not-spn && \
    cat not-spn.tsv && \
    head not-spn-1A.tblastn.tsv && \
    head not-spn-2B.tblastn.tsv && \
    head not-spn-2X.tblastn.tsv && \
    echo "empty" && \
    pbptyper --assembly /test/empty.fasta --prefix empty && \
    cat empty.tsv && \
    head empty-1A.tblastn.tsv && \
    head empty-2B.tblastn.tsv && \
    head empty-2X.tblastn.tsv && \
    echo "not-a-fasta" && \
    pbptyper --assembly /test/not-a-fasta.fasta --prefix not-a-fasta && \
    cat not-a-fasta.tsv && \
    head not-a-fasta-1A.tblastn.tsv && \
    head not-a-fasta-2B.tblastn.tsv && \
    head not-a-fasta-2X.tblastn.tsv && \
    echo "poor" && \
    pbptyper --assembly /test/poor.fasta --prefix poor && \
    cat poor.tsv && \
    head poor-1A.tblastn.tsv && \
    head poor-2B.tblastn.tsv && \
    head poor-2X.tblastn.tsv

# print help and version info; check dependencies
RUN pbptyper --help && \
 pbptyper --check && \
 pbptyper --version

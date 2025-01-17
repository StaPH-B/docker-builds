FROM mambaorg/micromamba:1.4.1 as app

USER root

WORKDIR /

ARG DNAAPLER_VER="0.5.0"

# metadata labels
LABEL base.image="mambaorg/micromamba:1.4.1"
LABEL dockerfile.version="1"
LABEL software="dnaapler"
LABEL software.version="${DNAAPLER_VER}"
LABEL description="Rotates chromosomes and more"
LABEL website="https://github.com/gbouras13/dnaapler"
LABEL license="MIT"
LABEL license.url="https://github.com/gbouras13/dnaapler/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# create the conda environment, install mykrobe via bioconda package; cleanup conda garbage
RUN micromamba create -n dnaapler -y -c bioconda -c defaults -c conda-forge dnaapler=${DNAAPLER_VER} && \
    micromamba clean -a -y

# set the PATH and LC_ALL for singularity compatibility
ENV PATH="/opt/conda/envs/dnaapler/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# set final working directory as /data
WORKDIR /data

# default command is to print help options
CMD [ "dnaapler", "--help" ]

# new base for testing
FROM app as test

# set working directory to /test
WORKDIR /test

# checking that tool is in PATH
RUN dnaapler --help && dnaapler --version

# downloads genome sequence and then extracts the last plasmid in the laziest way possible
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/025/259/185/GCA_025259185.1_ASM2525918v1/GCA_025259185.1_ASM2525918v1_genomic.fna.gz && \
    gunzip GCA_025259185.1_ASM2525918v1_genomic.fna.gz && \
    grep "CP104365.1" GCA_025259185.1_ASM2525918v1_genomic.fna -A 50000 > CP104365.1.fasta && \
    dnaapler mystery --prefix mystery_test --output mystery_test -i CP104365.1.fasta && \ 
    dnaapler plasmid --prefix plasmid_test --output plasmid_test -i CP104365.1.fasta && \
    ls mystery_test plasmid_test

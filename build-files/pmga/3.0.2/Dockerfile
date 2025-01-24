# Base Image
FROM ubuntu:focal

ARG PMGA_VERSION="3.0.2"
ARG MASH_VERSION="1.1"

# Metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="pmga"
LABEL software.version="3.0.1"
LABEL description="A command-line version of PMGA (PubMLST Genome Annotator) for serotyping, serotyping and MLST of all Neisseria species and Haemophilus influenzae"
LABEL website="https://github.com/rpetit3/pmga"
LABEL license="https://github.com/rpetit3/pmga/blob/master/LICENSE"
LABEL maintainer="Robert A. Petit III"
LABEL maintainer.email="robert.petit@theiagen.com"

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        ncbi-blast+ \
        pigz \
        wget && \
    pip3 install biopython>=1.78 executor requests && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install Mash
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VERSION}/mash-Linux64-v${MASH_VERSION}.tar.gz && \
    tar -xvf mash-Linux64-v${MASH_VERSION}.tar.gz && \
    rm -rf mash-Linux64-v${MASH_VERSION}.tar && \
    mv /mash-Linux64-v${MASH_VERSION} /mash

# Install PMGA
RUN wget https://github.com/rpetit3/pmga/archive/refs/tags/v${PMGA_VERSION}.tar.gz && \
    tar -xzf v${PMGA_VERSION}.tar.gz && \
    rm v${PMGA_VERSION}.tar.gz && \
    mv pmga-${PMGA_VERSION} /pmga && \
    cp /pmga/pmga.py /pmga/pmga && \
    cp /pmga/pmga-build.py /pmga/pmga-build && \
    cd /pmga && \
    /pmga/pmga-build --outdir blastdbs && \
    mkdir /data

ENV PATH="/mash:/pmga:${PATH}"

WORKDIR /data

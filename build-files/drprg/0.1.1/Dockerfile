# 'FROM' defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. The production image uses everything to the 'app' stage.
FROM mambaorg/micromamba:1.5.1 as app

# List all software versions are ARGs near the top of the dockerfile
# 'ARG' sets environment variables during the build stage
ARG DRPRG_VER="0.1.1"
ARG MTB_VER="20230308"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user

LABEL base.image="mambaorg/micromamba:1.4.9"
LABEL dockerfile.version="1"
LABEL software="Dr. PRG"
LABEL software.version="${DRPRG_VER}"
LABEL description="Antimicrobial resistance prediction"
LABEL website="https://github.com/mbhall88/drprg"
LABEL license="https://github.com/mbhall88/drprg/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install your desired software into the base conda/micromamba environment, pinning the version
# clean up conda garbage
# make /data to use as a working directory
RUN micromamba install --name base -c conda-forge -c bioconda -c defaults drprg=${DRPRG_VER} && \
    micromamba clean -a -y && \
    mkdir /data

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# set the environment, add base conda/micromamba bin directory into path
# set locale settings to UTF-8
ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# download MTB index and change the name
RUN mkdir /drprg && \
    drprg index --download mtb@${MTB_VER} --outdir /drprg && \
    mv /drprg/mtb/mtb-${MTB_VER} /drprg/mtb/mtb
    
CMD drprg --help

WORKDIR /data

FROM app as test

WORKDIR /test

RUN drprg --help

# testing prediction
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR230/005/SRR23086705/SRR23086705_1.fastq.gz && \
    drprg predict -x /drprg/mtb/mtb -i SRR23086705_1.fastq.gz --illumina -o outdir/ && \
    ls outdir/*

# list available databases for download
RUN drprg index --list
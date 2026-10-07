# sourced from https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile_mamba
FROM mambaorg/micromamba:2.9.0-ubuntu24.04 AS app

ARG SEQSENDER_VERSION=1.5.1

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.9.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="SeqSender"
LABEL software.version="${SEQSENDER_VERSION}"
LABEL description="Python program that automates the process of generating submission files and batch uploading to NCBI archives and GISAID databases"
LABEL website="https://github.com/CDCgov/seqsender"
LABEL license="https://github.com/CDCgov/seqsender/blob/master/LICENSE"
LABEL maintainer="Vincent Tu"
LABEL maintainer.email="vincent.tu@phila.gov"

# install dependencies and cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    libsqlite3-0 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download source code; make /data
RUN wget -q https://github.com/CDCgov/seqsender/archive/refs/tags/v${SEQSENDER_VERSION}.tar.gz && \
  tar -xzf v${SEQSENDER_VERSION}.tar.gz && \
  rm -r v${SEQSENDER_VERSION}.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C.UTF-8 \
  PATH=/opt/conda/bin/:${PATH}:/seqsender-${SEQSENDER_VERSION}

# Clean hardcoded package build hashes from env.yaml, then install with compatible versions
RUN sed -i -E 's/=[^ ]+//g' "/seqsender-${SEQSENDER_VERSION}/env.yaml" && \
    micromamba install --yes --name base -f "/seqsender-${SEQSENDER_VERSION}/env.yaml" \
    python=3.10 beartype "pandera=0.18.3" "numpy<2" && \
    micromamba clean --all --force-pkgs-dirs --yes
    
# default command is to pull up help options
CMD ["seqsender.py", "--help"]

# set working directory to /data
WORKDIR /data

# test layer
# test layer
FROM app AS test

WORKDIR /seqsender-${SEQSENDER_VERSION}

# print version and grep for it; if not found, exit with error
RUN seqsender.py --help && \
    seqsender.py version

# generate test data for FLU and COV and check if directories are created
# generate test data for FLU and COV and check if directories are created; otherwise exit with error
RUN for org in FLU COV; \
  do seqsender.py test_data --biosample --sra --genbank --organism "${org}" --submission_dir /data/test_dir && \
     test -d "/data/test_dir/${org}_TEST_DATA/" || exit 1; \
  done

# test network connection
RUN seqsender.py test_network_connection | \
    grep "No network connection issues detected" || exit 1

RUN micromamba list -n base


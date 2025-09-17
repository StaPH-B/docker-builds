# sourced from https://github.com/StaPH-B/docker-builds/blob/master/dockerfile-template/Dockerfile_mamba
FROM mambaorg/micromamba:2.3.1-ubuntu22.04 AS app

ARG SEQSENDER_VERSION=1.3.4

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.1-ubuntu22.04"
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
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download source code; make /data
RUN wget -q https://github.com/CDCgov/seqsender/archive/refs/tags/v${SEQSENDER_VERSION}.tar.gz && \
  tar -xzf v${SEQSENDER_VERSION}.tar.gz && \
  rm -r v${SEQSENDER_VERSION}.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C.UTF-8 \
  PATH=/opt/conda/bin/:${PATH}:/seqsender-${SEQSENDER_VERSION}

# increase number of open files
# install software into the base micromamba environment, pinning the version
# clean up conda garbage
RUN ulimit -n 65536 && \
  micromamba install --yes --name base -f "/seqsender-${SEQSENDER_VERSION}/env.yaml" && \
  micromamba clean --all --yes 

# default command is to pull up help options
CMD ["seqsender.py", "--help"]

# set working directory to /data
WORKDIR /data

# test layer
FROM app AS test

# print version and grep for it; if not found, exit with error
RUN seqsender.py --help && \
  seqsender.py version | \
  grep "Version: ${SEQSENDER_VERSION}" || exit 1

# generate test data for FLU and COV and check if directories are created; otherwise exit with error
RUN for org in FLU COV; \
  do seqsender.py test_data -bsng --organism "${org}" --submission_dir test_dir && \
    test -d "test_dir/${org}_TEST_DATA/" || exit 1; \
  done

# test network connection
RUN seqsender.py test_network_connection | \
  grep "No network connection issues detected" || exit 1

RUN micromamba list -n base

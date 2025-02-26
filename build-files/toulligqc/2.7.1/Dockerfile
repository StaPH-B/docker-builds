FROM python:3.11.11-slim AS app

ARG TOULIGQC_VER="2.7.1"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="python:3.11.11-slim"
LABEL dockerfile.version="1"
LABEL software="ToulligQC"
LABEL software.version="${TOULIGQC_VER}"
LABEL description="QC analyses of Oxford Nanopore runs"
LABEL website="https://github.com/GenomiqueENS/toulligQC"
LABEL license="https://github.com/GenomiqueENS/toulligQC/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates\
    procps \
    bzip2 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/GenomiqueENS/toulligQC/archive/refs/tags/v${TOULIGQC_VER}.tar.gz && \
    pip install --no-cache-dir v${TOULIGQC_VER}.tar.gz && \
    rm -rf v${TOULIGQC_VER}.tar.gz

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="$PATH" \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "toulligqc", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app AS test

ARG TOULIGQC_VER

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN toulligqc --help && \
    toulligqc --version

RUN wget -q http://outils.genomique.biologie.ens.fr/leburon/downloads/toulligqc-example/toulligqc_demo_data.tar.bz2 && \
    tar -xvjf toulligqc_demo_data.tar.bz2 && \
    cd toulligqc_demo_data && \
    ./run-toulligqc.sh && \
    ls /test/toulligqc_demo_data/output/ToulligQC_Demo_Data/report.html \
    /test/toulligqc_demo_data/output/ToulligQC_Demo_Data/report.data \
    /test/toulligqc_demo_data/output/ToulligQC_Demo_Data/images/*html

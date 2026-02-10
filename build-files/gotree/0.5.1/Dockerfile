
ARG GOTREE_VER="0.5.1"
# 'FROM' defines where the Dockerfile is starting to build from.
FROM ubuntu:jammy AS app

# List all software versions are ARGs near the top of the dockerfile
ARG GOTREE_VER

# 'LABEL' instructions tag the image with metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="gotree"
LABEL software.version="${GOTREE_VER}"
LABEL description="GoTree is a set of command line tools to manipulate phylogenetic trees"
LABEL website="https://github.com/evolbioinfo/gotree"
LABEL license="https://github.com/evolbioinfo/gotree/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies: wget is needed to download the binary
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install gotree
# GoTree is distributed as a single binary, so we download it, make it executable, and move it to /usr/local/bin
RUN wget https://github.com/evolbioinfo/gotree/releases/download/v${GOTREE_VER}/gotree_v${GOTREE_VER}_amd64_linux && \
    mv gotree_v${GOTREE_VER}_amd64_linux /usr/local/bin/gotree && \
    chmod +x /usr/local/bin/gotree && \
    mkdir /data

# 'CMD' instructions set a default command
CMD [ "gotree", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

FROM app AS test

ARG GOTREE_VER

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# Basic executable check
RUN gotree --help && \
    gotree version

RUN wget https://github.com/evolbioinfo/gotree/archive/refs/tags/v${GOTREE_VER}.tar.gz && \
    tar -xvf v${GOTREE_VER}.tar.gz && \
    cd gotree-${GOTREE_VER} && \
    sed -i 's|GOTREE=\./gotree|GOTREE=gotree|g' test.sh && \
    bash test.sh

# Functional test: Generate a random tree and calculate stats
# This ensures the binary actually performs calculation tasks
RUN gotree generate uniformtree -l 100 -n 10 | gotree stats
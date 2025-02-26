FROM ubuntu:jammy as app

ARG CORESNPFILTER_VER="0.2.0"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Core-SNP-filter"
LABEL software.version="${CORESNPFILTER_VER}"
LABEL description="This is a tool to filter sites (i.e. columns) in a FASTA-format whole-genome pseudo-alignment"
LABEL website="https://github.com/rrwick/Core-SNP-filter"
LABEL license="https://github.com/rrwick/Core-SNP-filter/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

RUN wget -q https://github.com/rrwick/Core-SNP-filter/releases/download/v${CORESNPFILTER_VER}/coresnpfilter-linux-x86_64-musl-v${CORESNPFILTER_VER}.tar.gz && \
    tar -vxf coresnpfilter-linux-x86_64-musl-v${CORESNPFILTER_VER}.tar.gz && \
    rm -rf coresnpfilter-linux-x86_64-musl-v${CORESNPFILTER_VER}.tar.gz

ENV LC_ALL=C

CMD [ "coresnpfilter", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN coresnpfilter --help && \
    coresnpfilter --version

RUN wget -q https://github.com/rrwick/Core-SNP-filter/raw/refs/heads/main/demo.fasta.gz && \
    coresnpfilter -e -c 0.95 demo.fasta.gz > demo_core.fasta && \
    head demo_core.fasta
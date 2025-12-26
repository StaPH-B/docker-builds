FROM ubuntu:jammy AS app

ARG SOFTWARENAME_VER="0.1.0.232"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Spestimator"
LABEL software.version="${SOFTWARENAME_VER}"
LABEL description="Uses 16S to identify a range of possible species."
LABEL website="https://github.com/erinyoung/Spestimator"
LABEL license="https://github.com/erinyoung/Spestimator/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    ncbi-blast+ \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir spestimator==${SOFTWARENAME_VER} && \
    spestimator -h && \
    mkdir /data

ENV LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "spestimator", "-h" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN spestimator --help && \
    spestimator --version

RUN apt-get update && apt-get install -y wget

RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/900/636/985/GCF_900636985.1_45889_C01/GCF_900636985.1_45889_C01_genomic.fna.gz && \
    gunzip GCF_900636985.1_45889_C01_genomic.fna.gz && \
    spestimator -i *.fna -o testing.csv --download-genomes genomes && \
    head testing.csv && \
    ls genomes/* | wc -l

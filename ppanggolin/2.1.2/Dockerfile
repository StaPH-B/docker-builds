ARG PPANGGOLIN_VER="2.1.2"

FROM mambaorg/micromamba:1.5.8 as app

ARG PPANGGOLIN_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="PPanGGOLiN"
LABEL software.version="${PPANGGOLIN_VER}"
LABEL description="Depicting microbial species diversity via a Partitioned PanGenome Graph Of Linked Neighbors"
LABEL website="https://github.com/labgem/PPanGGOLiN"
LABEL license="https://github.com/labgem/PPanGGOLiN/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/conda/envs/base/bin/:/opt/conda/bin/:$PATH" LC_ALL=C

RUN micromamba install --name base -c conda-forge -c bioconda -c defaults ppanggolin=${PPANGGOLIN_VER} && \
    micromamba clean -a -f -y

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD ppanggolin -h

# 'WORKDIR' sets working directory
WORKDIR /data

FROM app as test

ARG PPANGGOLIN_VER

WORKDIR /test

RUN ppanggolin --help && \
    ppanggolin --version

# getting test files from github repo
RUN wget -q https://github.com/labgem/PPanGGOLiN/archive/refs/tags/${PPANGGOLIN_VER}.tar.gz && \
    tar -xvf ${PPANGGOLIN_VER}.tar.gz

RUN cd PPanGGOLiN-${PPANGGOLIN_VER}/testingDataset && \
    ppanggolin all --fasta genomes.fasta.list --output output

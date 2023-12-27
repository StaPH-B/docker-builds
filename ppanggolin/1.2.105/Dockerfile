ARG PPANGGOLIN_VER="1.2.105"

FROM mambaorg/micromamba:1.4.9 as app

ARG PPANGGOLIN_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:1.4.9"
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
    micromamba clean -a -y && \
    ppanggolin -h && \
    mkdir /data

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
    ppanggolin annotate --fasta organisms.fasta.list --output output && cp output/pangenome.h5 output/pangenome.1.h5 && \
    ppanggolin cluster   -p output/pangenome.h5                      && cp output/pangenome.h5 output/pangenome.2.h5 && \
    ppanggolin graph     -p output/pangenome.h5                      && cp output/pangenome.h5 output/pangenome.3.h5 && \
    ppanggolin partition -p output/pangenome.h5                      && cp output/pangenome.h5 output/pangenome.4.h5 && \
    ppanggolin draw      -p output/pangenome.h5 --ucurve             && \
    ppanggolin write     -p output/pangenome.h5 --stats --output output_stats && \
    md5sum output/pangenome*.h5 && \
    head output_stats/*


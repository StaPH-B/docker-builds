FROM mambaorg/micromamba:2.9.0-ubuntu24.04 AS app

ARG LONGREADSUM_VERSION="1.6.0"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.9.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="LONGREADSUM"
LABEL software.version="${LONGREADSUM_VERSION}"
LABEL description="A fast and flexible QC tool for long read sequencing data"
LABEL website="https://github.com/WGLab/LongReadSum"
LABEL license="https://github.com/WGLab/LongReadSum/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN micromamba install --name base -c wglab -c conda-forge -c jannessp -c bioconda python=3.9 longreadsum=${LONGREADSUM_VERSION} && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8 \
    CONDA_PREFIX="/opt/conda"

CMD [ "longreadsum", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y \
    wget

RUN micromamba list -n base

RUN longreadsum --help

RUN wget -q --no-check-certificate https://downloads.pacbcloud.com/public/dataset/2021-11-Microbial-96plex/demultiplexed-reads/m64004_210929_143746.bc2062.bam &&\
    longreadsum bam -t 4 -i m64004_210929_143746.bc2062.bam -o test





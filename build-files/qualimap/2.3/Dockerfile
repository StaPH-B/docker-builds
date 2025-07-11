FROM mambaorg/micromamba:2.0.8-ubuntu22.04 AS app

ARG QUALIMAP_VER="2.3"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.0.8-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="QualiMap"
LABEL software.version="${QUALIMAP_VER}"
LABEL description="the quality control of alignment sequencing data with GUI or CLI"
LABEL website="http://qualimap.conesalab.org/"
LABEL license="https://bitbucket.org/kokonech/qualimap/src/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN micromamba install --name base -c conda-forge -c bioconda bioconductor-repitools qualimap=${QUALIMAP_VER} && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "qualimap", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

WORKDIR /test

RUN qualimap --help

ADD https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123.sorted.bam SRR13957123.sorted.bam

RUN qualimap bamqc -bam SRR13957123.sorted.bam
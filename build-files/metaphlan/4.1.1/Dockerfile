FROM mambaorg/micromamba:1.5.8 as app

ARG METAPHLAN_VER="4.1.1"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="MetaPhlAn"
LABEL software.version="${METAPHLAN_VER}"
LABEL description="MetaPhlAn is a computational tool for species-level microbial profiling from metagenomic shotgun sequencing data"
LABEL website="https://github.com/biobakery/MetaPhlAn"
LABEL license="https://github.com/biobakery/MetaPhlAn/blob/master/license.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    procps &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda metaphlan=${METAPHLAN_VER} &&\
    micromamba clean -afy

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "metaphlan", "--help" ]

WORKDIR /data

## Test ##
FROM app as test

RUN metaphlan --help

# get test sample
RUN wget https://github.com/biobakery/MetaPhlAn/releases/download/4.1.0/SRS014476-Supragingival_plaque.fasta.gz
# download toy db
RUN metaphlan --install --index mpa_vJan21_TOY_CHOCOPhlAnSGB_202103 --bowtie2db /toy
# metaphlan test
RUN metaphlan SRS014476-Supragingival_plaque.fasta.gz --input_type fasta --bowtie2db /toy --index mpa_vJan21_TOY_CHOCOPhlAnSGB_202103 > test.txt &&\
    cat test.txt

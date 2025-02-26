FROM mambaorg/micromamba:1.5.9 AS app

ARG VERKKO_VER="2.2"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.9"
LABEL dockerfile.version="1"
LABEL software="Verkko"
LABEL software.version="${VERKKO_VER}"
LABEL description="Verkko is a hybrid genome assembly pipeline developed for telomere-to-telomere assembly of PacBio HiFi or Oxford Nanopore Duplex and Oxford Nanopore simplex reads."
LABEL website="https://github.com/marbl/verkko"
LABEL license="https://github.com/marbl/verkko/blob/master/README.licenses"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    procps &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda verkko=${VERKKO_VER} && \
    micromamba clean -afy

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "verkko", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

RUN verkko --help

RUN apt-get update && apt-get install --no-install-recommends -y curl

# test data
RUN curl -L https://obj.umiacs.umd.edu/sergek/shared/ecoli_hifi_subset24x.fastq.gz -o hifi.fastq.gz &&\
    curl -L https://obj.umiacs.umd.edu/sergek/shared/ecoli_ont_subset50x.fastq.gz -o ont.fastq.gz

# verkko test run
RUN verkko -d asm --hifi ./hifi.fastq.gz --nano ./ont.fastq.gz &&\
    head asm/assembly.hifi-coverage.csv &&\
    head -c 1000 asm/assembly.fasta


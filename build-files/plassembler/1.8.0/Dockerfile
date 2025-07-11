ARG PLASSEMBLER_VERSION="1.8.0"

FROM mambaorg/micromamba:2.3.0-ubuntu22.04 AS app

ARG PLASSEMBLER_VERSION

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="SOFTWARENAME"
LABEL software.version="${PLASSEMBLER_VERSION}"
LABEL description="Hybrid plasmid assembly"
LABEL website="https://github.com/gbouras13/plassembler"
LABEL license="https://github.com/gbouras13/plassembler/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda plassembler=${PLASSEMBLER_VERSION} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    TERM=xterm-256color \
    LC_ALL=C.UTF-8

CMD [ "plassembler", "--help" ]

# 440M size
RUN plassembler download -d /plassembler_db

WORKDIR /data

FROM app AS test

ARG PLASSEMBLER_VERSION

WORKDIR /test

RUN plassembler --help && \
    plassembler --version

RUN wget https://github.com/gbouras13/plassembler/archive/refs/tags/v${PLASSEMBLER_VERSION}.tar.gz && \
    tar -xvf v${PLASSEMBLER_VERSION}.tar.gz && \
    plassembler run \
        -l plassembler-${PLASSEMBLER_VERSION}/tests/test_data/end_to_end/case1.fastq.gz \
        -1 plassembler-${PLASSEMBLER_VERSION}/tests/test_data/end_to_end/input_R1.fastq.gz \
        -2 plassembler-${PLASSEMBLER_VERSION}/tests/test_data/end_to_end/input_R2.fastq.gz \
        -d /plassembler_db \
        -o output_test -t 4 -c 50000 && \
    ls output_test

RUN micromamba list -n base

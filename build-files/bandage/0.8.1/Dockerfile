FROM mambaorg/micromamba:1.5.6 as app

ARG BANDAGE_VERSION="0.8.1"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.6"
LABEL dockerfile.version="1"
LABEL software="bandage"
LABEL software.version="${BANDAGE_VERSION}"
LABEL description="Bandage is a program for visualising de novo assembly graphs."
LABEL website="https://rrwick.github.io/Bandage/"
LABEL license="https://github.com/rrwick/Bandage?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    ffmpeg \
    libsm6 \
    libxext6 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda -c defaults bandage=${BANDAGE_VERSION} && \
    micromamba clean -a -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "Bandage", "--help" ]

WORKDIR /data

FROM app as test

WORKDIR /test

RUN Bandage --help && \
    Bandage --version

RUN wget -q https://raw.githubusercontent.com/rrwick/Bandage/main/tests/test_query_paths.gfa && \
    Bandage image test_query_paths.gfa test.png && \
    ls test.png


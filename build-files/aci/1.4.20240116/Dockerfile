FROM python:3.9.17-slim as app

ARG ACI_VER="1.4.20240116"

LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="ACI"
LABEL software.version="${ACI_VER}"
LABEL description="Visualize Amplicon Coverage/Depth"
LABEL website="https://github.com/erinyoung/ACI"
LABEL license="https://github.com/erinyoung/ACI?tab=MIT-1-ov-file#readme"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache amplicon_coverage_inspector==${ACI_VER}

ENV PATH="$PATH" \
    LC_ALL=C

CMD [ "aci", "--help" ]

WORKDIR /data

FROM app as test

WORKDIR /test

RUN aci --help && \
    aci --version

RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget -q https://github.com/erinyoung/ACI/raw/main/tests/data/test.bam && \
    wget -q https://raw.githubusercontent.com/erinyoung/ACI/main/tests/data/test.bed && \
    aci --bam test.bam --bed test.bed --out out && \
    ls out/*

FROM python:3.11-slim as app

ARG CIRCULOCOV_VER="0.1.20240104"
ARG MINIMAP2_VER="2.26"

LABEL base.image="python:3.11-slim"
LABEL dockerfile.version="1"
LABEL software="CirculoCov"
LABEL software.version="${CIRCULOCOV_VER}"
LABEL description="Circular-aware coverage estimations"
LABEL website="https://github.com/erinyoung/CirculoCov"
LABEL license="https://github.com/erinyoung/CirculoCov/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    bzip2 \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install circulocov via pip
RUN pip install --no-cache circulocov==${CIRCULOCOV_VER}

# install minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner && \
    mkdir /data

ENV PATH="/minimap2-${MINIMAP2_VER}_x64-linux/:$PATH" \
    LC_ALL=C

CMD [ "circulocov", "--help" ]

WORKDIR /data

FROM app as test

WORKDIR /test

RUN circulocov --help && \
    circulocov --version

RUN apt-get update && apt-get install -y --no-install-recommends wget

# downloads some SARS-CoV-2 data
RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
    wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    circulocov -g SRR13957123.consensus.fa -i SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz -o out && \
    ls out/* && \
    circulocov -g SRR13957123.consensus.fa -i SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz -o out_all -a && \
    ls out_all/* && ls out_all/fastq/*

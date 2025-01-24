FROM ubuntu:jammy as app

ARG PANGO_ALIASOR_VER="0.3.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Pango Aliasor"
LABEL software.version="${PANGO_ALIASOR_VER}"
LABEL description="Links sublineages to parent pangolin lineages"
LABEL website="https://github.com/corneliusroemer/pango_aliasor"
LABEL license="https://github.com/corneliusroemer/pango_aliasor/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python-is-python3 \
    wget \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/corneliusroemer/pango_aliasor/archive/refs/tags/v${PANGO_ALIASOR_VER}.tar.gz && \
    pip install v${PANGO_ALIASOR_VER}.tar.gz && \
    rm v${PANGO_ALIASOR_VER}.tar.gz && \
    pip install --no-cache pandas && \
    mkdir /data

ENV PATH="$PATH" LC_ALL=C

COPY aliasor.py /usr/bin/.

WORKDIR /key

RUN wget -q https://raw.githubusercontent.com/cov-lineages/pango-designation/master/pango_designation/alias_key.json

WORKDIR /data

CMD [ "aliasor.py", "--help" ]

FROM staphb/pangolin:4.3.1-pdata-1.28 as pangolin

RUN apt-get update && apt-get install -y --no-install-recommends zstd

RUN wget -q https://github.com/corneliusroemer/pango-sequences/raw/main/data/pango-consensus-sequences_genome-nuc.fasta.zst && \
    zstd -d pango-consensus-sequences_genome-nuc.fasta.zst && \
    pangolin pango-consensus-sequences_genome-nuc.fasta

FROM app as test

WORKDIR /test

RUN aliasor.py --help

COPY --from=pangolin /data/lineage_report.csv .

RUN aliasor.py --input lineage_report.csv --output aliased_lineage_report_github.tsv && \
    aliasor.py --input lineage_report.csv --output aliased_lineage_report.tsv --alias-key /key/alias_key.json && \
    wc -l aliased_lineage_report_github.tsv aliased_lineage_report.tsv && \
    head aliased_lineage_report_github.tsv aliased_lineage_report.tsv


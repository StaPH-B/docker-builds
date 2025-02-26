FROM ubuntu:jammy as app

ARG DIAMOND_VER="2.1.9"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="DIAMOND"
LABEL software.version="${DIAMOND_VER}"
LABEL description="Accelerated BLAST compatible local sequence aligner."
LABEL website="https://github.com/bbuchfink/diamond"
LABEL license="https://github.com/bbuchfink/diamond/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ncbi-blast+ &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/bbuchfink/diamond/releases/download/v${DIAMOND_VER}/diamond-linux64.tar.gz &&\
    tar -C /usr/local/bin -xvf diamond-linux64.tar.gz && \
    rm diamond-linux64.tar.gz

ENV LC_ALL=C

CMD [ "diamond", "help" ]

WORKDIR /data

## Test ##
FROM app as test

RUN diamond test

RUN wget --no-check-certificate https://scop.berkeley.edu/downloads/scopeseq-2.07/astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa &&\
    diamond makedb --in astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa -d astral40 &&\
    diamond blastp -q astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa -d astral40 -o out.tsv --very-sensitive &&\
    head out.tsv

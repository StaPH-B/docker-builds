FROM ubuntu:noble AS app

ARG DIAMOND_VER="2.2.1"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="DIAMOND"
LABEL software.version="${DIAMOND_VER}"
LABEL description="Accelerated BLAST compatible local sequence aligner."
LABEL website="https://github.com/bbuchfink/diamond"
LABEL license="https://github.com/bbuchfink/diamond/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/bbuchfink/diamond/releases/download/v${DIAMOND_VER}/diamond-linux64.tar.gz &&\
    tar -C /usr/local/bin -xvf diamond-linux64.tar.gz && \
    rm diamond-linux64.tar.gz

ENV LC_ALL=C

CMD [ "diamond", "help" ]

WORKDIR /data

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN diamond test

# Currently running into an issue with this URL, where a bot catcher page (Anubis Web Firewall Utility) prevents access before redirecting to the file directory.
# Alternatives I've tried that have not succeeded:
#   wget https://scop.berkeley.edu/downloads/scopeseq-2.07/astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa
#   curl -L -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' 'https://scop.berkeley.edu/downloads/scopeseq-2.07/astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa' -o 'astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa'
RUN wget --quiet --no-check-certificate https://scop.berkeley.edu/downloads/scopeseq-2.07/astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa &&\
    cat astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa && \
    diamond makedb --in astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa -d astral40 &&\
    diamond blastp -q astral-scopedom-seqres-gd-sel-gs-bib-40-2.07.fa -d astral40 -o out.tsv --very-sensitive &&\
    head out.tsv

ARG BAKTA_VER="1.12.1"

FROM staphb/bakta:${BAKTA_VER} AS app

ARG BAKTA_VER


# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="staphb/bakta:${BAKTA_VER}"
LABEL dockerfile.version="1"
LABEL software="Bakta"
LABEL software.version="${BAKTA_VER}"
LABEL description="rapid & standardized annotation of bacterial genomes, MAGs & plasmids"
LABEL website="https://github.com/oschwengers/bakta"
LABEL license="https://github.com/oschwengers/bakta/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

ENV BAKTA_DB=/db/db-light

WORKDIR /db

RUN bakta_db download --type light 

CMD ["bakta", "--help"]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN bakta --help && \
    bakta_db --help && \
    bakta --version

RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/815/GCF_000195815.1_ASM19581v1/GCF_000195815.1_ASM19581v1_genomic.fna.gz && \
    gunzip GCF_000195815.1_ASM19581v1_genomic.fna.gz && \
    bakta GCF_000195815.1_ASM19581v1_genomic.fna && \
    head GCF_000195815.1_ASM19581v1_genomic.gbff

RUN micromamba list

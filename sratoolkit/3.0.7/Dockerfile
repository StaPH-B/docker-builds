FROM ubuntu:jammy as app

ARG SRATOOLKIT_VER="3.0.7"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SRA Toolkit"
LABEL software.version="${SRATOOLKIT_VER}"
LABEL description="Collection of tools and libraries for using data in the INSDC Sequence Read Archives"
LABEL website="https://github.com/ncbi/sra-tools"
LABEL license="https://github.com/ncbi/sra-tools/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/${SRATOOLKIT_VER}/sratoolkit.${SRATOOLKIT_VER}-ubuntu64.tar.gz &&\
    tar -xvf sratoolkit.${SRATOOLKIT_VER}-ubuntu64.tar.gz && rm sratoolkit.${SRATOOLKIT_VER}-ubuntu64.tar.gz

ENV PATH="$PATH:/sratoolkit.${SRATOOLKIT_VER}-ubuntu64/bin"\
    LC_ALL=C

CMD prefetch -h && fastq-dump -h && fasterq-dump -h

WORKDIR /data

## Test ##
FROM app as test

RUN prefetch -h && fastq-dump -h && fasterq-dump -h

RUN fastq-dump --stdout -X 2 SRR390728


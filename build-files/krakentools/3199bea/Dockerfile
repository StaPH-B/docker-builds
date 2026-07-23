FROM ubuntu:noble AS app

WORKDIR /

# using a git commit because the last release was over three years ago, despite recent(ish) activity in the repo's main branch
# this commit is from 2025-08-01: https://github.com/jenniferlu717/KrakenTools/commit/3199bea2b4768b2bb435f04483f5af3d8e51d4ae
ARG KRAKENTOOLS_VERSION="3199bea2b4768b2bb435f04483f5af3d8e51d4ae"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="KrakenTools"
LABEL software.version=${KRAKENTOOLS_VERSION}
LABEL description="KrakenTools is a set of tools for processing Kraken output"
LABEL website="https://github.com/jenniferlu717/KrakenTools"
LABEL documentation="https://github.com/jenniferlu717/KrakenTools"
LABEL license="https://github.com/jenniferlu717/KrakenTools/blob/master/LICENSE"
LABEL maintainer="Sage Wright"
LABEL maintainer.email="sagemwright@gmail.com"


# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    python3 \
    python3-pip \
    python-is-python3 \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --break-system-packages biopython==1.84 \
    pandas==2.2.3

RUN wget https://github.com/jenniferlu717/KrakenTools/archive/${KRAKENTOOLS_VERSION}.tar.gz && \
    tar -vxf ${KRAKENTOOLS_VERSION}.tar.gz && \
    rm -rf ${KRAKENTOOLS_VERSION}.tar.gz && \
    cd /KrakenTools-${KRAKENTOOLS_VERSION} && \
    chmod +x *

ENV PATH=/KrakenTools-${KRAKENTOOLS_VERSION}:${PATH}

WORKDIR /data

CMD ["extract_kraken_reads.py", "--help"]

FROM staphb/kraken2:2.17.1-viral-20251015 as test-data

WORKDIR /testdata

RUN wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_1.fastq.gz?raw=true -O SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_2.fastq.gz?raw=true -O SRR13957123_2.fastq.gz && \
    kraken2 --paired --classified-out cseqs#.fq --db /kraken2-db SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz --report kraken2_report.txt --output classifiedreads.txt

FROM app AS test

WORKDIR /test

RUN extract_kraken_reads.py --help

COPY --from=test-data /testdata/ .

RUN extract_kraken_reads.py \
    -k classifiedreads.txt \
    -r kraken2_report.txt \
    -s1 cseqs_1.fq \
    -s2 cseqs_2.fq \
    -t 2697049 \
    --fastq-output \
    -o extracted_1.fq \
    -o2 extracted_2.fq

RUN test -s extracted_1.fq
RUN grep -q "^@" extracted_1.fq

RUN kreport2krona.py -r kraken2_report.txt -o krona.txt
RUN test -s krona.txt

RUN kreport2mpa.py -r kraken2_report.txt -o mpa.txt
RUN test -s mpa.txt

RUN combine_kreports.py \
    -r kraken2_report.txt kraken2_report.txt \
    -o combined.txt
RUN test -s combined.txt

RUN ls /KrakenTools-*/*py
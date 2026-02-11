FROM ubuntu:jammy AS app

ARG MYLOASM_VER="0.4.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SoftwareName"
LABEL software.version="${MYLOASM_VER}"
LABEL description="Myloasm is a de novo metagenome assembler for long-read sequencing data"
LABEL website="https://github.com/bluenote-1577/myloasm"
LABEL license="https://github.com/bluenote-1577/myloasm/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate -O /usr/local/bin/myloasm https://github.com/bluenote-1577/myloasm/releases/download/v${MYLOASM_VER}/myloasm-${MYLOASM_VER}-x86_64-avx2 &&\
    chmod +x /usr/local/bin/myloasm

ENV LC_ALL=C

CMD [ "myloasm", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

RUN wget --no-check-certificate \
    https://github.com/epi2me-labs/wf-metagenomics/raw/master/test_data/case01/barcode01/reads.fastq.gz \
    https://github.com/epi2me-labs/wf-metagenomics/raw/master/test_data/case01/barcode01/reads2.fastq.gz \
    https://github.com/epi2me-labs/wf-metagenomics/raw/master/test_data/case01/barcode01/reads3.fastq.gz

RUN myloasm reads.fastq.gz reads2.fastq.gz reads3.fastq.gz -o test -t 50 &&\
    cat test/assembly_primary.fa

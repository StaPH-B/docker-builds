FROM nvidia/cuda:12.4.0-base-ubuntu22.04 AS app

ARG DORADO_VER="0.8.3"

LABEL base.image="nvidia/cuda:12.4.0-base-ubuntu20.04"
LABEL dockerfile.version="1"
LABEL software="Dorado"
LABEL software.version="${DORADO_VER}"
LABEL description="A tool for basecalling Fast5/Pod5 files from Oxford Nanopore sequencing"
LABEL website="https://github.com/nanoporetech/dorado"
LABEL license="https://github.com/nanoporetech/dorado/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y\
    wget \
    pigz \
    procps &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q --no-check-certificate https://cdn.oxfordnanoportal.com/software/analysis/dorado-${DORADO_VER}-linux-x64.tar.gz &&\
    tar --strip-components=1 -C /usr/local/ -xvf dorado-${DORADO_VER}-linux-x64.tar.gz &&\
    rm dorado-${DORADO_VER}-linux-x64.tar.gz

ENV LC_ALL=C 

CMD ["dorado", "-h"]

WORKDIR /data

## Test ##
FROM app AS test

ADD https://github.com/nanoporetech/dorado/raw/release-v0.8/tests/data/pod5/dna_r10.4.1_e8.2_260bps/dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5 dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5

RUN dorado download --model dna_r10.4.1_e8.2_260bps_sup@v3.5.2 &&\
    dorado basecaller dna_r10.4.1_e8.2_260bps_sup@v3.5.2 dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5 --emit-moves --max-reads 10 > calls.bam &&\
    dorado summary calls.bam


FROM nvidia/cuda:12.2.0-base-ubuntu22.04 AS app

ARG DORADO_VER="1.4.0"

LABEL base.image="nvidia/cuda:12.2.0-base-ubuntu22.04"
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
    ca-certificates \
    pigz \
    procps &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://cdn.oxfordnanoportal.com/software/analysis/dorado-${DORADO_VER}-linux-x64.tar.gz &&\
    tar --strip-components=1 -C /usr/local/ -xvf dorado-${DORADO_VER}-linux-x64.tar.gz &&\
    rm dorado-${DORADO_VER}-linux-x64.tar.gz

ENV LC_ALL=C 

CMD ["dorado", "-h"]

WORKDIR /data

## Test ##
FROM app AS test

RUN wget https://github.com/nanoporetech/dorado/raw/release-v1.1/tests/data/pod5/dna_r10.4.1_e8.2_400bps_5khz/dna_r10.4.1_e8.2_400bps_5khz-FLO_PRO114M-SQK_LSK114_XL-5000.pod5 &&\
    dorado basecaller fast dna_r10.4.1_e8.2_400bps_5khz-FLO_PRO114M-SQK_LSK114_XL-5000.pod5

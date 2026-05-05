ARG BAMTOOLS_VER="2.5.3"

## Builder ##
FROM ubuntu:noble AS builder

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    cmake \
    zlib1g-dev

ARG BAMTOOLS_VER

# bamtools
RUN wget -q https://github.com/pezmaster31/bamtools/archive/refs/tags/v${BAMTOOLS_VER}.tar.gz &&\
    tar -xzf v${BAMTOOLS_VER}.tar.gz &&\
    cd bamtools-${BAMTOOLS_VER} &&\
    mkdir build &&\
    cd build &&\
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local .. &&\
    make -j 4 &&\
    make install


## App ##
FROM ubuntu:noble AS app

ARG BAMTOOLS_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="HiFiAdapterFilt"
LABEL software.version="${BAMTOOLS_VER}"
LABEL description="A command-line toolkit for reading, writing, and manipulating BAM files"
LABEL website="https://github.com/pezmaster31/bamtools"
LABEL license="https://github.com/pezmaster31/bamtools/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/ /usr/local/

ENV LC_ALL=C

CMD ["bamtools", "--help"]

WORKDIR /data

## Test ##
FROM app AS test 

RUN bamtools --help

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.sorted.bam &&\
    bamtools stats -insert -in SRR13957123.sorted.bam



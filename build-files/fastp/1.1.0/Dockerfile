ARG FASTP_VER="1.1.0"
ARG ISAL_VER="2.31.1"

## Builder ##
FROM ubuntu:jammy AS builder

ARG FASTP_VER
ARG ISAL_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates \
    make \
    libdeflate-dev \
    autoconf \
    automake \
    libtool \
    nasm \
    yasm \
    help2man

# Note: libisal-dev package does not include libisal.a. So, Isa-l was compiled here.
RUN wget https://github.com/intel/isa-l/archive/refs/tags/v${ISAL_VER}.tar.gz &&\
    tar -xvf v${ISAL_VER}.tar.gz &&\
    cd isa-l-${ISAL_VER} &&\
    ./autogen.sh &&\
    ./configure --prefix=/usr --libdir=/usr/lib/x86_64-linux-gnu &&\
    make && make install

# Note: Use static to include isa-l & libdeflate
RUN wget https://github.com/OpenGene/fastp/archive/refs/tags/v${FASTP_VER}.tar.gz &&\
    tar -xvf v${FASTP_VER}.tar.gz &&\
    cd fastp-${FASTP_VER} &&\
    make static LIBRARY_DIRS=/usr/lib/x86_64-linux-gnu &&\
    make install

## App ##
FROM ubuntu:jammy AS app

ARG FASTP_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Fastp"
LABEL software.version=${FASTP_VER}
LABEL description="An ultra-fast all-in-one FASTQ preprocessor"
LABEL website="https://github.com/OpenGene/fastp"
LABEL license="https://github.com/OpenGene/fastp/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"


RUN apt-get update && apt-get install -y --no-install-recommends \
    jq &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/fastp /usr/local/bin/fastp

ENV LC_ALL=C

WORKDIR /data

CMD [ "fastp", "--help" ]

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y wget

# downloading sars-cov-2 fastq test files
RUN wget -q \
    https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz \
    https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz

# running fastp on the files
RUN fastp \
    -i SRR13957123_1.fastq.gz \
    -I SRR13957123_2.fastq.gz \
    -o SRR13957123_PE1.fastq.gz \
    -O SRR13957123_PE2.fastq.gz \
    -h SRR13957123_fastp.html \
    -j SRR13957123_fastp.json
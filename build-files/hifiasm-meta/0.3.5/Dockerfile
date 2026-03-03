ARG HIFIASM_META_VER="0.3.5"

## Builder ##
FROM ubuntu:noble AS builder

ARG HIFIASM_META_VER

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    zlib1g-dev &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# hifiasm-meta
RUN wget https://github.com/xfengnefx/hifiasm-meta/archive/refs/tags/hamtv${HIFIASM_META_VER}.tar.gz &&\
    tar -xvf hamtv${HIFIASM_META_VER}.tar.gz && rm hamtv${HIFIASM_META_VER}.tar.gz &&\
    cd hifiasm-meta-hamtv${HIFIASM_META_VER} && make &&\
    mv hifiasm_meta /usr/local/bin/

## App ##
FROM ubuntu:noble AS app

ARG HIFIASM_META_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="hifiasm-meta"
LABEL software.version="${HIFIASM_META_VER}"
LABEL description="A hifiasm fork for metagenome assembly using Hifi reads"
LABEL website="https://github.com/xfengnefx/hifiasm-meta"
LABEL license="https://github.com/xfengnefx/hifiasm-meta/blob/meta/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/hifiasm_meta /usr/local/bin/

ENV LC_ALL=C

CMD ["hifiasm_meta"]

WORKDIR /data

## Test ##
FROM app AS test

RUN hifiasm_meta -h

# test hifiasm-meta (requires ~18GB of RAM.)
# RUN apt-get update && apt-get install -y wget
# RUN wget -q https://zenodo.org/records/5908204/files/zymoD6331std-ecoli-ten-percent.fq.gz?download=1 -O test.fq.gz &&\
#     hifiasm_meta -t4 --force-rs -o asm test.fq.gz 2>asm.log


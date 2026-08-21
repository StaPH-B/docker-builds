ARG WTDBG2_VER="2.5"

## Builder ##
FROM ubuntu:noble AS builder

RUN apt-get update && apt-get install -y \
    build-essential\
    zlib1g-dev \
    wget \
    perl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/ruanjue/wtdbg2/archive/refs/tags/v2.5.tar.gz &&\
    tar -xvf v2.5.tar.gz && rm v2.5.tar.gz &&\
    cd wtdbg2-2.5 &&\
    make && make install &&\
    cp wtdbg2.pl /usr/local/bin/ &&\
    cp scripts/* /usr/local/bin/

## App ##
FROM ubuntu:noble AS app

ARG WTDBG2_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Wtdbg2"
LABEL software.version="${WTDBG2_VER}"
LABEL description="Wtdbg2 is a de novo sequence assembler for long noisy reads produced by PacBio or Oxford Nanopore Technologies"
LABEL website="https://github.com/ruanjue/wtdbg2"
LABEL license="https://github.com/ruanjue/wtdbg2/blob/master/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# dependencies for scripts & polishing
RUN apt-get update && apt-get install -y --no-install-recommends \
    perl \
    minimap2 \
    samtools \
    bwa &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/ /usr/local/bin/

ENV LC_ALL=C

CMD [ "wtdbg2", "--help" ]

WORKDIR /data

## prep test data ##
FROM staphb/rasusa:4.1.0 AS testdata

RUN wget https://downloads.pacbcloud.com/public/dataset/2021-11-Microbial-96plex/demultiplexed-reads/m64004_210929_143746.bc2033.bam &&\
    rasusa reads --coverage 25 --genome-size 1.6m --output test.fastq.gz --output-format fastq m64004_210929_143746.bc2033.bam 

## Test ##
FROM app AS test 

COPY --from=testdata /data/test.fastq.gz /data/test.fastq.gz

# wtdbg2.pl assembles reads with wtdbg2, create concensus wtpoa-cns and polish consensus using minimap and samtools
RUN wtdbg2.pl -t 4 -x ccs -g 1.6m -o dbg test.fastq.gz &&\
    head dbg.cns.fa



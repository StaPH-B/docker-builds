ARG TGSFILTER_VER=1.11

## Builder ##
FROM ubuntu:noble AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Note: 1.11 was not released. The latest commit hash is a47b30e
RUN git clone https://github.com/HuiyangYu/TGSFilter.git &&\
    cd TGSFilter &&\
    sed -i 's/-fPIE/-no-pie/' Makefile &&\
    make &&\
    mv ./bin/tgsfilter /usr/local/bin/

## App ##
FROM ubuntu:noble AS app

ARG TGSFILTER_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="TGSFilter"
LABEL software.version="${TGSFILTER_VER}"
LABEL description="An ultra-fast and efficient tool for long reads filtering and trimming"
LABEL website="https://github.com/HuiyangYu/TGSFilter"
LABEL license="https://github.com/HuiyangYu/TGSFilter/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/tgsfilter /usr/local/bin/tgsfilter

ENV LC_ALL=C

CMD [ "tgsfilter", "-h" ]

WORKDIR /data

## Test data ##
FROM staphb/sratoolkit AS data

RUN fasterq-dump SRR31499991 &&\
    gzip SRR31499991_1.fastq

## Test ##
FROM app AS test 

COPY --from=data /data/SRR31499991.fastq.gz /data/SRR31499991.fastq.gz

RUN tgsfilter -i SRR31499991.fastq.gz -x hifi -g 1.8m -d 60 -o test.clean.fq.gz





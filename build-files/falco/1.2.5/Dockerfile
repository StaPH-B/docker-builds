ARG FALCO_VER="1.2.5"

## Builder ##
FROM ubuntu:jammy AS builder

ARG FALCO_VER

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    zlib1g-dev \
    libhts-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/smithlabcode/falco/releases/download/v${FALCO_VER}/falco-${FALCO_VER}.tar.gz &&\
    mkdir /opt/falco &&\
    tar --strip-components=1 -C /opt/falco -xvf falco-${FALCO_VER}.tar.gz &&\
    cd /opt/falco &&\
    ./configure CXXFLAGS="-O3 -Wall" --enable-hts &&\
    make HAVE_HTSLIB=1 all &&\
    make HAVE_HTSLIB=1 install

## App ##
FROM ubuntu:jammy AS app

ARG FALCO_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="falco"
LABEL software.version="${FALCO_VER}"
LABEL description="A C++ drop-in replacement of FastQC to assess the quality of sequence read data"
LABEL website="https://github.com/smithlabcode/falco"
LABEL license="https://github.com/smithlabcode/falco/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    libhts-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /opt/falco/Configuration/ /opt/falco/Configuration/

ENV LC_ALL=C

CMD [ "falco", "-help" ]

WORKDIR /data

## Test ##
FROM app AS test

ADD https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123.sorted.bam /data/
ADD https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz /data/

RUN falco -o bamtest SRR13957123.sorted.bam &&\
    falco -o fqtest SRR13957123_1.fastq.gz

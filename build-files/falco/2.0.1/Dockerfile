FROM ubuntu:noble AS app

ARG FALCO_VER="2.0.1"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="falco"
LABEL software.version="${FALCO_VER}"
LABEL description="A C++ drop-in replacement of FastQC to assess the quality of sequence read data"
LABEL website="https://github.com/smithlabcode/falco"
LABEL license="https://github.com/smithlabcode/falco/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install --no-install-recommends -y \
    libhts3 \
    libdeflate0 \
    libhtscodecs2 \
    liblzma5 \
    libbz2-1.0 \
    libstdc++6 \
    libgcc-s1 \
    zlib1g \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/smithlabcode/falco/releases/download/v${FALCO_VER}/falco-${FALCO_VER}-Linux.tar.gz && \
    tar -xvf falco-${FALCO_VER}-Linux.tar.gz && \
    mkdir -p /usr/local/bin /opt/falco && \
    cp /falco-${FALCO_VER}-Linux/bin/falco /usr/local/bin/ && \
    cp -r /falco-${FALCO_VER}-Linux/share/falco/* /opt/falco/&& \
    rm -rf falco-${FALCO_VER}-Linux.tar.gz /falco-${FALCO_VER}-Linux

ENV LC_ALL=C

CMD [ "falco", "-help" ]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN falco --version && \
    falco --help

RUN wget https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123.sorted.bam && \
    wget https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz

RUN falco -o bamtest SRR13957123.sorted.bam && \
    head bamtest/SRR13957123.sorted/fastqc_data.txt && \
    falco -o fqtest SRR13957123_1.fastq.gz && \
    head fqtest/SRR13957123_1/fastqc_data.txt

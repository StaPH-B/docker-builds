ARG BEDDER_RS_VER="0.1.14"

FROM python:3.13-slim AS app
ARG BEDDER_RS_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="bedder-rs"
LABEL software.version="${BEDDER_RS_VER}"
LABEL description="A rust-based command-line tool for genomic analysis serving as a successor to bedtools."
LABEL website="https://github.com/quinlan-lab/bedder-rs"
LABEL license="https://github.com/quinlan-lab/bedder-rs/blob/main/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/quinlan-lab/bedder-rs/releases/download/v${BEDDER_RS_VER}/bedder-static-linux-x86_64 && \
    ls -lah && \
    mv bedder-static-linux-x86_64 /usr/local/bin/bedder && \
    chmod +x /usr/local/bin/bedder

ENV PYTHONHOME=/usr/local \
    PYTHONPATH=/usr/local/lib/python3.13 \
    LC_ALL=C

CMD [ "bedder", "--help" ]

WORKDIR /data


FROM app AS test
ARG BEDDER_RS_VER

WORKDIR /test

RUN bedder --help && \
    bedder --version

RUN wget -q https://github.com/quinlan-lab/bedder-rs/archive/refs/tags/v${BEDDER_RS_VER}.tar.gz && \
    tar -xzf v${BEDDER_RS_VER}.tar.gz && \
    rm v${BEDDER_RS_VER}.tar.gz
    

RUN cd bedder-rs-${BEDDER_RS_VER} && \
    echo "intersect test" && \
    bedder intersect -a tests/examples/aa.bed -b tests/examples/bb.bed -g tests/examples/fake.fai --a-piece whole-wide --b-piece none && \
    echo "map test" && \
    bedder map -a tests/map_a.bed -b tests/map_b.bed -g tests/examples/fake.fai
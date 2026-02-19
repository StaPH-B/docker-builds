ARG AUTOCYCLER_VER="0.5.2"

FROM ubuntu:noble AS app

ARG AUTOCYCLER_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Autocycler"
LABEL software.version="${AUTOCYCLER_VER}"
LABEL description="generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Autocycler"
LABEL license="https://github.com/rrwick/Autocycler/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

# install autocycler and helper scripts
RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    tar -vxf autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    rm autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    wget -q https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz && \
    tar -vxf autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz && \
    rm autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz

ENV PATH=$PATH LC_ALL=C

CMD [ "autocycler", "--help" ]

WORKDIR /data

FROM app AS test

ARG AUTOCYCLER_VER

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

# demo dataset does not change with version
RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -vxf autocycler-demo-dataset.tar && \
    autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --genome_size "242000"

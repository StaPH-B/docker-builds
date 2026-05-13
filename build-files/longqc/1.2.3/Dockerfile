ARG LONGQC_VER="1.2.3"

FROM python:3.9.17-slim AS builder
ARG LONGQC_VER

WORKDIR /opt

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    libhts-dev \
    build-essential && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir \
    numpy \
    scipy \
    "matplotlib>=2.1.2" \
    scikit-learn \
    "pandas>=0.24.0" \
    jinja2 \
    h5py \
    pysam \
    edlib

RUN wget https://github.com/yfukasawa/LongQC/archive/refs/tags/v${LONGQC_VER}.tar.gz && \
    tar -xzf v${LONGQC_VER}.tar.gz && \
    rm v${LONGQC_VER}.tar.gz && \
    mv LongQC-${LONGQC_VER} /opt/LongQC

RUN cd /opt/LongQC/minimap2-coverage && \
    make && \
    sed -i '1s;^;#!/usr/bin/env python\n;' /opt/LongQC/longQC.py && \
    chmod +x /opt/LongQC/longQC.py


FROM python:3.9.17-slim AS app
ARG LONGQC_VER

LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="LongQC"
LABEL software.version="${LONGQC_VER}"
LABEL description="A tool for the data quality control of the PacBio and ONT long reads, and it has two functionalities: sample QC and platform QC."
LABEL website="https://github.com/yfukasawa/LongQC"
LABEL license="https://github.com/yfukasawa/LongQC/blob/master/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    libhts3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /opt/LongQC /opt/LongQC

RUN ln -s /opt/LongQC/longQC.py /usr/local/bin/longqc && \
    ln -s /opt/LongQC/longQC.py /usr/local/bin/LongQC

ENV PATH="/opt/LongQC:/opt/LongQC/minimap2-coverage:/opt/venv/bin:${PATH}" LC_ALL=C

WORKDIR /data

CMD ["longQC.py", "--help"]


FROM app AS test

WORKDIR /test

RUN echo -e "\n\nMain help message: " && longQC.py --help && \
    echo -e "\n\nrunqc help message: " && longqc runqc -h && \
    echo -e "\n\nsampleqc help message: " && LongQC sampleqc -h && \
    longQC.py --version

# ONT test dataset download
RUN wget -q https://github.com/bactopia/bactopia-tests/raw/646919e3f8174f6cc1a462a78109ba8fdbcd92d3/species/portiera/reads/nanopore/ERR3772599.fastq.gz && \
    longQC.py sampleqc -x ont-ligation -o longqc_ONT_out ERR3772599.fastq.gz && \
    ls longqc_ONT_out/

RUN wget -q https://downloads.pacbcloud.com/public/dataset/2021-11-Microbial-96plex/demultiplexed-reads/m64004_210929_143746.bc2002.bam && \
    longQC.py sampleqc -x pb-sequel -o longqc_PB_out m64004_210929_143746.bc2002.bam && \
    ls longqc_PB_out
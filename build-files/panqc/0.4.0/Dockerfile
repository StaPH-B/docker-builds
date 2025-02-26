FROM ubuntu:jammy as app

ARG PANQC_VER="0.4.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="panqc"
LABEL software.version="${PANQC_VER}"
LABEL description="A pan-genome quality control toolkit for evaluating nucleotide redundancy in pan-genome analyses."
LABEL website="https://github.com/maxgmarin/panqc"
LABEL license="https://github.com/maxgmarin/panqc/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    python3 \
    python3-pip \
    python3-dev \
    gcc && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install cython

RUN wget -q https://github.com/maxgmarin/panqc/archive/refs/tags/${PANQC_VER}.tar.gz && \
    pip install --no-cache-dir ${PANQC_VER}.tar.gz && \
    rm ${PANQC_VER}.tar.gz && \
    mkdir /data

ENV LC_ALL=C

CMD panqc nrc --help && panqc utils --help

WORKDIR /data

FROM app as test

WORKDIR /test

RUN panqc nrc --help && \
    panqc utils --help

RUN wget -q https://github.com/maxgmarin/panqc/archive/refs/tags/${PANQC_VER}.tar.gz && \
    tar -xvf ${PANQC_VER}.tar.gz && \
    cd panqc-${PANQC_VER}/tests/data && \
    panqc nrc -a TestSet1.InputAsmPaths.tsv -r TestSet1.pan_genome_reference.fa.gz -m TestSet1.gene_presence_absence.csv -o test_results/

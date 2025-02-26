FROM ubuntu:jammy AS app

ARG ENA_VER="1.7.1"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="enaBrowserTools"
LABEL software.version="${ENA_VER}"
LABEL description="A set of scripts that interface with the ENA web services to download data from ENA."
LABEL website="https://github.com/enasequence/enaBrowserTools"
LABEL license="https://github.com/enasequence/enaBrowserTools/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    ca-certificates \
    wget \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install requests

# ENA tools
RUN wget -q https://github.com/enasequence/enaBrowserTools/archive/refs/tags/v${ENA_VER}.tar.gz && \
    tar -xvf v${ENA_VER}.tar.gz && \
    rm v${ENA_VER}.tar.gz


ENV PATH="/enaBrowserTools-${ENA_VER}/python3:$PATH" LC_ALL=C

CMD [ "enaDataGet", "--help" ]

WORKDIR /data

# A second FROM insruction creates a new stage
FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN enaDataGet -h && enaGroupGet -h

RUN enaDataGet -f fastq SRR29437696 && ls */*fastq.gz

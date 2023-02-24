FROM ubuntu:jammy as app

ARG PORECHOP_VER=0.2.4

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="porechop"
LABEL software.version=${PORECHOP_VER}
LABEL description="The swiss army knife for genome assembly."
LABEL website="https://github.com/rrwick/Porechop"
LABEL license="https://github.com/rrwick/Porechop/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  procps \
  wget \
  python3-pip \
  python3-distutils \
  python3 \
  make \
  g++ && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools

RUN wget -q https://github.com/rrwick/Porechop/archive/refs/tags/v${PORECHOP_VER}.tar.gz && \
  tar -xf v${PORECHOP_VER}.tar.gz && ls  && \
  rm v${PORECHOP_VER}.tar.gz && \
  cd /Porechop-${PORECHOP_VER} && \
  python3 setup.py install

ENV LC_ALL=C

WORKDIR /data

FROM app as test

WORKDIR /test

RUN porechop --help && porechop --version

RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR225/094/SRR22580994/SRR22580994_1.fastq.gz && \
    porechop -i SRR22580994_1.fastq.gz -o SRR22580994_chopped.fastq.gz && wc -l *fastq.gz
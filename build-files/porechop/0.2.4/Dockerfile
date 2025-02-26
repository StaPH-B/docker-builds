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

# DL small ONT FASTQ files, run through porechop as a test, print number of lines in each (expect less lines in the .chopped.fastq.gz file)
RUN echo "downloading ONT test data from bactopia/bactopia-tests on GitHub and running porechop on them..." && \
    wget -q https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz && \
    porechop -i ERR3772599.fastq.gz -o ERR3772599.chopped.fastq.gz && \
    wc -l *fastq.gz

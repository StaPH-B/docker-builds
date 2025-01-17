FROM ubuntu:jammy as app

ARG GFASTATS_VER=1.3.6

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="gfastats"
LABEL software.version=${GFASTATS_VER}
LABEL description="The swiss army knife for genome assembly."
LABEL website="https://github.com/vgl-hub/gfastats"
LABEL license="https://github.com/vgl-hub/gfastats/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  procps \
  wget \
  make \
  g++ \
  zlib1g-dev && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/vgl-hub/gfastats/releases/download/v${GFASTATS_VER}/gfastats.v${GFASTATS_VER}.tar.gz && \
  tar -xf gfastats.v${GFASTATS_VER}.tar.gz && \
  rm gfastats.v${GFASTATS_VER}.tar.gz && \
  cd /gfastats && \
  make -j

ENV PATH="/gfastats/build/bin:${PATH}" \
  LC_ALL=C

WORKDIR /data

FROM app as test

WORKDIR /test

RUN gfastats --help && gfastats --version

RUN gfastats /gfastats/testFiles/random1.fasta -o gfa && \
  gfastats /gfastats/testFiles/random2.gfa2 && \
  gfastats /gfastats/testFiles/random1.fasta -k /gfastats/testFiles/random1.instructions.sak -o gfa && \
  gfastats --tabular --seq-report /gfastats/testFiles/random6.circular.gfa
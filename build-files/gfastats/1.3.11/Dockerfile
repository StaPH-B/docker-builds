ARG GFASTATS_VER=1.3.11

FROM ubuntu:noble AS app

ARG GFASTATS_VER

LABEL base.image="ubuntu:noble"
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
  wget && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

RUN wget -q https://github.com/vgl-hub/gfastats/releases/download/v${GFASTATS_VER}/gfastats.v${GFASTATS_VER}-linux.tar.gz && \
  tar -vxf gfastats.v${GFASTATS_VER}-linux.tar.gz && \
  rm gfastats.v${GFASTATS_VER}-linux.tar.gz && \
  chmod +x gfastats

ENV PATH="$PATH" \
  LC_ALL=C

CMD ["gfastats", "--help"]

WORKDIR /data

FROM app AS test

ARG GFASTATS_VER

WORKDIR /test

RUN gfastats --help && gfastats --version

RUN wget -q https://github.com/vgl-hub/gfastats/archive/refs/tags/v${GFASTATS_VER}.tar.gz && \
  tar -xvf v${GFASTATS_VER}.tar.gz

RUN gfastats gfastats-${GFASTATS_VER}/testFiles/random1.fasta -o gfa && \
  gfastats gfastats-${GFASTATS_VER}/testFiles/random2.gfa2 && \
  gfastats gfastats-${GFASTATS_VER}/testFiles/random1.fasta -k gfastats-${GFASTATS_VER}/testFiles/random1.instructions.sak -o gfa && \
  gfastats --tabular --segment-report gfastats-${GFASTATS_VER}/testFiles/random6.circular.gfa > results.txt && \
  head results.txt
  

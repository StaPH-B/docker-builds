FROM ubuntu:jammy as app

ARG SAMTOOLSVER="1.18"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Samtools"
LABEL software.version="${SAMTOOLSVER}"
LABEL description="Tools (written in C using htslib) for manipulating next-generation sequencing data"
LABEL website="https://github.com/samtools/samtools"
LABEL license="https://github.com/samtools/samtools/blob/develop/LICENSE"
LABEL maintainer="Shelby Bennett"
LABEL maintainer.email="shelby.bennett@dgs.virginia.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
  libncurses5-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  zlib1g-dev \
  libssl-dev \
  gcc \
  wget \
  make \
  perl \
  bzip2 \
  gnuplot \
  ca-certificates \
  gawk \
  python3 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
  rm samtools-${SAMTOOLSVER}.tar.bz2 && \
  cd samtools-${SAMTOOLSVER} && \
  ./configure && \
  make && \
  make install && \
  mkdir /data

ENV LC_ALL=C

WORKDIR /data

CMD samtools --help

FROM app as test

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
  wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
  wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.primer.bed && \
  samtools stats SRR13957123.primertrim.sorted.bam && \
  samtools faidx SRR13957123.consensus.fa && \
  samtools ampliconstats nCoV-2019.primer.bed SRR13957123.primertrim.sorted.bam > SRR13957123_ampliconstats.txt && \
  plot-ampliconstats plot SRR13957123_ampliconstats.txt && \
  ls
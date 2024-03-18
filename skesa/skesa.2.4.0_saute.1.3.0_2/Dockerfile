ARG SKESA_VER="skesa.2.4.0_saute.1.3.0_2"

FROM ubuntu:jammy as builder

ARG SKESA_VER

RUN apt-get update && apt-get install -y \
  ca-certificates \
  procps \
  wget \
  make \
  git \
  g++ \
  cmake \
  libboost-filesystem-dev \
  libboost-all-dev \
  libmysqlclient-dev \
  flex \
  bison \
  doxygen \
  libxml2 \
  default-jdk

# get skesa, gfa_connector, and kmercounter binaries, rename them
RUN wget -q https://github.com/ncbi/SKESA/archive/refs/tags/${SKESA_VER}.tar.gz && \
  tar -xzvf ${SKESA_VER}.tar.gz && \
  rm ${SKESA_VER}.tar.gz && \
  cd SKESA-${SKESA_VER} && \
  make

# copying executables to easy-to-copy-later place
RUN cp /SKESA-${SKESA_VER}/skesa         /usr/local/bin/ && \
  cp /SKESA-${SKESA_VER}/saute         /usr/local/bin/ && \
  cp /SKESA-${SKESA_VER}/saute_prot    /usr/local/bin/ && \
  cp /SKESA-${SKESA_VER}/gfa_connector /usr/local/bin/ && \
  cp /SKESA-${SKESA_VER}/kmercounter   /usr/local/bin/ && skesa -h

FROM ubuntu:jammy as app

ARG SKESA_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SKESA"
LABEL software.version="${SKESA_VER}"
LABEL description="Strategic Kmer Extension for Scrupulous Assemblies"
LABEL website="https://github.com/ncbi/SKESA"
LABEL lisence="https://github.com/ncbi/SKESA/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  procps \
  wget && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/* /usr/local/bin/

# set PATH, set perl locale settings for singularity compatibility
ENV PATH=${PATH} \
  LC_ALL=C

CMD skesa -h

WORKDIR /data

FROM app as test

RUN skesa -h && \
  skesa -v && \
  saute -h && \
  saute -v && \
  saute_prot -h && \
  saute_prot -v && \
  gfa_connector -h && \
  gfa_connector -v && \
  kmercounter -h && \
  kmercounter -v

WORKDIR /test

RUN skesa --sra_run SRR1510963 --hash_count --contigs_out /test/SRR1510963_skesa.fasta && \
  head /test/SRR1510963_skesa.fasta

RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
  wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
  skesa --reads SRR13957123_1.fastq.gz,SRR13957123_2.fastq.gz --cores 4 --memory 48 > SRR13957123_skesa.fa && \
  head SRR13957123_skesa.fa

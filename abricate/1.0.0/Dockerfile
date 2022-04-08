ARG ABRICATE_VER="1.0.0"

FROM ubuntu:focal as app

ARG ABRICATE_VER
ARG ANY2FASTA_VERSION=0.4.2

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="3"
LABEL software="Abricate"
LABEL software.version="${ABRICATE_VER}"
LABEL description="Mass screening of contigs for AMR or virulence genes"
LABEL website="https://github.com/tseemann/abricate"
LABEL license="https://github.com/tseemann/abricate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
# removed: emboss
# ncbi-blast+ version in apt for ubuntu:focal = v2.9.0
RUN apt-get update && apt-get install -y --no-install-recommends \
  bioperl \
  gzip \
  unzip \
  liblist-moreutils-perl \
  libjson-perl \
  libtext-csv-perl \
  libfile-slurp-perl \
  liblwp-protocol-https-perl \
  libwww-perl \
  libpath-tiny-perl \
  git \
  ncbi-blast+ \
  wget && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install any2fasta
RUN wget https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VERSION}.tar.gz && \
    tar -xvf v${ANY2FASTA_VERSION}.tar.gz && \
    rm v${ANY2FASTA_VERSION}.tar.gz && \
    cd any2fasta-${ANY2FASTA_VERSION} && \
    chmod +x any2fasta

# install abricate
RUN wget https://github.com/tseemann/abricate/archive/v${ABRICATE_VER}.tar.gz && \
    tar -zxvf v${ABRICATE_VER}.tar.gz && \
    rm -rf v${ABRICATE_VER}.tar.gz

# set $PATH
# set perl locale settings for singularity compatibility
ENV PATH="/abricate-${ABRICATE_VER}/bin:\
/any2fasta-${ANY2FASTA_VERSION}:\
$PATH"\
    LC_ALL=C

# check dependencies, setup db's, make working directory /data
# tests now run as part of travis, instead of in dockerfile
RUN abricate --check && \
    abricate --setupdb && \
    mkdir /data

WORKDIR /data

# testing
FROM app as test

ARG ABRICATE_VER

COPY tests.sh .

RUN bash tests.sh ${ABRICATE_VER}

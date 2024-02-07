FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during build time
ARG ARIBA_VER="2.14.7"

# versions from https://github.com/sanger-pathogens/ariba/blob/71909ed5b068723119e941045d25ed60328e70e7/install_dependencies.sh
ARG SPADES_VER="3.13.1"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="ARIBA"
LABEL software.version="${ARIBA_VER}"
LABEL description="ARIBA: Antimicrobial Resistance Identification By Assembly"
LABEL website="https://github.com/sanger-pathogens/ariba"
LABEL license="https://github.com/sanger-pathogens/ariba/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Harry Hung"
LABEL maintainer2.email="ch31@sanger.ac.uk"

# prevents having to enter commands during apt-get install
ARG DEBIAN_FRONTEND=noninteractive

# dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  python3-dev \
  python3-pip \
  python3-tk \
  python3-setuptools \
  python3-wheel \
  cython3 \
  zlib1g-dev \
  bowtie2 \
  mummer \
  cd-hit \
  wget \
  curl \
  gawk \
  locales-all \
  build-essential \
  libbz2-dev \
  libjpeg-dev  \
  liblzma-dev  \
  autoconf \
  automake \
  perl \
  libcurl4-gnutls-dev \
  libssl-dev \
  libncurses5 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/* 

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en 

# optional installation to enable the usage of SPAdes assembler
RUN wget -q https://github.com/ablab/spades/releases/download/v${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm SPAdes-${SPADES_VER}-Linux.tar.gz

# needed to avoid a matplotlib error
# https://github.com/sanger-pathogens/ariba/blob/b1b524c9d9588cba9d998c9121bd74c63856526/Dockerfile#L49
ENV MPLBACKEND="agg"

# install ariba with pip3
RUN wget -q https://github.com/sanger-pathogens/ariba/archive/refs/tags/v${ARIBA_VER}.tar.gz && \
  pip3 install v${ARIBA_VER}.tar.gz && \
  rm -rf v${ARIBA_VER}.tar.gz && \
  mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="/SPAdes-${SPADES_VER}-Linux/bin:$PATH" \
  LC_ALL=C

WORKDIR /data

# default command is to pull up help options
CMD ["ariba", "--help"]

# new base for testing
FROM app as test

# print out ARIBA version and 
RUN ariba version

# run built-in test and confirm files are successfully created
RUN ariba test out && \
  ls out/OUT/assemblies.fa.gz && \
  ls out/OUT/assembled_genes.fa.gz && \
  ls out/OUT/assembled_seqs.fa.gz && \
  ls out/OUT/log.clusters.gz && \
  ls out/OUT/report.tsv && \
  ls out/OUT/version_info.txt

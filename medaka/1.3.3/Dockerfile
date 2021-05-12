FROM ubuntu:bionic

ARG medakaVer="1.3.3"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Medaka"
LABEL software.version="1.2.0"
LABEL description="Consensus sequence correction provided by ONT Research"
LABEL website="https://github.com/nanoporetech/medaka"
LABEL license="https://github.com/nanoporetech/medaka/blob/master/LICENSE.md"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

RUN apt-get update && apt-get install --no-install-recommends -y make \
 cmake \
 file \
 bzip2 \
 gcc \
 g++ \
 python \
 zlib1g-dev \
 wget \
 curl \
 libffi-dev \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 libssl-dev \
 python3-all-dev \
 python3-venv \
 python-virtualenv \
 virtualenv \
 git-lfs && \
 apt-get clean && apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# initialize git lfs, prior to cloning repo
RUN git lfs install

# install medaka
RUN git clone https://github.com/nanoporetech/medaka.git --single-branch --depth 1 --branch v${medakaVer} && \
 cd medaka && \
 make install && \
 mkdir /data

WORKDIR /data

# acts similar to activating python venv before running
# LC_ALL=C for singularity compatibility
ENV PATH="/medaka/venv/bin:$PATH"\
 LC_ALL=C

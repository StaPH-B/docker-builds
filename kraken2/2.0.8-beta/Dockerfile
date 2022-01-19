# base image
FROM ubuntu:xenial as app

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Kraken2"
LABEL software.version="2.0.8-beta"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
  wget \
  zlib1g-dev \
  make \
  g++

# DL Kraken2, unpack, and install
RUN wget https://github.com/DerrickWood/kraken2/archive/v2.0.8-beta.tar.gz && \
  tar -xzf v2.0.8-beta.tar.gz && \
  rm -rf v2.0.8-beta.tar.gz && \
  cd kraken2-2.0.8-beta && \
  ./install_kraken2.sh . && \
  mkdir /data

ENV PATH="$PATH:/kraken2-2.0.8-beta" \
    LC_ALL=C

WORKDIR /data

# DL MiniKraken2_v1_8GB database. Built from RefSeq bacteria, archaea, and viral libraries. No human.
RUN mkdir /kraken2-db && \
  cd /kraken2-db && \
  wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_8gb_20210517.tar.gz && \
  tar -zxf k2_standard_8gb_20210517.tar.gz && \
  rm -rf k2_standard_8gb_20210517.tar.gz

FROM app as test

# Get test dependencies
RUN apt-get update && apt-get install -y python3
COPY kraken2/2.0.8-beta/tests /tests
COPY test_data/trim_reads/SRR5481494_sub.extendedFrags.fastq.gz /test_data/trim_reads/
COPY test_data/trim_reads/SRR5481494_sub.notCombined_*.fastq.gz /test_data/trim_reads/

# Run positive control
RUN bash /tests/scripts/run_positive_control.sh

# Check output
RUN python3 -m unittest discover -s /tests

# Test with: docker build --progress=plain --target=test -t kraken2-test-image -f kraken2/2.0.8-beta/Dockerfile .

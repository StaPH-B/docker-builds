# base image
FROM ubuntu:xenial as app

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1.1"
LABEL software="Kraken"
LABEL software.version="1.0"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken"
LABEL license="https://github.com/DerrickWood/kraken/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
  wget \
  zlib1g-dev \
  make \
  g++ \
  cpanminus \
  rsync

# DL Jellyfish, unpack, and install
RUN wget https://github.com/gmarcais/Jellyfish/releases/download/v1.1.12/jellyfish-1.1.12.tar.gz && \
  tar -zxf jellyfish-1.1.12.tar.gz && rm -rf jellyfish-1.1.12.tar.gz
RUN cd jellyfish-1.1.12 && ./configure --prefix=/opt/ && make -j 4 && make install

# DL Kraken v1.0, unpack, and install
RUN wget https://github.com/DerrickWood/kraken/archive/v1.0.tar.gz && \
  tar -xzf v1.0.tar.gz && \ 
  rm -rf v1.0.tar.gz && \
  cd kraken-1.0 && \
  mkdir /opt/kraken && \
  ./install_kraken.sh /opt/kraken/ && \
  mkdir /data

ENV PATH="$PATH:/opt/kraken:/opt/bin" \
    LC_ALL=C
WORKDIR /data

# this perl module and rsync required for kraken-build
RUN cpanm Getopt::Std

# DL MiniKraken database
RUN mkdir /kraken-database && \
  cd /kraken-database && \
  wget https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz && \
  tar -zxf minikraken_20171019_4GB.tgz && \
  rm -rf minikraken_20171019_4GB.tgz

FROM app as test

# Get test dependencies
RUN apt-get update && apt-get install -y python3
COPY kraken/1.0/tests /tests
COPY test_data/trim_reads/SRR5481494_sub.extendedFrags.fastq.gz /test_data/trim_reads/
COPY test_data/trim_reads/SRR5481494_sub.notCombined_*.fastq.gz /test_data/trim_reads/

# Run positive control
RUN bash /tests/scripts/run_positive_control.sh

# Check output
RUN python3 -m unittest discover -s /tests

# Test with: docker build --progress=plain --target=test -t kraken-test-image -f kraken/1.0/Dockerfile .

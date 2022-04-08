FROM ubuntu:xenial as app

ARG SEQYCLEANVER=1.10.09

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="2"
LABEL software="seqyclean"
LABEL software.version="${SEQYCLEANVER}"
LABEL description="Trims and cleans fastq files"
LABEL website="https://github.com/ibest/seqyclean"
LABEL license="https://github.com/ibest/seqyclean/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# getting dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  zlib1g-dev \
  ca-certificates \
  wget \
  make \
  gcc \
  g++ && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/ibest/seqyclean/archive/refs/tags/${SEQYCLEANVER}.tar.gz && \
  tar -xzf ${SEQYCLEANVER}.tar.gz && \
  rm -r ${SEQYCLEANVER}.tar.gz && \
  cd /seqyclean-${SEQYCLEANVER} && \
  make && mkdir /data

COPY Adapters_plus_PhiX_174.fasta /.

# Set working directory
WORKDIR /data

# add to path
ENV PATH="/seqyclean-${SEQYCLEANVER}/bin:${PATH}"

# testing
FROM app as test

RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
  wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
  seqyclean -minlen 25 -qual -c /Adapters_plus_PhiX_174.fasta -1 SRR13957123_1.fastq.gz -2 SRR13957123_2.fastq.gz -o SRR13957123_clean

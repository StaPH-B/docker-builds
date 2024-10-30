ARG MASURCA_VER="4.1.2"

FROM ubuntu:jammy AS builder

ARG MINIMAP2_VER="2.28"
ARG BWA_VER="0.7.18"
ARG MASURCA_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  build-essential \
  curl \
  wget \
  gcc \
  zlib1g-dev \
  bzip2 \
  libboost-dev \
  libbz2-dev \
  liblzma-dev \
  numactl \
  procps

# install minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner && \
  cp minimap2-${MINIMAP2_VER}_x64-linux/minimap2 /usr/local/bin && \
  minimap2 --version

# install bwa
RUN wget https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz && \
  tar -xvf v${BWA_VER}.tar.gz && \
  cd bwa-${BWA_VER} && \
  make && \
  mv bwa /usr/local/bin/

# install masurca suite
# the last line of install.sh is to copy Flye to bin, but it already installed Flye there
RUN wget -q https://github.com/alekseyzimin/masurca/releases/download/v${MASURCA_VER}/MaSuRCA-${MASURCA_VER}.tar.gz && \
  tar -xvf MaSuRCA-${MASURCA_VER}.tar.gz && \
  cd /MaSuRCA-${MASURCA_VER} && \
  bash install.sh || true

FROM ubuntu:jammy AS app

ARG MASURCA_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="masurca"
LABEL software.version="${MASURCA_VER}"
LABEL description="Genome Assembly and Analysis"
LABEL website="https://github.com/alekseyzimin/masurca"
LABEL license="https://github.com/alekseyzimin/masurca/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  wget \
  numactl \
  procps \
  perl \
  unzip \
  bzip2 \
  file && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /MaSuRCA-${MASURCA_VER} /MaSuRCA-${MASURCA_VER}

#RUN ls / && ls /MaSuRCA* && ls /MaSuRCA*/Flye/bin && ls /MaSuRCA*/bin && ls /MaS*/bin/polca.sh && hweaver

ENV PATH="${PATH}:/MaSuRCA-${MASURCA_VER}/Flye/bin:/MaSuRCA-${MASURCA_VER}/bin" \
  LC_ALL=C

CMD masurca --help

WORKDIR /data

FROM app as test

RUN masurca --help && masurca --version

# testing POLCA
WORKDIR /test1

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
  wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
  wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
  polca.sh -a SRR13957123.consensus.fa -r 'SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz' && \
  test -f SRR13957123.consensus.fa.PolcaCorrected.fa

# testing hybrid assembly
WORKDIR /test2

#RUN ls /MaSuRCA-4.1.2/bin && cat /MaSuRCA-4.1.2/bin/expand_fastq && whatever

RUN wget -q https://github.com/rrwick/Unicycler/raw/69e712eb95c4b9f8a46aade467260260a9ce7a91/sample_data/short_reads_1.fastq.gz && \
  wget -q https://github.com/rrwick/Unicycler/raw/69e712eb95c4b9f8a46aade467260260a9ce7a91/sample_data/short_reads_2.fastq.gz && \
  wget -q https://github.com/rrwick/Unicycler/raw/69e712eb95c4b9f8a46aade467260260a9ce7a91/sample_data/long_reads_low_depth.fastq.gz && \
  echo "masurca -t 2 -i short_reads_1.fastq.gz,short_reads_2.fastq.gz -r long_reads_low_depth.fastq.gz && hweagver"

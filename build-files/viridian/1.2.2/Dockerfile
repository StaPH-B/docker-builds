ARG VIRIDIAN_VER="1.2.2"
ARG SAMTOOLS_VER="1.20"
ARG BCFTOOLS_VER=${SAMTOOLS_VER}
ARG HTSLIB_VER=${SAMTOOLS_VER}
ARG ENA_VER="1.7.1"
ARG NGMERGE_VER="0.3"
ARG VT_VER="0.57721"
ARG RACON_VER="1.5.0"
ARG MUMMER_VER="4.0.0rc1"
ARG READITANDKEEP_VER="0.3.0"
ARG CYLON_COMMIT_HASH="57d559a76254b0b95785f7c02fa58ef806713e01"
ARG VARIFIER_COMMIT_HASH="8bc8726ed3cdb337dc47b62515e709759e451137"
ARG MINIMAP2_VER="2.28"

## Builder ##
FROM ubuntu:jammy as build
ARG SAMTOOLS_VER
ARG BCFTOOLS_VER
ARG HTSLIB_VER
ARG NGMERGE_VER
ARG VT_VER
ARG RACON_VER
ARG READITANDKEEP_VER
ARG MINIMAP2_VER
ARG MUMMER_VER

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
  wget \
  ca-certificates \
  perl \
  bzip2 \
  cmake \
  git \
  autoconf \
  automake \
  make \
  curl \
  gcc \
  g++ \
  gnuplot \
  zlib1g-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  libncurses5-dev \
  libssl-dev \
  libperl-dev \
  libgsl0-dev \
  procps \
  gawk \
  sed \
  build-essential \
  unzip \
  nasm \
  pkgconf \
  libtool \
  ruby \
  yaggo \
  gcc-11 && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# compile bcftools
RUN wget -q https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VER}/bcftools-${BCFTOOLS_VER}.tar.bz2 && \
  tar -xjf bcftools-${BCFTOOLS_VER}.tar.bz2 && \
  rm -v bcftools-${BCFTOOLS_VER}.tar.bz2 && \
  cd bcftools-${BCFTOOLS_VER} && \
  make && \
  make install

# compile samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
  cd samtools-${SAMTOOLS_VER} && \
  ./configure && \
  make && \
  make install

# compile htslib
RUN wget -q https://github.com/samtools/htslib/releases/download/${HTSLIB_VER}/htslib-${HTSLIB_VER}.tar.bz2 && \
  tar -vxjf htslib-${HTSLIB_VER}.tar.bz2 && \
  rm -v htslib-${HTSLIB_VER}.tar.bz2 && \
  cd htslib-${HTSLIB_VER} && \
  make && \
  make install

# compile NGmerge
RUN wget -q https://github.com/harvardinformatics/NGmerge/archive/refs/tags/v${NGMERGE_VER}.tar.gz && \
  tar -vxf v${NGMERGE_VER}.tar.gz && \
  cd NGmerge-${NGMERGE_VER} && \
  make && \
  cp NGmerge /usr/local/bin/.

# compile vt
RUN wget -q https://github.com/atks/vt/archive/refs/tags/${VT_VER}.tar.gz && \
  tar -vxf ${VT_VER}.tar.gz && \
  cd vt-${VT_VER} && \
  make && \
  cp vt /usr/local/bin/.

# compile racon
RUN wget -q https://github.com/lbcb-sci/racon/archive/refs/tags/${RACON_VER}.tar.gz && \
  tar -xvf ${RACON_VER}.tar.gz && \
  cd racon-${RACON_VER} && \
  mkdir build && \
  cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make && \
  cp bin/racon /usr/local/bin/.

# compile read-it-and-keep
RUN wget -q https://github.com/GlobalPathogenAnalysisService/read-it-and-keep/archive/refs/tags/v${READITANDKEEP_VER}.tar.gz && \
  tar -vxf v${READITANDKEEP_VER}.tar.gz && \
  cd read-it-and-keep-${READITANDKEEP_VER}/src && \
  make && \
  cp readItAndKeep /usr/local/bin/.

# install minimap2 binary
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner && \
  cp minimap2-${MINIMAP2_VER}_x64-linux/minimap2 /usr/local/bin

RUN wget -q https://github.com/mummer4/mummer/archive/refs/tags/v${MUMMER_VER}.tar.gz && \
  tar -xvf v${MUMMER_VER}.tar.gz && \
  cd mummer-${MUMMER_VER} && \
  autoreconf -i && \
  ./configure CXXFLAGS="-std=c++11 -Wno-maybe-uninitialized" LDFLAGS=-static && \
  make && \
  make install && \
  ldconfig

## App ##
FROM ubuntu:jammy as app

ARG VIRIDIAN_VER
ARG ENA_VER
ARG CYLON_COMMIT_HASH
ARG VARIFIER_COMMIT_HASH

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="viridian"
LABEL software.version="${VIRIDIAN_VER}"
LABEL description="Ultra-careful amplicon-aware viral assembly for tiled amplicon schemes."
LABEL website="https://github.com/iqbal-lab-org/viridian"
LABEL license="https://github.com/iqbal-lab-org/viridian/blob/master/LICENSE"
LABEL maintainer="Wilson Chan"
LABEL maintainer.email="chan.wilson.wc@gmail.com"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  python3 \
  python3-pip \
  python3-dev \
  gzip \
  gcc \
  perl \
  zlib1g \
  libncurses5 \
  bzip2 \
  liblzma-dev \
  libcurl4-gnutls-dev \
  wget \
  && apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=build /usr/local/bin/* /usr/local/bin/
COPY --from=build /usr/local/lib/* /usr/local/lib/

RUN pip install --no-cache-dir cython

# ENA tools
RUN wget -q https://github.com/enasequence/enaBrowserTools/archive/refs/tags/v${ENA_VER}.tar.gz && \
  tar -xvf v${ENA_VER}.tar.gz && \
  rm v${ENA_VER}.tar.gz

RUN wget -q https://github.com/iqbal-lab-org/cylon/archive/${CYLON_COMMIT_HASH}.zip &&\
  pip install --no-cache-dir ${CYLON_COMMIT_HASH}.zip && \
  rm ${CYLON_COMMIT_HASH}.zip

RUN wget -q https://github.com/iqbal-lab-org/varifier/archive/${VARIFIER_COMMIT_HASH}.zip &&\
  pip install --no-cache-dir ${VARIFIER_COMMIT_HASH}.zip && \
  rm ${VARIFIER_COMMIT_HASH}.zip 

# install viridian
RUN wget -q https://github.com/iqbal-lab-org/viridian/archive/refs/tags/v${VIRIDIAN_VER}.tar.gz && \
  pip install --no-cache-dir v${VIRIDIAN_VER}.tar.gz && \
  mkdir viridian && \
  tar -C viridian --strip-components=1 -xvf v${VIRIDIAN_VER}.tar.gz && \
  rm v${VIRIDIAN_VER}.tar.gz

WORKDIR /data

CMD ["viridian", "--help "]

ENV PATH="/enaBrowserTools-${ENA_VER}/python3:$PATH" LC_ALL=C

## Test ##
FROM app as test

WORKDIR /test

RUN cd /viridian && \
  pip install --no-cache-dir pytest && \
  pytest

RUN viridian run_one_sample --run_accession SRR29437696 --outdir OUT && \
  wc -l OUT/consensus.fa.gz OUT/log.json.gz OUT/qc.tsv.gz && \
  head OUT/variants.vcf

RUN viridian run_one_sample --run_accession SRR29437696 --outdir OUT2 --keep_bam && \
  wc -l OUT2/consensus.fa.gz OUT2/log.json.gz OUT2/qc.tsv.gz OUT2/reference_mapped.bam && \
  head OUT2/variants.vcf

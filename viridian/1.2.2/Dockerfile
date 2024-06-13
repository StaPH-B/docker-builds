FROM ubuntu:20.04 as app

ARG VIRIDIAN_VERSION=1.2.2

LABEL base.image="ubuntu:20.04"
LABEL dockerfile.version="1"
LABEL software="viridian"
LABEL software.version="${VIRIDIAN_VERSION}"
LABEL description="Ultra-careful amplicon-aware viral assembly for tiled amplicon schemes."
LABEL website="https://github.com/iqbal-lab-org/viridian"
LABEL license="https://github.com/iqbal-lab-org/viridian/blob/master/LICENSE"
LABEL maintainer="Wilson Chan"
LABEL maintainer.email="chan.wilson.wc@gmail.com"

# Dependency pins
ARG ENA_VERSION=1.7.1
ARG BCFTOOLS_VERSION=1.10.2
ARG MUMMER_VERSION=4.0.0
ARG NGMERGE_COMMIT_HASH=224fc6a0066024e05965d101d998704815cb4c41
ARG VT_COMMIT_HASH=2187ff6347086e38f71bd9f8ca622cd7dcfbb40c
ARG MINIMAP2_COMMIT_HASH=b0b199f5039e8da5e8d1a9a7ae130580fd33fe1f
ARG CYLON_COMMIT_HASH=57d559a76254b0b95785f7c02fa58ef806713e01

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/bioinf-tools/:/bioinf-tools/enaBrowserTools/python3/:$PATH

ARG BIOINF_TOOLS=/bioinf-tools

RUN apt-get update && apt-get install -y software-properties-common && \
  apt-add-repository universe && apt-get update

RUN apt-get install -y \
  build-essential \
  cmake \
  automake \
  gcc \
  gcc-10 \
  g++-10 \
  gdb \
  git \
  python3 \
  python3-pip \
  python3-setuptools \
  python3-dev \
  wget \
  zlib1g-dev \
  libbz2-dev \
  liblzma-dev \
  libhts-dev \
  tabix \
  curl \
  libvcflib-tools \
  libcurl4-gnutls-dev \
  libssl-dev \
  samtools

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave \
  /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10

RUN python3 -m pip install tox

WORKDIR ${BIOINF_TOOLS}

# Begin Dependency Install

RUN mkdir -p enaBrowserTools && \
  wget -qO- https://github.com/enasequence/enaBrowserTools/archive/refs/tags/v${ENA_VERSION}.tar.gz | \
  tar xz --strip-components=1 -C enaBrowserTools

RUN git clone https://github.com/harvardinformatics/NGmerge.git NGmerge-git && \
  cd NGmerge-git && git checkout ${NGMERGE_COMMIT_HASH} && make install

RUN mkdir -p bcftools-git && \
  wget -qO- https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 | \
  tar xj --strip-components=1 -C bcftools-git && cd bcftools-git && make install

RUN git clone https://github.com/atks/vt.git vt-git && \
  cd vt-git && git checkout ${VT_COMMIT_HASH} && make && mv vt ${BIOINF_TOOLS}

RUN git clone https://github.com/lh3/minimap2.git minimap2-git && \
  cd minimap2-git && git checkout ${MINIMAP2_COMMIT_HASH} && \
  if [ "$(dpkg --print-architecture | grep '^arm' | wc -l)" -eq 1 ]; then \
  make arm_neon=1 aarch64=1; else make; fi && \
  mv minimap2 ${BIOINF_TOOLS}

RUN git clone --recursive https://github.com/lbcb-sci/racon.git racon-git && \
  cd racon-git && mkdir build && cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make CC=gcc-10 CPP=g++-10 CXX=g++-10 LD=g++-10 && \
  make install

RUN mkdir -p mummer-git && \
  wget -qO- https://github.com/mummer4/mummer/releases/download/v${MUMMER_VERSION}rc1/mummer-${MUMMER_VERSION}rc1.tar.gz | \
  tar xz --strip-component=1 -C mummer-git && \
  cd mummer-git && ./configure LDFLAGS=-static && make && make install && ldconfig

RUN git clone https://github.com/iqbal-lab-org/cylon.git cylon-git && \
  cd cylon-git && git checkout ${CYLON_COMMIT_HASH} && python3 -m pip install .

RUN git clone https://github.com/GlobalPathogenAnalysisService/read-it-and-keep.git && \
  cd read-it-and-keep && git checkout ${READITANDKEEP_COMMIT_HASH} && \
  cd src && make && cd ${BIOINF_TOOLS} && cp -s ${BIOINF_TOOLS}/read-it-and-keep/src/readItAndKeep .

RUN git clone https://github.com/iqbal-lab-org/varifier.git varifier && \
  cd varifier && git checkout ${VARIFIER_COMMIT_HASH} && python3 -m pip install .

# Clean up left over git folders
RUN find . -type d -name "*-git" -print0 | xargs -0 rm -rf

WORKDIR /data

RUN wget -qO- https://github.com/iqbal-lab-org/viridian/archive/refs/tags/v${VIRIDIAN_VERSION}.tar.gz | \
  tar xz --strip-components=1 -C . && \
  python3 -m pip install pytest && \
  python3 -m pip install -r requirements.txt && \
  python3 -m pip install .

CMD ["viridian"]

## Test ##
FROM app as test

WORKDIR /test

COPY --from=app /data /test

RUN pytest

RUN viridian run_one_sample --run_accession SRR12345678 --outdir OUT

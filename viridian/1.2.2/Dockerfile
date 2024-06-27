FROM ubuntu:20.04 as build

LABEL base.image="ubuntu:20.04"
LABEL dockerfile.version="1"
LABEL software="viridian"
LABEL software.version="${VIRIDIAN_VERSION}"
LABEL description="Ultra-careful amplicon-aware viral assembly for tiled amplicon schemes."
LABEL website="https://github.com/iqbal-lab-org/viridian"
LABEL license="https://github.com/iqbal-lab-org/viridian/blob/master/LICENSE"
LABEL maintainer="Wilson Chan"
LABEL maintainer.email="chan.wilson.wc@gmail.com"

ARG VIRIDIAN_VERSION=1.2.2
ARG ENA_VERSION=1.7.1
ARG BCFTOOLS_VERSION=1.10.2
ARG MUMMER_VERSION=4.0.0
ARG NGMERGE_COMMIT_HASH=224fc6a0066024e05965d101d998704815cb4c41
ARG VT_COMMIT_HASH=2187ff6347086e38f71bd9f8ca622cd7dcfbb40c
ARG MINIMAP2_COMMIT_HASH=b0b199f5039e8da5e8d1a9a7ae130580fd33fe1f
ARG CYLON_COMMIT_HASH=57d559a76254b0b95785f7c02fa58ef806713e01
ARG READITANDKEEP_COMMIT_HASH=61ae15be1e515c960b0135eae7dd59568a9de30d
ARG VARIFIER_COMMIT_HASH=8bc8726ed3cdb337dc47b62515e709759e451137

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/usr/local/bin:/data/enaBrowserTools/python3/:$PATH

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential \
  cmake \
  gcc-10 \
  g++-10 \
  git \
  python3 \
  python3-pip \
  python3-dev \
  wget \
  zlib1g-dev \
  libbz2-dev \
  liblzma-dev \
  libhts-dev \
  libcurl4-gnutls-dev \
  libssl-dev \
  samtools && \
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10 && \
  python3 -m pip install tox

WORKDIR /tmp

# Install dependencies
RUN git clone https://github.com/harvardinformatics/NGmerge.git NGmerge && \
  cd NGmerge && git checkout ${NGMERGE_COMMIT_HASH} && make install

RUN mkdir -p bcftools && \
  wget -qO- https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2 | tar xj --strip-components=1 -C bcftools && \
  cd bcftools && make install

RUN git clone https://github.com/atks/vt.git vt && \
  cd vt && git checkout ${VT_COMMIT_HASH} && make && mv vt /usr/local/bin/

RUN git clone https://github.com/lh3/minimap2.git minimap2 && \
  cd minimap2 && git checkout ${MINIMAP2_COMMIT_HASH} && \
  if [ "$(dpkg --print-architecture | grep '^arm' | wc -l)" -eq 1 ]; then \
  make arm_neon=1 aarch64=1; else make; fi && \
  mv minimap2 /usr/local/bin/

RUN git clone --recursive https://github.com/lbcb-sci/racon.git racon && \
  cd racon && mkdir build && cd build && \
  cmake -DCMAKE_BUILD_TYPE=Release .. && \
  make CC=gcc-10 CPP=g++-10 CXX=g++-10 LD=g++-10 && \
  make install

RUN mkdir -p mummer && \
  wget -qO- https://github.com/mummer4/mummer/releases/download/v${MUMMER_VERSION}rc1/mummer-${MUMMER_VERSION}rc1.tar.gz | \
  tar xz --strip-components=1 -C mummer && \
  cd mummer && ./configure LDFLAGS=-static && make && make install && ldconfig

RUN git clone https://github.com/iqbal-lab-org/cylon.git cylon && \
  cd cylon && git checkout ${CYLON_COMMIT_HASH} && python3 -m pip install .

RUN git clone https://github.com/GlobalPathogenAnalysisService/read-it-and-keep.git read-it-and-keep && \
  cd read-it-and-keep && git checkout ${READITANDKEEP_COMMIT_HASH} && \
  cd src && make && mv readItAndKeep /usr/local/bin/

RUN git clone https://github.com/iqbal-lab-org/varifier.git varifier && \
  cd varifier && git checkout ${VARIFIER_COMMIT_HASH} && python3 -m pip install .

FROM build as app

COPY --from=build /usr/local/bin/* /usr/local/bin/

WORKDIR /data

RUN mkdir -p enaBrowserTools && \
  wget -qO- https://github.com/enasequence/enaBrowserTools/archive/refs/tags/v${ENA_VERSION}.tar.gz | \
  tar xz --strip-components=1 -C enaBrowserTools

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

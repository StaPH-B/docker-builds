FROM ubuntu:bionic

# for easy upgrade later. ARG variables only persist during image build
ARG SHIGATYPERVER=1.0.6
ARG SAMTOOLSVER=1.9
ARG BCFTOOLSVER=1.9
ARG MINIMAP2VER=2.16
ARG PANDASVER=0.24.2

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Shigatyper"
LABEL software.version="1.0.6"
LABEL description="Determines Shigella serotype"
LABEL website="https://github.com/CFSAN-Biostatistics/shigatyper"
LABEL license="https://anaconda.org/bioconda/shigatyper/badges/license.svg"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies and clean up apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 zlib1g-dev \
 libssl-dev \
 curl \
 gcc \
 wget \
 make \
 perl \
 python3 \
 python3-pip \
 python3-setuptools \
 bzip2 \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
 tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
 rm samtools-${SAMTOOLSVER}.tar.bz2 && \
 cd samtools-${SAMTOOLSVER} && \
 ./configure && \
 make && \
 make install

# install bcftools
RUN wget https://github.com/samtools/bcftools/releases/download/${BCFTOOLSVER}/bcftools-${BCFTOOLSVER}.tar.bz2 && \
 tar -vxjf bcftools-${BCFTOOLSVER}.tar.bz2 && \
 rm bcftools-${BCFTOOLSVER}.tar.bz2 && \
 cd bcftools-${BCFTOOLSVER} && \
 make && \
 make install

# install minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2VER}/minimap2-${MINIMAP2VER}_x64-linux.tar.bz2 | tar -jxvf -

# install pandas
RUN pip3 install --upgrade pip && \
  pip3 install pandas==${PANDASVER}

# install shigatyper and make /data
RUN wget https://github.com/CFSAN-Biostatistics/shigatyper/archive/refs/tags/conda-package-${SHIGATYPERVER}.tar.gz && \
  tar -xvf conda-package-${SHIGATYPERVER}.tar.gz && \
  rm conda-package-${SHIGATYPERVER}.tar.gz && \
  cd shigatyper-conda-package-${SHIGATYPERVER} && \
  python3 setup.py build && \
  python3 setup.py install && \
  mkdir /data

# set perl locale settings
ENV LC_ALL=C

# set PATH
ENV PATH="${PATH}:/minimap2-${MINIMAP2VER}_x64-linux"

WORKDIR /data

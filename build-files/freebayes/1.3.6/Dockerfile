FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time
ARG FREEBAYES_VER="1.3.6"
ARG SAMTOOLSVER="1.14"
ARG VCFTOOLS_VER="0.1.16"

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="FreeBayes"
LABEL software.version="1.3.6"
LABEL description="FreeBayes is a haplotype-based variant detector and is a great tool for calling variants from a population."
LABEL website="https://github.com/freebayes/freebayes"
LABEL license="https://github.com/freebayes/freebayes/blob/master/LICENSE"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="jvhagey@gmail.com"

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        build-essential \
        pkg-config \
        meson \
        zlib1g-dev \
        liblzma-dev \
        libbz2-dev \
        libncurses5-dev \
        libc6 \
        libgcc-s1 \
        libstdc++6 \
        libvcflib1 \
        libvcflib-tools \
        bc \
        parallel \
        ninja-build \
        wget && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Build and install samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
    rm samtools-${SAMTOOLSVER}.tar.bz2 && \
    cd samtools-${SAMTOOLSVER} && \
    ./configure && \
    make && \
    make install
  
# Build and install vcftools
RUN wget https://github.com/vcftools/vcftools/releases/download/v${VCFTOOLS_VER}/vcftools-${VCFTOOLS_VER}.tar.gz && \
    tar -vxzf vcftools-${VCFTOOLS_VER}.tar.gz && \
    rm vcftools-${VCFTOOLS_VER}.tar.gz && \
    cd vcftools-${VCFTOOLS_VER} && \
    ./configure && \
    make && \
    make install

# Build and install freebayes
RUN wget https://github.com/freebayes/freebayes/releases/download/v${FREEBAYES_VER}/freebayes-${FREEBAYES_VER}-src.tar.gz && \
    tar -xvzf freebayes-${FREEBAYES_VER}-src.tar.gz && \
    rm freebayes-${FREEBAYES_VER}-src.tar.gz && \
    cd freebayes && \
    meson build/ --buildtype debug && \
    cd build && \
    ninja && \
    mkdir /data

# set perl locale settings
# Required by most tools that use perl with singularity so we can use container with both docker and singularity
ENV LC_ALL=C

# Add files paths of software
ENV PATH="${PATH}:/freebayes/build\
:/samtools-${SAMTOOLSVER}\
:/vcftools-${VCFTOOLS_VER}"

# Add references and entrypoint script
WORKDIR /data

# new base for testing
FROM app as test

# Run test
RUN cd /freebayes/build && \
    ninja test

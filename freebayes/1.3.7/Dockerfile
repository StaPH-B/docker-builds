FROM ubuntu:jammy as builder

ARG FREEBAYES_VER="1.3.7"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    build-essential \
    pkg-config \
    meson \
    cmake \
    zlib1g-dev \
    liblzma-dev \
    libbz2-dev \
    libncurses5-dev \
    libc6 \
    libgcc-s1 \
    libstdc++6 \
    libvcflib1 \
    libvcflib-tools \
    libseqlib-dev \
    libvcflib-dev \
    bc \
    parallel \
    ninja-build \
    wget \
    samtools \
    vcftools && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget https://github.com/freebayes/freebayes/archive/refs/tags/v${FREEBAYES_VER}.tar.gz && \
    tar -xvzf v${FREEBAYES_VER}.tar.gz && \
    mv freebayes-${FREEBAYES_VER} /freebayes && \
    cd /freebayes && \
    meson build/ && \
    cd build && \
    ninja

RUN /freebayes/build/freebayes --help

FROM ubuntu:jammy as app

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="FreeBayes"
LABEL software.version="1.3.7"
LABEL description="FreeBayes is a haplotype-based variant detector and is a great tool for calling variants from a population."
LABEL website="https://github.com/freebayes/freebayes"
LABEL license="https://github.com/freebayes/freebayes/blob/master/LICENSE"
LABEL maintainer="Kitty Chase"
LABEL maintainer.email="kitty.chase@dhhs.nc.gov"
LABEL maintainer2="Jill Hagey"
LABEL maintainer2.email="jvhagey@gmail.com"

COPY --from=builder /freebayes/build/* /usr/local/bin/

# vcftools version is 0.1.16
# samtools version is 1.13
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    bc \
    ca-certificates \
    libseqlib-dev \
    libvcflib-tools \
    parallel \
    procps \
    samtools \
    vcftools \
    wget && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN freebayes --help && vcftools --help && samtools --help

ENV LC_ALL=C

WORKDIR /data

CMD freebayes --help

# new base for testing
FROM app as test

RUN freebayes --help && vcftools --help && samtools --help

RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123.sorted.bam && \
    wget -q https://raw.githubusercontent.com/UPHL-BioNGS/Cecret/master/genomes/MN908947.3.fasta && \
    freebayes -f MN908947.3.fasta SRR13957123.sorted.bam > var.vcf && \
    head var.vcf

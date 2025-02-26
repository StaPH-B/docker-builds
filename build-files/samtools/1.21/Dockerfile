ARG SAMTOOLS_VER="1.21"

FROM ubuntu:jammy as builder

ARG SAMTOOLS_VER

# install dependencies required for compiling samtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    libdeflate-dev \
    gcc \
    wget \
    make \
    perl \
    bzip2 \
    gnuplot \
    ca-certificates

# download, compile, and install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install && \
    make test

### start of app stage ###
FROM ubuntu:jammy as app

ARG SAMTOOLS_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="samtools"
LABEL software.version="${SAMTOOLS_VER}"
LABEL description="Tools (written in C using htslib) for manipulating next-generation sequencing data"
LABEL website="https://github.com/samtools/samtools"
LABEL license="https://github.com/samtools/samtools/blob/develop/LICENSE"
LABEL maintainer="Shelby Bennett"
LABEL maintainer.email="shelby.bennett@dgs.virginia.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"
LABEL maintainer4="Kutluhan Incekara"
LABEL maintainer4.email="kutluhan.incekara@ct.gov"

ARG DEBIAN_FRONTEND=noninteractive

# install dependencies required for running samtools
# 'gnuplot' required for plot-ampliconstats
RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    zlib1g \
    libncurses5 \
    bzip2 \
    liblzma5 \
    libcurl3-gnutls \
    libdeflate0 \
    gnuplot \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# copy in samtools executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/

ENV LC_ALL=C

# final working directory is /data
WORKDIR /data

# default command is to pull up help options
CMD ["samtools", "--help"]

### start of test stage ###
FROM app as test

ARG SAMTOOLS_VER

# check PATH
RUN samtools --help

# install make and wget for downloading test files
RUN apt-get update && apt-get install --no-install-recommends -y wget ca-certificates

WORKDIR /test

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
    wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.primer.bed && \
    samtools stats SRR13957123.primertrim.sorted.bam && \
    samtools faidx SRR13957123.consensus.fa && \
    samtools ampliconstats nCoV-2019.primer.bed SRR13957123.primertrim.sorted.bam > SRR13957123_ampliconstats.txt && \
    plot-ampliconstats plot SRR13957123_ampliconstats.txt && \
    ls

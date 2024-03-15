ARG SAMTOOLS_VER=1.19
ARG BOWTIE2_VER=2.5.3

FROM ubuntu:jammy as builder

ARG SAMTOOLS_VER
ARG BOWTIE2_VER

# install dependencies required for compiling samtools
RUN apt-get update && apt-get install --no-install-recommends -y \
  libncurses5-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  zlib1g-dev \
  libssl-dev \
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
  make install

FROM ubuntu:jammy as app

ARG SAMTOOLSVER
ARG BOWTIE2_VER

# metadata (there are a few other labels you can add, these are optional but preferred!)
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Bowtie2"
LABEL software.version=$BOWTIE2_VER
LABEL description="Bowtie2: Genome assembler using a reference and mapping"
LABEL website="https://github.com/BenLangmead/bowtie2"
LABEL documentation="http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml"
LABEL maintainer="Holly Halstead"
LABEL maintainer.email="holly.halstead@doh.wa.gov"

# install dependencies, cleanup apt garbage.
RUN apt-get update && apt-get install -y --no-install-recommends\
  wget \
  ca-certificates \
  procps \
  unzip \
  libsys-hostname-long-perl \
  python3 \
  gzip && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/* /usr/local/bin/

# download, unpack Bowtie2
RUN wget -q https://sourceforge.net/projects/bowtie-bio/files/bowtie2/${BOWTIE2_VER}/bowtie2-${BOWTIE2_VER}-linux-x86_64.zip/download && \
  unzip download && \
  rm -rf download

ENV PATH="$PATH:/bowtie2-${BOWTIE2_VER}-linux-x86_64/"

CMD bowtie2 --help

# set working directory
WORKDIR /data

FROM app as test

ARG BOWTIE2_VER

WORKDIR /test

RUN bowtie2 -h && \
  bowtie2 --version && \
  bowtie2-align-s -h && \
  bowtie2-align-l -h && \
  bowtie2-build -h && \
  bowtie2-build-s -h && \
  bowtie2-build-l -h && \
  bowtie2-inspect -h && \
  bowtie2-inspect-s -h && \
  bowtie2-inspect-l -h

RUN bowtie2 -x /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/index/lambda_virus -U /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/reads/longreads.fq > example1.sam && head example1.sam && \
  bowtie2 -x /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/index/lambda_virus -1 /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/reads/reads_1.fq -2 /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/reads/reads_2.fq > example2.sam && head example2.sam && \
  bowtie2-build /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/reference/lambda_virus.fa example3 && ls example3*bt2 && \
  bowtie2-build --large-index /bowtie2-${BOWTIE2_VER}-linux-x86_64/example/reference/lambda_virus.fa example4 && ls example4*bt2l && \
  bowtie2-inspect --summary example3 > example5.txt && head example5.txt && \
  bowtie2-inspect --large-index example4 > example6.txt && head example6.txt
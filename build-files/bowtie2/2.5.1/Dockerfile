# FROM defines the base docker image to start from. This command has to come first in the file
FROM --platform=linux/x86_64 ubuntu:xenial as app

ARG SAMTOOLSVER=1.15
ARG BOWTIE2VER=2.5.1

# metadata (there are a few other labels you can add, these are optional but preferred!)
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Bowtie2"
LABEL software.version=$BOWTIE2VER
LABEL description="Bowtie2: Genome assembler using a reference and mapping\n Samtools: a set of tools for interacting with and reformatting sequence data"
LABEL website="http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml\n https://www.htslib.org/"
LABEL maintainer="Holly Halstead"
LABEL maintainer.email="holly.halstead@doh.wa.gov"

# install dependencies, cleanup apt garbage.
RUN apt-get update && apt-get install -y --no-install-recommends\
 build-essential=12.1ubuntu2  \
 autoconf=2.69-9 \
 zlib1g-dev=1:1.2.8.dfsg-2ubuntu4.3  \
 python3=3.5.1-3  \
 wget=1.17.1-1ubuntu1.5 \
 libbz2-dev=1.0.6-8ubuntu0.2 \
 liblzma-dev=5.1.1alpha+20120614-2ubuntu2 \
 libncurses5-dev=6.0+20160213-1ubuntu1 \
 bedtools=2.25.0-1 \
 python3-pip=8.1.1-2ubuntu0.6 \
 unzip=6.0-20ubuntu1.1  && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download, unpack Bowtie2 and Samtools
RUN wget -q -O bowtie2.zip https://sourceforge.net/projects/bowtie-bio/files/bowtie2/${BOWTIE2VER}/bowtie2-${BOWTIE2VER}-linux-x86_64.zip/download; \
  unzip bowtie2.zip -d /opt/; \
  ln -s /opt/bowtie2-${BOWTIE2VER}-linux-x86_64/ /opt/bowtie2; \
  rm bowtie2.zip
  ENV PATH $PATH:/opt/bowtie2


#samtools# SAMtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
  rm samtools-${SAMTOOLSVER}.tar.bz2 && \
  cd samtools-${SAMTOOLSVER} && \
  ./configure && \
  make && \
  make install

# set working directory
WORKDIR /data

FROM app as test

RUN wget https://raw.githubusercontent.com/BenLangmead/bowtie2/master/example/reads/longreads.fq && \
 wget https://raw.githubusercontent.com/BenLangmead/bowtie2/master/example/reference/lambda_virus.fa &&  \
 bowtie2-build lambda_virus.fa lambda_virus && \
 bowtie2 -x lambda_virus -U longreads.fq

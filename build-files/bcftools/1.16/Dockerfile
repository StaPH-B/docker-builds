FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during build time
ARG bcftoolsVer="1.16"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="bcftools"
LABEL software.version="${bcftoolsVer}"
LABEL description="Variant calling and manipulating files in the Variant Call Format (VCF) and its binary counterpart BCF"
LABEL website="https://github.com/samtools/bcftools"
LABEL license="https://github.com/samtools/bcftools/blob/develop/LICENSE"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install dependencies, cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
 wget \
 ca-certificates \
 perl \
 bzip2 \
 autoconf \
 automake \
 make \
 gcc \
 zlib1g-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 libssl-dev \
 libperl-dev \
 libgsl0-dev && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# get bcftools and make /data
RUN wget https://github.com/samtools/bcftools/releases/download/${bcftoolsVer}/bcftools-${bcftoolsVer}.tar.bz2 && \
 tar -vxjf bcftools-${bcftoolsVer}.tar.bz2 && \
 rm bcftools-${bcftoolsVer}.tar.bz2 && \
 cd bcftools-${bcftoolsVer} && \
 make && \
 make install && \
 mkdir /data

# set $PATH (honestly unnecessary here, lol) and locale settings for singularity compatibility
ENV PATH="$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

FROM app as test

RUN wget https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V4/SARS-CoV-2.reference.fasta && \
  wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
  bcftools mpileup -A -d 200 -B -Q 0 -f SARS-CoV-2.reference.fasta SRR13957123.primertrim.sorted.bam | \
  bcftools call -mv -Ov -o SRR13957123.vcf

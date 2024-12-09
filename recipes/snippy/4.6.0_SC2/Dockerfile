ARG SNIPPY_VER="4.6.0"

FROM ubuntu:bionic as app

ARG SNIPPY_VER

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL container.version="1.0.0"
LABEL software="Snippy"
LABEL software.version="${SNIPPY_VER}"
LABEL description="Rapid haploid variant calling and core genome alignment"
LABEL website="https://github.com/tseemann/snippy"
LABEL license="https://github.com/tseemann/snippy/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

### install dependencies ###
# BioPerl version in ubuntu:bioinic 1.7.2 (as of March 2020)
# snp-sites now bundled w/ snippy
# parallel now bundled w/ snippy
# cpanminus removed (no need to install additional perl modules)
# g++ and gcc removed (no compiling needed)
RUN apt-get update && apt-get -y --no-install-recommends install \
 wget \ 
 libstdc++6 \ 
 libbz2-1.0 \
 autoconf \
 unzip \
 bzip2 \
 gzip \
 wget \
 perl \
 less \
 libdatetime-perl \
 libxml-simple-perl \
 libdigest-md5-perl \
 default-jre \
 bioperl \
 hmmer \
 zlib1g-dev \
 python \
 python3 \
 liblzma-dev \
 libbz2-dev \
 xz-utils \ 
 curl \
 libcurl4-openssl-dev \
 libssl-dev \
 make && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# bwa 0.7.17-r1188 - bundled

# minimap2 2.17-r941 - bundled

# samtools 1.10 - bundled

# bedtools 2.29.2 - bundled 
# dependencies required for bedtools (used to install via apt): 
# zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++ 
# these are probably only needed when installing from source and compiling - leaving just in case

# bcftools 1.10.2 - bundled

# freebayes 1.3.1-dirty - bundled
# python3 required for freebayes

# vcflib - bundled

# vt 0.5772-60f436c3 - bundled
# libcurl4-openssl-dev required for vt

# SnpEff 4.3t - bundled (build 2017-11-24 10:18)

# Seqtk 1.3-r106 - bundled

# Samclip 0.4 - bundled

# snp-sites 2.3.3 - via apt-get 

# any2fasta 0.4.2 - bundled

# wgsim 0.3.1-r13 - bundled for testing snippy

# Snippy ${SNIPPY_VER}, make /data, and grab reference genome
RUN wget https://github.com/tseemann/snippy/archive/v${SNIPPY_VER}.tar.gz && \
  tar -zxf v${SNIPPY_VER}.tar.gz && \
  rm v${SNIPPY_VER}.tar.gz && \
  mkdir /data /reference && \
  curl -s ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/858/895/GCF_009858895.2_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna.gz | gzip -dc > /reference/MN908947_SC2_reference.fasta


# set PATH and perl local settings
ENV PATH="${PATH}:\
/snippy-${SNIPPY_VER}/bin:\
/snippy-${SNIPPY_VER}/binaries/linux:\
/snippy-${SNIPPY_VER}/binaries/noarch" \
    LC_ALL=C

WORKDIR /data

FROM app as test

ARG SNIPPY_VER

# run tests from https://github.com/tseemann/snippy/blob/master/.travis.yml
RUN realpath . && \
  snippy --version && \
  snippy --check && \
  snippy-core --version && \
  snippy-core --check && \
  cd /snippy-${SNIPPY_VER} && \
  make -C test

WORKDIR /test
# Download SC2 fastqs for test, run Snippy 4.6.0
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR918/006/ERR9187736/ERR9187736_1.fastq.gz && \
  wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR918/006/ERR9187736/ERR9187736_2.fastq.gz && \
  snippy --cpus 2 --outdir results --ref /reference/MN908947_SC2_reference.fasta --R1 ERR9187736_1.fastq.gz --R2 ERR9187736_2.fastq.gz

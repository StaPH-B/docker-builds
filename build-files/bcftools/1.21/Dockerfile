# for easy upgrade later. ARG variables only persist during build time
ARG BCFTOOLS_VER="1.21"

FROM ubuntu:jammy as builder

# re-instantiate variable
ARG BCFTOOLS_VER

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
  libgsl0-dev \
  libdeflate-dev \
  procps && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean


# download, compile, and install bcftools
RUN wget https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VER}/bcftools-${BCFTOOLS_VER}.tar.bz2 && \
  tar -xjf bcftools-${BCFTOOLS_VER}.tar.bz2 && \
  rm -v bcftools-${BCFTOOLS_VER}.tar.bz2 && \
  cd bcftools-${BCFTOOLS_VER} && \
  ./configure --enable-libgsl --enable-perl-filters &&\
  make && \
  make install && \
  make test 

### start of app stage ###
FROM ubuntu:jammy as app

# re-instantiate variable
ARG BCFTOOLS_VER

# putting the labels in
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="bcftools"
LABEL software.version="${BCFTOOLS_VER}"
LABEL description="Variant calling and manipulating files in the Variant Call Format (VCF) and its binary counterpart BCF"
LABEL website="https://github.com/samtools/bcftools"
LABEL license="https://github.com/samtools/bcftools/blob/develop/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install dependencies required for running bcftools
# https://github.com/samtools/bcftools/blob/develop/INSTALL#L29
RUN apt-get update && apt-get install --no-install-recommends -y \
  perl\
  zlib1g \
  gsl-bin \
  bzip2 \
  liblzma5 \
  libcurl3-gnutls \
  libdeflate0 \  
  procps \
  && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# copy in bcftools executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/
# copy in bcftools plugins from builder stage
COPY --from=builder /usr/local/libexec/bcftools/* /usr/local/libexec/bcftools/

# set locale settings for singularity compatibility
ENV LC_ALL=C

# set final working directory
WORKDIR /data

# default command is to pull up help optoins
CMD ["bcftools", "--help"]

### start of test stage ###
FROM app as test

# running --help and listing plugins
RUN bcftools --help && bcftools plugin -lv

# install wget for downloading test files
RUN apt-get update && apt-get install -y wget vcftools

RUN echo "downloading test SC2 BAM and FASTA and running bcftools mpileup and bcftools call test commands..." && \
  wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V4/SARS-CoV-2.reference.fasta && \
  wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
  bcftools mpileup -A -d 200 -B -Q 0 -f SARS-CoV-2.reference.fasta SRR13957123.primertrim.sorted.bam | \
  bcftools call -mv -Ov -o SRR13957123.vcf
  
RUN echo "testing plugins..." && \
  bcftools +counts SRR13957123.vcf

RUN echo "testing polysomy..." && \
  wget https://samtools.github.io/bcftools/howtos/cnv-calling/usage-example.tgz &&\
  tar -xvf usage-example.tgz &&\
  zcat test.fcr.gz | ./fcr-to-vcf -b bcftools -a map.tab.gz -o outdir/ &&\
  bcftools cnv -o cnv/ outdir/test.vcf.gz &&\
  bcftools polysomy -o psmy/ outdir/test.vcf.gz &&\
  head psmy/dist.dat

RUN echo "reading test data from Google Cloud to validate GCS support" && \
  bcftools head -h 20 gs://genomics-public-data/references/hg38/v0/1000G_phase1.snps.high_confidence.hg38.vcf.gz

RUN  echo "reading test data from S3 to validate AWS support" && \
  bcftools head -h 20 s3://human-pangenomics/T2T/CHM13/assemblies/variants/GATK_CHM13v2.0_Resource_Bundle/resources-broad-hg38-v0-1000G_phase1.snps.high_confidence.hg38.t2t-chm13-v2.0.vcf.gz

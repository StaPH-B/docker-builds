FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1.0.0"
LABEL software="Snippy"
LABEL software.version="4.4.5"
LABEL description="Rapid haploid variant calling and core genome alignment"
LABEL website="https://github.com/tseemann/snippy"
LABEL license="https://github.com/tseemann/snippy/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
 wget \ 
 gcc \ 
 libstdc++6 \ 
 libbz2-1.0 \
 cpanminus \
 autoconf \
 parallel \
 unzip \
 libsnp-sites1 \
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
 liblzma-dev \
 libbz2-dev \
 xz-utils \ 
 curl \
 g++ \
 libcurl4-openssl-dev \
 libssl-dev \
 make && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* &&\
 apt-get remove -y samtools

# REMOVED FROM ABOVE: emboss

# install bwa - bundled

# install minimap2
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 && \
  tar -xvf minimap2-2.17_x64-linux.tar.bz2 && \
  rm minimap2-2.17_x64-linux.tar.bz2

# install samtools - bundled

# install bedtools 2.29.0 since >=2.27.0 is required for barrnap and the apt-get package is 2.25.0
# dependencies required for bedtools: zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
  tar -zxf bedtools-2.29.0.tar.gz && \
  rm bedtools-2.29.0.tar.gz && \
  cd bedtools2 && \
  make

# bcftools - bundled

# freebayes - bundled (hopefully all of the three things listed on snippy github)

# vcflib - bundled

# install vt - libcurl3 needed for this?
RUN wget https://github.com/atks/vt/archive/0.57721.tar.gz &&\
  tar -xzf 0.57721.tar.gz && \
  rm 0.57721.tar.gz && \
  cd vt-0.57721 && \
  make && \
  make test

# install SnpEff - unzip needed
RUN wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip && \
  unzip snpEff_latest_core.zip

# get Seqtk
RUN mkdir seqtk &&\ 
  cd seqtk &&\
  wget https://github.com/lh3/seqtk/archive/v1.3.tar.gz &&\
  tar -zxf v1.3.tar.gz &&\
  rm v1.3.tar.gz &&\
  cd seqtk-1.3/ &&\
  make &&\
  make install

# Samclip
RUN mkdir samclip &&\
  cd samclip &&\
  wget https://raw.githubusercontent.com/tseemann/samclip/master/samclip &&\
  chmod +x samclip

#get Snippy itself
RUN wget https://github.com/tseemann/snippy/archive/v4.4.5.tar.gz &&\
  tar -zxf v4.4.5.tar.gz &&\
  rm v4.4.5.tar.gz &&\
  cd snippy-4.4.5

ENV PATH="/bedtools2/bin:\
/minimap2-2.17_x64-linux:\
/vt-0.57721/:\
/snpEff/scripts:\
/samclip:\
/snippy-4.4.5/bin:\
/snippy-4.4.5/binaries/linux:\
${PATH}"

# set perl locale settings for singularity compatibility
ENV LC_ALL=C

WORKDIR /data

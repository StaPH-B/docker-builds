FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.1.0"
LABEL software="Prokka"
LABEL software.version="1.14.0"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
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
 make && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install bedtools 2.29.0 since >=2.27.0 is required for barrnap and the apt-get package is 2.25.0
# dependencies required for bedtools: zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.29.0/bedtools-2.29.0.tar.gz && \
  tar -zxf bedtools-2.29.0.tar.gz && \
  rm bedtools-2.29.0.tar.gz && \
  cd bedtools2 && \
  make

# add bedtools to PATH for barrnap test
ENV PATH="$PATH:/bedtools2/bin"

# install barrnap
RUN wget https://github.com/tseemann/barrnap/archive/0.9.tar.gz && \
    tar -zxf 0.9.tar.gz && \
    rm 0.9.tar.gz && \
    cd barrnap-0.9 && \
    make test

RUN wget https://github.com/tseemann/prokka/archive/v1.14.0.tar.gz && \
    tar -xzf v1.14.0.tar.gz && \
    rm -rf v1.14.0.tar.gz && \
    mkdir /data

# install tbl2asn manually since the one included with prokka is expired.
# Probably will have to do again in Jan 2021 unless Torsten removes it from prokka
RUN wget ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux64.tbl2asn.gz -O linux64.tbl2asn.gz && \
    gunzip linux64.tbl2asn.gz && \
    mv linux64.tbl2asn /usr/bin/tbl2asn && \
    chmod 755 /usr/bin/tbl2asn

# set PATH to prioritize /usr/bin/tbl2asn before /prokka-[VERSION]/binaries/*/tbl2asn
ENV PATH="$PATH:/prokka-1.14.0/bin:\
/barrnap-0.9/bin"

# set perl locale settings so barrnap works in singularity image
ENV LC_ALL=C

RUN prokka --setupdb && prokka --listdb
WORKDIR /data

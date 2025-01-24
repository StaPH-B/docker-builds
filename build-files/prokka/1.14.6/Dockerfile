# setting these ARGs as global variables, so they persist across all build layers (but not in final production image)
ARG PROKKA_VER="1.14.6"
ARG BEDTOOLS_VER="2.29.0"
ARG BARRNAP_VER="0.9"
ARG BLAST_VER="2.9.0"

FROM ubuntu:bionic as app

# re-instantiating for the app build layer
ARG PROKKA_VER
ARG BEDTOOLS_VER
ARG BARRNAP_VER
ARG BLAST_VER

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Prokka"
LABEL software.version="${PROKKA_VER}"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# so that apt/tzdata doesn't ask for user input for a timezone
ARG DEBIAN_FRONTEND="noninteractive"

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
 cpanminus \
 make \
 libidn11 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install bedtools 2.29.0 since >=2.27.0 is required for barrnap and the apt-get package is 2.25.0
# dependencies required for bedtools: zlib1g-dev python liblzma-dev libbz2-dev xz-utils curl g++
RUN wget https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VER}/bedtools-${BEDTOOLS_VER}.tar.gz && \
  tar -zxf bedtools-${BEDTOOLS_VER}.tar.gz && \
  rm bedtools-${BEDTOOLS_VER}.tar.gz && \
  cd bedtools2 && \
  make

# add bedtools to PATH for barrnap test
ENV PATH="$PATH:/bedtools2/bin"

# install barrnap
RUN wget https://github.com/tseemann/barrnap/archive/${BARRNAP_VER}.tar.gz && \
    tar -zxf ${BARRNAP_VER}.tar.gz && \
    rm ${BARRNAP_VER}.tar.gz && \
    cd barrnap-${BARRNAP_VER} && \
    make test

# to fix error when running Prokka 1.14.5: '"uniq" is not exported by the List::Util module'
# error introduced while updating dockerfile from prokka 1.14.0 to 1.14.5
RUN cpanm List::Util

# download prokka and make /data
RUN wget https://github.com/tseemann/prokka/archive/v${PROKKA_VER}.tar.gz && \
    tar -xzf v${PROKKA_VER}.tar.gz && \
    rm -rf v${PROKKA_VER}.tar.gz && \
    mkdir /data

# install tbl2asn manually since the one included with prokka is expired. 
# Probably will have to do again in Dec 2021 unless Torsten removes it from prokka
RUN wget ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/converters/by_program/tbl2asn/linux64.tbl2asn.gz -O linux64.tbl2asn.gz && \
    gunzip linux64.tbl2asn.gz && \
    mv linux64.tbl2asn /usr/bin/tbl2asn && \
    chmod 755 /usr/bin/tbl2asn

# install blast binaries directly from NCBI FTP; prioritize this over the blast binaries included with prokka
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz

# set PATH to prioritize /usr/bin/tbl2asn (and other paths like ncbi-blast+) before /prokka-[VERSION]/binaries*/tbl2asn
# second line added so that parallel is forced into PATH (wasn't working in Singularity without explicitly setting this)
# set perl locale settings so barrnap works in singularity image
ENV PATH="${PATH}:/ncbi-blast-${BLAST_VER}+/bin/:\
/prokka-${PROKKA_VER}/bin:\
/prokka-${PROKKA_VER}/binaries/common:\
/prokka-${PROKKA_VER}/binaries/linux:\
/barrnap-${BARRNAP_VER}/bin"\
 LC_ALL=C

# index dbs and list what dbs were setup; set working dir to /data
RUN prokka --setupdb && prokka --listdb

WORKDIR /data

FROM app as test

# re-instantiating for the test layer
ARG PROKKA_VER

WORKDIR /prokka-${PROKKA_VER}

# run tests from https://github.com/tseemann/prokka/blob/master/.travis.yml
RUN realpath . && prokka --version && \
 prokka --help && \
 ! prokka --doesnotexist && \
 prokka --depends && \
 prokka --setupdb && \
 prokka --listdb && \
 prokka --cpus 2 --outdir asm --prefix asm test/plasmid.fna && \
 grep '>' asm/asm.fna && \
 prokka --cleandb
 
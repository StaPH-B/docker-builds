FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during image build time
ARG mashtreeVer="1.2.0"
ARG mashVer="2.2"
ARG quicktreeVer="2.5"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="mashtree"
LABEL software.version="1.2.0"
LABEL description="Create a tree using Mash distances"
LABEL website="https://github.com/lskatz/mashtree"
LABEL license="https://github.com/lskatz/mashtree/blob/master/LICENSE"
LABEL maintainer1="Abigail Shockey"
LABEL maintainer1.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
 perl \
 build-essential \
 sqlite3 \
 libsqlite3-dev \
 libjson-perl \
 make \
 wget \
 cpanminus \
 libexpat1-dev \
 liblwp-protocol-https-perl \
 libnet-ssleay-perl && \
 apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install perl modules
RUN cpanm --force --notest BioPerl \
 Bio::Perl \
 Bio::DB::GenBank \
 LWP::Protocol::https \
 IO::Socket::SSL \
 Bio::Sketch::Mash \
 Bio::Kmer \
 DBD::SQLite \
 DBI \
 File::Which

# install mash
RUN wget https://github.com/marbl/Mash/releases/download/v${mashVer}/mash-Linux64-v${mashVer}.tar && \
  tar -xf mash-Linux64-v${mashVer}.tar && \
  rm -rf mash-Linux64-v${mashVer}.tar

# install quicktree
RUN wget https://github.com/khowe/quicktree/archive/v${quicktreeVer}.tar.gz && \
  tar -xzf v${quicktreeVer}.tar.gz && \
  rm -rf v${quicktreeVer}.tar.gz && \
  cd quicktree-${quicktreeVer} && \
  make quicktree

# add mash and quicktree to the path to allow mashtree to pass tests
ENV PATH="${PATH}:/mash-Linux64-v${mashVer}:\
/quicktree-${quicktreeVer}"

# install mashtree
RUN wget https://github.com/lskatz/mashtree/archive/v${mashtreeVer}.tar.gz && \
  tar -xzf v${mashtreeVer}.tar.gz && \
  rm -rf v${mashtreeVer}.tar.gz && \
  cd mashtree-${mashtreeVer}/ && \
  perl Makefile.PL && \
  mkdir /data

# set PATH to include mashtree. LC_ALL for singularity compatibility
ENV PATH="${PATH}:/mashtree-${mashtreeVer}/bin"\
 LC_ALL=C

WORKDIR /data

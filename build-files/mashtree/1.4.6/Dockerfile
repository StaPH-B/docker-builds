FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during image build time
ARG mashtreeVer="1.4.6"
ARG mashVer="2.3"
ARG quicktreeVer="2.5"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="mashtree"
LABEL software.version="${mashtreeVer}"
LABEL description="Create a tree using Mash distances"
LABEL website="https://github.com/lskatz/mashtree"
LABEL license="https://github.com/lskatz/mashtree/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
LABEL maintainer3="Muhammad yasir Nawaz"
LABEL maintainer3.email="nawazm@michigan.gov"

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
  rm -rf mash-Linux64-v${mashVer}.tar && \
  chown root:root /mash-Linux64-v${mashVer}/*

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

CMD mashtree --help

####################################
########### test stage #############
####################################

# getting a fasta file with datasets
FROM staphb/ncbi-datasets:14.3.0 as fasta

WORKDIR /fasta_test

RUN datasets download genome accession GCA_007765495.1,GCF_000006945.2,GCF_016028495.1 --filename datasets.zip && \
    unzip datasets.zip 

FROM app as test

WORKDIR /test

COPY --from=fasta /fasta_test/ncbi_dataset/data/*/*.fna . 

RUN mashtree *.fna > tree.dnd
RUN mashtree --help

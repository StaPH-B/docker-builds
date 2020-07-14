FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL container.version="1"
LABEL software="Augur"
LABEL software.version="9.0.0"
LABEL description="Pipeline components for real-time phylodynamic analysis"
LABEL website="https://github.com/nextstrain/augur"
LABEL license="https://github.com/nextstrain/augur/blob/master/LICENSE.txt"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Jake Garfin"
LABEL maintainer2.email="jake.garfin@state.mn.us"

RUN apt-get update && apt-get install -y python3 \
  wget\
  python3-pip\
  iqtree=1.6.1+dfsg-1\
  build-essential\
  zlib1g-dev\
  pkg-config\
  mafft=7.310-1\
  locales

RUN wget https://github.com/vcftools/vcftools/releases/download/v0.1.16/vcftools-0.1.16.tar.gz &&\
  tar -xzf vcftools-0.1.16.tar.gz &&\
  rm vcftools-0.1.16.tar.gz &&\
  cd vcftools-0.1.16 &&\
  ./configure &&\
  make && make install &&\
  mkdir /data

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  locale-gen


ENV LC_ALL=en_US.UTF-8


RUN pip3 install nextstrain-augur==9.0.0 snakemake

WORKDIR /data

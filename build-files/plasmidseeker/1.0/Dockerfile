FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="PlasmidSeeker"
LABEL software.version="1.0"
LABEL description="A k-mer based program for the identification of known plasmids from bacterial whole genome sequencing reads"
LABEL website="https://github.com/bioinfo-ut/PlasmidSeeker"
LABEL license="https://github.com/bioinfo-ut/PlasmidSeeker/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install perl and git
RUN apt-get update && apt-get -y install \
  wget \
  bzip2 \
  gzip \
  perl \
  git \
  r-base-core \
  r-base \
  r-base-dev \
  libclang-dev && apt-get clean

RUN git clone https://github.com/bioinfo-ut/PlasmidSeeker.git

RUN chmod -R 777 PlasmidSeeker/

ENV PATH="${PATH}:/PlasmidSeeker:/PlasmidSeeker/GenomeTester4"

ENV LC_ALL=C

FROM ubuntu:jammy as app

ARG DATASETS_VER="16.10.3"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="NCBI's datasets and dataformat"
LABEL software.version="${DATASETS_VER}"
LABEL description="Downloads biological sequence data from NCBI"
LABEL website="https://github.com/ncbi/datasets"
LABEL documentation="https://www.ncbi.nlm.nih.gov/datasets/docs/v1/"
LABEL license="https://github.com/ncbi/datasets/blob/master/pkgs/ncbi-datasets-cli/LICENSE.md"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# unzip isn't needed for datasets/dataformat, but it is often used after downloading files with datasets
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  ca-certificates \
  unzip && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

# install ncbi datasets tool (pre-compiled binary)
RUN wget https://github.com/ncbi/datasets/releases/download/v${DATASETS_VER}/linux-amd64.cli.package.zip && \
  unzip linux-amd64.cli.package.zip && \
  rm linux-amd64.cli.package.zip && \
  chmod +x dataformat datasets

ENV LC_ALL=C

WORKDIR /data

# datasets is generally datasets <subcommand> --help, but just typing in 'datasets' should bring up a help menu
CMD [ "datasets", "--help" ]

FROM app as test

RUN dataformat --help && datasets --help

# stolen from Curtis at https://github.com/StaPH-B/docker-builds/blob/master/pangolin/4.1.2/Dockerfile
RUN datasets download virus genome accession ON924087.1 --filename ON924087.1.zip && \
  unzip ON924087.1.zip && \
  rm ON924087.1.zip && \
  cp ncbi_dataset/data/genomic.fna ON924087.1.fna && \
  wc -c ON924087.1.fna

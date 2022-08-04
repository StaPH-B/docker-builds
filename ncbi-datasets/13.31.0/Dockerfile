FROM ubuntu:focal as app

# As of 2022-08-04, there's not a way to specify a version for datasets at https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/
# They have a github repo at https://github.com/ncbi/datasets
ARG DATASETS_VER="13.31.0"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="NCBI's datasets and dataformat"
LABEL software.version="${DATASETS_VER}"
LABEL description="Downloads biological sequence data from NCBI"
LABEL website="https://www.ncbi.nlm.nih.gov/datasets/docs/v1/"
# Currently doesn't have a license, but it's likely public domain
LABEL license="https://github.com/ncbi/datasets"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# unzip isn't needed for datasets/dataformat, but it is often used after downloading files with datasets
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 unzip \
 ca-certificates \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

# install ncbi datasets tool (pre-compiled binary)
RUN wget https://github.com/ncbi/datasets/releases/download/v${DATASETS_VER}/linux-amd64.cli.package.zip && \
  unzip linux-amd64.cli.package.zip && \
  rm linux-amd64.cli.package.zip && \
  chmod +x dataformat datasets

ENV LC_ALL=C

WORKDIR /data

FROM app as pretest

RUN dataformat --help && datasets --help

RUN datasets download virus genome accession ON924087.1 --filename ON924087.1.zip && \
  unzip ON924087.1.zip && \
  rm ON924087.1.zip && \
  cp ncbi_dataset/data/genomic.fna ON924087.1.fna

FROM staphb/pangolin:4.1.2-pdata-1.12 as test

COPY --from=pangolin /opt/conda/envs/pangolin/bin /pangolin

RUN /pangolin/pangolin ON924087.1.fna && cat lineage_report.csv

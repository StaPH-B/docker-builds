FROM ubuntu:jammy as app

# version doesn't show appear anywhere on ftp; only can be determined via command-line
# this docker image was built 2022-12-13 and this was the current version
ARG TABLE2ASN_VER="1.26.678"
ARG TABLE2ASN_RELEASE_DATE="2022-06-14"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="NCBI's table2asn"
LABEL software.version="${TABLE2ASN_VER}"
LABEL description="Converts files of various formats to ASN.1"
LABEL website="https://www.ncbi.nlm.nih.gov/genbank/table2asn/"
LABEL license="unknown"
LABEL maintainer="Sage Wright"
LABEL maintainer.email="sage.wright@theiagen.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 gzip && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

# install ncbi table2asn tool (pre-compiled binary)
RUN wget https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${TABLE2ASN_RELEASE_DATE}/by_program/table2asn/linux64.table2asn.gz && \
  gunzip linux64.table2asn.gz && \
  mv linux64.table2asn table2asn && \
  chmod +x table2asn

ENV LC_ALL=C

WORKDIR /data

FROM app as test

RUN table2asn -help && table2asn -version

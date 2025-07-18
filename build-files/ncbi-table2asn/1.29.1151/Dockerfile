ARG RELEASE_DATE="2025-03-03"

FROM ubuntu:jammy AS app

# version doesn't show appear anywhere on ftp; only can be determined via command-line
# this docker image was built 2022-12-13 and this was the current version
ARG TABLE2ASN_VER="1.29.1151"
ARG RELEASE_DATE

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
  gzip \
  libidn12 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
  ln -s /usr/lib/x86_64-linux-gnu/libidn.so.12 /usr/lib/x86_64-linux-gnu/libidn.so.11

WORKDIR /usr/local/bin

ENV STAPHB_TOOLS="agp_validate \
  asn2all \
  asn2asn \
  asn2fasta \
  asn2flat \
  asn2fsa \
  asn2gb \
  asn2idx \
  asn2xml \
  asndisc \
  asnmacro \
  asnval \
  asnvalidate \
  gap_stats \
  gene2xml \
  insdseqget \
  sbtedit \
  sqn2agp \
  srcchk \
  table2asn "

RUN for tool in ${STAPHB_TOOLS} ; do \
  echo "Downloading ${tool}" && \
  wget -q https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${RELEASE_DATE}/by_program/${tool}/linux64.${tool}.gz && \
  gunzip linux64.${tool}.gz && \
  mv linux64.${tool} ${tool} && \
  chmod +x ${tool} ; done

ENV LC_ALL=C

CMD ["table2asn", "-help"]

WORKDIR /data

FROM app AS test

ARG RELEASE_DATE

# NOTE: Not all of these tools support the '-help' or '-version flag'
# This ensures that all tools are in $PATH and executable
RUN for tool in ${STAPHB_TOOLS} ; do echo "Checking ${tool}" && ${tool} -help && ${tool} -version ; done

WORKDIR /test

RUN wget https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${RELEASE_DATE}/documentation/short.fsa && \
  wget https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${RELEASE_DATE}/documentation/SubmissionTemplate.sbt && \
  table2asn -i short.fsa  && \
  table2asn -t SubmissionTemplate.sbt -i short.fsa -o helicase.sqn

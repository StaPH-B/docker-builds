FROM ubuntu:jammy as app

# version doesn't show appear anywhere on ftp; only can be determined via command-line
# this docker image was built 2022-12-13 and this was the current version
ARG TABLE2ASN_VER="1.28.943"
ARG RELEASE_DATE="2023-10-05"

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

ENV STAPHB_TOOLS="agp_validate asn2all asn2asn asn2fasta asn2flat asn2fsa asn2gb asn2idx asn2xml asndisc asnmacro asnval asnvalidate gap_stats gene2xml insdseqget sqn2agp srcchk table2asn"

RUN for tool in ${STAPHB_TOOLS} ; do \
  wget -q https://ftp.ncbi.nlm.nih.gov/asn1-converters/versions/${RELEASE_DATE}/by_program/${tool}/linux64.${tool}.gz ; \
  gunzip linux64.${tool}.gz && \
  mv linux64.${tool} ${tool} && \
  chmod +x ${tool} ; done

ENV LC_ALL=C

CMD for tool in ${STAPHB_TOOLS} ; do ${tool} -help ; done

WORKDIR /data

FROM app as test

RUN for tool in ${STAPHB_TOOLS} ; do ${tool} -help ; ${tool} -version ; done

FROM python:3.9.17-slim AS app

USER root
WORKDIR /

ARG POD5_TOOLS_VERSION="0.3.36"

LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="pod5"
LABEL software.version="${POD5_TOOLS_VERSION}"
LABEL description="This software provides a Python module for reading and writing POD5 data."
LABEL website="https://github.com/nanoporetech/pod5-file-format"
LABEL license="https://github.com/nanoporetech/pod5-file-format/blob/master/LICENSE.md"
LABEL maintainer="Sage Wright"
LABEL maintainer.email="sagemwright@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Preferred/Correct code to install the new version
#RUN pip3 install --no-cache --break-system-packages pod5==${POD5_TOOLS_VERSION}

# Hardcode version to allow the download of 0.3.36 specific pod5 version
RUN pip3 install --no-cache git+https://github.com/nanoporetech/pod5-file-format.git@v0.3.36

WORKDIR /data

CMD [ "pod5", "--help" ]

FROM app AS test

WORKDIR /test

RUN pod5 --help && \
    pod5 --version

RUN wget https://github.com/nanoporetech/dorado/raw/release-v0.7/tests/data/pod5/dna_r10.4.1_e8.2_260bps/dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5

RUN pod5 view . --include "read_id, channel" --output summary.tsv && \
    pod5 subset . --summary summary.tsv --columns channel

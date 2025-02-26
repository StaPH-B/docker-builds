FROM ubuntu:focal as app

ARG MLST_VER="2.23.0"
ARG ANY2FASTA_VER="0.4.2"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="mlst"
LABEL software.version="${MLST_VER}"
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL website="https://github.com/tseemann/mlst"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"

# install dependencies via apt; cleanup apt garbage
# blast from ubuntu:focal is v2.9.0 (as of 2022-05-09)
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 gzip \
 file \
 ncbi-blast+ && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get any2fasta; move binary to /usr/local/bin which is already in $PATH
RUN wget https://github.com/tseemann/any2fasta/archive/refs/tags/v${ANY2FASTA_VER}.tar.gz && \
 tar xzf v${ANY2FASTA_VER}.tar.gz && \
 rm v${ANY2FASTA_VER}.tar.gz && \
 chmod +x any2fasta-${ANY2FASTA_VER}/any2fasta && \
 mv -v any2fasta-${ANY2FASTA_VER}/any2fasta /usr/local/bin

# get mlst
RUN wget https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz && \
 tar -xzf v${MLST_VER}.tar.gz && \
 rm v${MLST_VER}.tar.gz

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:" \
    LC_ALL=C.UTF-8

# check dependencies and list available schemes
RUN mlst --check && mlst --list

WORKDIR /data

FROM app as test

# copy in test script; run script
# test commands stolen shamelessly from https://github.com/tseemann/mlst/blob/master/.travis.yml
COPY mlst-tests.sh .
RUN bash mlst-tests.sh

### Example command to run mlst (broken into two lines for readability)
### If you have an assembly named contigs.fasta in your PWD:
# $ docker run -v ${PWD}:/data staphb/mlst:latest \
#   mlst contigs.fasta >mlst-results.tsv
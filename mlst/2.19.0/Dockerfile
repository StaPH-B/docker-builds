ARG MLST_VER="2.19.0"

FROM ubuntu:bionic as app
ARG MLST_VER

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL software="mlst"
LABEL software.version=$MLST_VER
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL website="https://github.com/tseemann/mlst"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Sarah Nadeau"
LABEL maintainer2.email="sarah.nadeau@bsse.ethz.ch"

RUN apt-get update && apt-get install -y wget \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 gzip \
 file

# get blast 2.9 binaries. Had to remove 'LATEST' from url since 2.10 is out
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.9.0/ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 rm ncbi-blast-2.9.0+-x64-linux.tar.gz

# get any2fasta
RUN cd /usr/local/bin && \
  wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
  chmod +x any2fasta

# get mlst
RUN wget https://github.com/tseemann/mlst/archive/v$MLST_VER.tar.gz &&\
 tar -xzf v$MLST_VER.tar.gz &&\
 rm v$MLST_VER.tar.gz

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-$MLST_VER/bin:\
/ncbi-blast-2.9.0+/bin" \
    LC_ALL=C

# check dependencies and list available schemes
RUN mlst --check && mlst --list

WORKDIR /data

FROM app as test
ARG MLST_VER

# Run test script
COPY test.sh .
RUN bash test.sh $MLST_VER

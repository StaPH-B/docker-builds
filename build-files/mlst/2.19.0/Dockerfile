FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL container.version="1"
LABEL software="mlst"
LABEL software.version="2.19.0"
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL website="https://github.com/tseemann/mlst"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

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
RUN wget https://github.com/tseemann/mlst/archive/v2.19.0.tar.gz &&\
 tar -xzf v2.19.0.tar.gz &&\
 rm v2.19.0.tar.gz

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-2.19.0/bin:\
/ncbi-blast-2.9.0+/bin" \
    LC_ALL=C

# check dependencies and list available schemes
RUN mlst --check && mlst --list

WORKDIR /data

### Example command to run mlst (broken into two lines for readability)
### If you have an assembly named contigs.fasta in your PWD:
# $ docker run -v ${PWD}:/data staphb/mlst:2.19.0 \
#   mlst contigs.fasta >mlst-results.tsv

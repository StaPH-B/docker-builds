FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="mlst"
LABEL software.version="2.16.2"
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL website="https://github.com/tseemann/mlst"
LABEL lisence="https://github.com/tseemann/mlst/blob/master/LICENSE"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y wget \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 ncbi-blast+ \
 gzip \
 file

RUN wget https://github.com/tseemann/mlst/archive/v2.16.2.tar.gz &&\
 tar -xzf v2.16.2.tar.gz &&\
 rm v2.16.2.tar.gz

ENV PATH=${PATH}:/mlst-2.16.2/bin

# check dependencies and list available schemes
RUN mlst --check && mlst --list

WORKDIR /data

### Example command to run mlst (broken into two lines for readability)
### If you have an assembly named contigs.fasta in your PWD:
# $ docker run -v ${PWD}:/data staphb/mlst:2.16.2 \
#   mlst contigs.fasta >mlst-results.tsv

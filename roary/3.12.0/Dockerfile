FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Roary"
LABEL software.version="3.12.0"
LABEL description="Rapid large-scale prokaryotic pan genome analysis"
LABEL website="https://github.com/sanger-pathogens/Roary"
LABEL license="https://github.com/sanger-pathogens/Roary/blob/master/GPL-LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get install -y bedtools \
                     cd-hit \
                     ncbi-blast+ \
                     mcl \
                     parallel \
                     prank \
                     mafft \
                     fasttree \
                     make \
                     curl \
                     cpanminus \
                     libxml-parser-perl \
                     libperlio-utf8-strict-perl \
                     libmoose-perl \
                     libgraph-perl

RUN cpanm LWP::Simple \
      Text::CSV \
      JSON \
      File::Slurp

RUN cpanm --force AJPAGE/Bio-Roary-3.12.0.tar.gz && \
      mkdir /data && \
      mkdir /kraken_db

WORKDIR /data
# set perl locale settings
ENV LC_ALL=C

FROM ubuntu:focal as app

ARG EMBOSS_VERSION="6.4.0"

ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="EMBOSS"
LABEL software.version=$EMBOSS_VERSION
LABEL description=" EMBOSS is a free Open Source software analysis package specially developed for the needs of the molecular biology (e.g. EMBnet) user community. The software automatically copes with data in a variety of formats and even allows transparent retrieval of sequence data from the web."
LABEL website="http://emboss.sourceforge.net"
LABEL license="http://emboss.sourceforge.net/licence/"
LABEL maintainer="András Asbóth"
LABEL maintainer.email="sbthandras@gmail.com"

RUN apt-get update && apt-get install -y \
  locales \
  software-properties-common \
  build-essential \
  libx11-dev \
  wget \
  --no-install-recommends && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# set locale
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# EMBOSS
RUN wget ftp://emboss.open-bio.org/pub/EMBOSS/old/${EMBOSS_VERSION}/EMBOSS-${EMBOSS_VERSION}.tar.gz && \
	tar -xzf EMBOSS-${EMBOSS_VERSION}.tar.gz && \
	rm EMBOSS-${EMBOSS_VERSION}.tar.gz && \
	cd EMBOSS-${EMBOSS_VERSION} && \ 
	./configure && \
	make  
ENV PATH="/EMBOSS-${EMBOSS_VERSION}/emboss:${PATH}"

# Default working directory and command
WORKDIR /data
CMD ['water', '-help']


# test layer
FROM app as test

# test with Bacteriophage T2 tail fiber gene 36 and Bacteriophage Ox2 tail fiber gene 36
RUN wget "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=X01753.1&rettype=fasta" -O X01753.1.fa && \
    wget "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=X01755.1&rettype=fasta" -O X01755.1.fa

# Alignment
RUN water -asequence X01753.1.fa -bsequence X01755.1.fa -gapopen 10 -gapextend 0.5 -outfile alignment.water && \
    cat alignment.water


# Base Image
FROM ubuntu:xenial

# Metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SeqSero2"
LABEL software.version="1.0.0"
LABEL description="Salmonella serotyping from genome sequencing data"
LABEL website="https://github.com/denglab/SeqSero2"
LABEL license="https://github.com/denglab/SeqSero2/blob/master/LICENSE"

# Maintainer
MAINTAINER Jake Garfin <jake.garfin@state.mn.us>

RUN apt-get update && apt-get install -y \
  python3\
  python3-pip\
  bwa\
  ncbi-blast+\
  sra-toolkit\
  bedtools\
  wget\
  zlib1g-dev\
  libbz2-dev\
  liblzma-dev\
  build-essential\
  libncurses5-dev

RUN pip3 install biopython

# Install samtools (installing from apt breaks SeqSero2 version check)
RUN wget 'https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2' && \
  tar -xvf samtools-1.9.tar.bz2 && rm samtools-1.9.tar.bz2 && cd samtools-1.9 && make

# Install salmID
RUN wget https://github.com/hcdenbakker/SalmID/archive/0.122.tar.gz && \
  tar -xzf 0.122.tar.gz && rm -rf 0.122.tar.gz

# Install SPAdes
RUN wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz && \
  tar -xzf SPAdes-3.13.0-Linux.tar.gz && \
  rm -rf SPAdes-3.13.0-Linux.tar.gz

# Install SeqSero2
RUN wget https://github.com/denglab/SeqSero2/archive/v1.0.0.tar.gz && \
  tar -xzf v1.0.0.tar.gz && rm -rf v1.0.0.tar.gz && mkdir /data


ENV PATH="${PATH}:/SeqSero2-1.0.0:/SPAdes-3.13.0-Linux/bin:/SalmID-0.122:/samtools-1.9"

WORKDIR /data

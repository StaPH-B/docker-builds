FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Legsta"
LABEL software.version="0.5.1"
LABEL description="In silico Legionella pneumophila Sequence Based Typing (SBT)"
LABEL website="https://github.com/tseemann/legsta"
LABEL license="https://github.com/tseemann/legsta/blob/master/LICENSE"
LABEL maintainer1="Jake Garfin"
LABEL maintainer1.email="jake.garfin@state.mn.us"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y \
 cpanminus \
 build-essential \
 libc6-i386 \
 wget && \
 apt-get clean && apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# Install perl module
RUN cpanm Data::Dumper 

# get any2fasta
RUN cd /usr/local/bin && \
  wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
  chmod +x any2fasta

# Install Legsta
ENV legstaVer=0.5.1
RUN wget https://github.com/tseemann/legsta/archive/v${legstaVer}.tar.gz && \
 tar -xzf v${legstaVer}.tar.gz && \
 rm v${legstaVer}.tar.gz && \
 mkdir /data

# set PATH and locale settings for singularity compatibility
ENV PATH="${PATH}:/legsta-${legstaVer}/bin"\
 LC_ALL=C

WORKDIR /data

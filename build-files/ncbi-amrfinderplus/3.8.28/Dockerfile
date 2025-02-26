FROM ubuntu:bionic

# For easy upgrade later. ARG variables only persist during build time
ARG amrfinderVer="3.8.28"

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version="3.8.4"
LABEL description="NCBI resistance gene detection tool"
LABEL website="https://github.com/ncbi/amr"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies, clean up apt garbage
RUN apt-get update && apt-get install -y \
 wget \ 
 curl \
 make \
 g++ && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# ncbi-blast+ 2.10.0
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.0/ncbi-blast-2.10.0+-x64-linux.tar.gz && \
 tar zxf ncbi-blast-2.10.0+-x64-linux.tar.gz && \
 rm ncbi-blast-2.10.0+-x64-linux.tar.gz && \
 mkdir /data 

# hmmer 3.3 since amrfinder requires 3.2 or higher (apt version is 3.1)
# apt dependencies: make, g++
RUN wget http://eddylab.org/software/hmmer/hmmer-3.3.tar.gz && \
 tar xzf hmmer-3.3.tar.gz && \
 rm hmmer-3.3.tar.gz && \
 cd hmmer-3.3 && \
 ./configure && \
 make && \
 make install

# ncbi AMRFinderPlus
# apt dependencies: curl
RUN mkdir amrfinder && cd /amrfinder && \
 wget https://github.com/ncbi/amr/releases/download/amrfinder_v${amrfinderVer}/amrfinder_binaries_v${amrfinderVer}.tar.gz && \
 tar zxf amrfinder_binaries_v${amrfinderVer}.tar.gz && \
 rm amrfinder_binaries_v${amrfinderVer}.tar.gz

# set PATH and locale settings for singularity compatibiliity
ENV PATH="${PATH}:/ncbi-blast-2.10.0+/bin:\
/amrfinder"\
 LC_ALL=C

# download databases
RUN cd /amrfinder && amrfinder -u

WORKDIR /data

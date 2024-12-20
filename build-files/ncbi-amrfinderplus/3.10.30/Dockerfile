FROM ubuntu:jammy as app

# For easy upgrade later. ARG variables only persist during build time
ARG AMRFINDER_VER="3.10.30"

# now installed via APT; have to use ubuntu:jammy to get these later versions
#ARG BLAST_VER="2.12.0"
#ARG HMMER_VER="3.3.2"

# to prevent tzdata from asking for a region during apt updates; ARG so that variable only 
# persists at buildtime
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version="${AMRFINDER_VER}"
LABEL description="NCBI resistance gene detection tool"
LABEL website="https://github.com/ncbi/amr"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Anders Goncalves da Silva"
LABEL maintainer3.email="andersgs@gmail.com"

# install dependencies, clean up apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \ 
 curl \
 ca-certificates \
 ncbi-blast+ \
 hmmer && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# ncbi-blast+ installed via apt is v2.12.0
# hmmer installed via apt is v3.3.2

# install ncbi AMRFinderPlus binaries; make /data
# apt dependencies: curl
RUN mkdir amrfinder && cd /amrfinder && \
 wget https://github.com/ncbi/amr/releases/download/amrfinder_v${AMRFINDER_VER}/amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
 tar zxf amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
 rm amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
 mkdir /data

# set PATH and locale settings for singularity compatibiliity
ENV PATH="${PATH}:\
/amrfinder"\
 LC_ALL=C.UTF-8

# download databases
RUN cd /amrfinder && amrfinder -u

WORKDIR /data

# testing layer; following steps from here: https://github.com/ncbi/amr/wiki/Test-your-installation
FROM app as test

# print out version and database version
RUN amrfinder --version && amrfinder --database_version

# full combined protein and nucleotide search; compare outputs with diff and check for exit code of 0
RUN amrfinder --plus -n /amrfinder/test_dna.fa -p /amrfinder/test_prot.fa -g /amrfinder/test_prot.gff -O Escherichia >/amrfinder/test_both.got && \
 diff /amrfinder/test_both.expected /amrfinder/test_both.got && \
 echo "exit code for test:" $?


FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time
ARG KLEBORATE_VER="2.3.2"
ARG BLAST_VER="2.9.0"
ARG MASH_VER="2.3"
ARG KAPTIVE_VER="2.0.6"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Kleborate"
LABEL software.version="${KLEBORATE_VER}"
LABEL description="tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC)"
LABEL website="https://github.com/katholt/Kleborate"
LABEL license="https://github.com/katholt/Kleborate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Frank Ambrosio"
LABEL maintainer2.email="frank.ambrosio@theiagen.com"

# install prerequisites. Cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 python3 \
 python3-pip \
 python3-setuptools \
 wget \
 ca-certificates \
 bzip2 \
 locales \
 git \
 procps && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# to avoid encoding issues during kleborate setup.py install step
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8
ENV LANG=en_US.UTF-8

# so that we get a more recent version of biopython instead of what is available via apt
# trying to get rid of biopython warning "BiopythonExperimentalWarning: Bio.Align.substitution_matrices ......"
RUN python3 -m pip install biopython

# mash; update UID and GID of mash files; make /data
# UID and GID changes because the original owner is UID: 1081147385 and GID: 1360859114 which does NOT play well with systems that limits GIDs and UIDs
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
 tar -xvf mash-Linux64-v${MASH_VER}.tar && \
 rm -rf mash-Linux64-v${MASH_VER}.tar && \
 chown root:root /mash-Linux64-v${MASH_VER}/* && \
 mkdir /data

# ncbi-blast+
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz

# set PATH and TERM to avoid warnings
ENV PATH="/mash-Linux64-v${MASH_VER}:\
/ncbi-blast-${BLAST_VER}+/bin/:\
${PATH}" \
 TERM=xterm-256color

# kleborate install
# as per author instructions. Have to use git clone and git checkout since kaptive is a git submodule. cannot use tarballs
RUN git clone --recursive https://github.com/katholt/Kleborate.git && \
 cd Kleborate && \
 git checkout v${KLEBORATE_VER} && \
 cd kaptive && \
 git pull https://github.com/katholt/Kaptive v${KAPTIVE_VER} && \
 cd ../ && \
 python3 setup.py install

# set working directory
WORKDIR /data

FROM app as test

# run Kleborate on assembly supplied with Kleborate code
RUN kleborate --resistance --kaptive --all \
        --assemblies /Kleborate/test/test_genomes/172.fasta.gz \
        --outfile /data/strain172-kleborate-test-out.tsv

# install pytest; run unit tests included with Kleborate
RUN apt-get update && apt-get install -y --no-install-recommends python3-pytest && \
 cd /Kleborate && \
 python3 -m pytest

# print help and version info
RUN kleborate --help && kleborate --version
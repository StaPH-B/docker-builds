# Use ubuntu as base image
FROM ubuntu:focal as app

ARG DATASETS_SARS_COV_2_VER="0.7.2"

# metadata
LABEL base.image="ubuntu:focal"
LABEL software="datasets-sars-cov-2"
LABEL software.version="v0.7.2"
LABEL dockerfile.version="1"
LABEL description="Benchmark datasets for WGS analysis of SARS-CoV-2."
LABEL website="https://github.com/CDCgov/datasets-sars-cov-2"
LABEL license="https://github.com/CDCgov/datasets-sars-cov-2/blob/master/LICENSE"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install dependencies
ARG TZ=Etc/UTC
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
 wget\
 build-essential\
 libxml2\
 libmagic-dev\
 libhdf5-dev\
 git\
 openjdk-8-jdk\
 software-properties-common\
 lsb-release\
 apt-transport-https\
 ca-certificates\
 doxygen\
 uuid-runtime && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

# install latest cmake
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null && \
 apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main" && \
 apt-get update && apt-get install -y cmake

# get NCBI SRA Tools
RUN mkdir /ncbi && cd /ncbi && \
 git clone https://github.com/ncbi/sra-tools.git && \
 git clone https://github.com/ncbi/ngs.git && \
 git clone https://github.com/ncbi/ncbi-vdb.git

RUN cd /ncbi/ncbi-vdb && ./configure && \
 make && \
 make install

RUN cd /ncbi/ngs && ./configure && \
 make -C ngs-sdk && \
 make -C ngs-sdk install && \
 make -C ngs-java && \
 make -C ngs-java install && \
 make -C ngs-python

RUN cd /ncbi/sra-tools && ./configure && \
 make && \
 make install

# install edirect
RUN mkdir /edirect && \
    perl -MNet::FTP -e '$ftp = new Net::FTP("ftp.ncbi.nlm.nih.gov", Passive => 1);$ftp->login; $ftp->binary;$ftp->get("/entrez/entrezdirect/edirect.tar.gz");' && \
    gunzip -c edirect.tar.gz | tar xf - && \
    rm edirect.tar.gz

# install missing xtract executable required by efetch
RUN wget https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/xtract.Linux.gz && \
 gunzip -f xtract.Linux.gz && \
 mv -v xtract.Linux /usr/local/bin/xtract && \
 chmod +x /usr/local/bin/xtract

# vdb-config workaround: https://github.com/ncbi/sra-tools/issues/291
RUN mkdir /home/user/ /home/user/.ncbi/ && printf '/LIBS/GUID = "%s"\n' `uuidgen` > /home/user/.ncbi/user-settings.mkfg

# get datasets-sars-cov-2
RUN cd /home/user/ && git clone --depth 1 --branch v${DATASETS_SARS_COV_2_VER} https://github.com/CDCgov/datasets-sars-cov-2.git

ENV HOME /home/user/

ENV PATH=$PATH:/edirect:/usr/local/ncbi/sra-tools/bin:/home/user/datasets-sars-cov-2/scripts \
 TERM=xterm-256color

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

FROM app as test

# can add your own NCBI_API_KEY to allow more requests to go through (only use for local building, do not commit with actual API key)
#ENV NCBI_API_KEY=""

# download the smallest data set as a test
RUN GenFSGopher.pl -o vocvoi-output /home/user/datasets-sars-cov-2/datasets/sars-cov-2-voivoc.tsv --numcpus 2 --layout onedir --compressed

# delete smallest dataset to save space
RUN rm -rf vocvoi-output/

# download a dataset that includes reads and assemblies
RUN GenFSGopher.pl -o SNF-A-output /home/user/datasets-sars-cov-2/datasets/sars-cov-2-SNF-A.tsv --numcpus 2 --layout onedir --compressed
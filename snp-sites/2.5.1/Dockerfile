# Use ubuntu as base image
FROM ubuntu:hirsute

# metadata
LABEL base.image="ubuntu:hirsute"
LABEL dockerfile.version="1"
LABEL software="snp-sites"
LABEL software.version="2.5.1"
LABEL description="Finds SNP sites from a multi-FASTA alignment files"
LABEL website="https://github.com/sanger-pathogens/snp-sites"
LABEL license="https://github.com/sanger-pathogens/snp-sites/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install snp-sites; cleanup apt garbage; make /data 
# snp-sites installed via apt-get for ubuntu:hirsute downloads version 2.5.1 (Oct 2019 release)
RUN apt-get update && apt-get install -y \
 snp-sites && \
 apt-get auto-clean && \
 rm -rf /var/lib/apt/lists/* && \
 mkdir -v /data

# set working directory
WORKDIR /data

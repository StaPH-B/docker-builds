# Use ubuntu as base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="snp-sites"
LABEL software.version="2.3.3"
LABEL description="Finds SNP sites from a multi-FASTA alignment files"
LABEL website="https://github.com/sanger-pathogens/snp-sites"
LABEL license="https://github.com/sanger-pathogens/snp-sites/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

RUN apt-get update && apt-get install -y \
    snp-sites

RUN mkdir /data
WORKDIR /data

# Use ubuntu as base image
FROM ubuntu:noble AS app

ARG SNP_SITES_VERSION=2.5.1

# metadata
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="snp-sites"
LABEL software.version="${SNP_SITES_VERSION}"
LABEL description="Finds SNP sites from a multi-FASTA alignment files"
LABEL website="https://github.com/sanger-pathogens/snp-sites"
LABEL license="https://github.com/sanger-pathogens/snp-sites/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install snp-sites; cleanup apt garbage; make /data 
# snp-sites installed via apt-get for ubuntu:noble downloads version 2.5.1 (Oct 2019 release)
RUN apt-get update && apt-get install -y --no-install-recommends \
snp-sites && \
apt-get auto-clean && \
rm -rf /var/lib/apt/lists/* && \
mkdir -v /data

# set working directory
WORKDIR /data

CMD [ "snp-sites", "--help" ]

# test stage
FROM app AS test 

# run test; check output files for expected strings
RUN echo -e ">sample1\nAGACACAGTCAC\n>sample1\nAGACAC----AC\n>sample1\nAAACGCATTCAN" > test.fasta && \
snp-sites test.fasta -o test.aln -m -p -v && \
ls -lha && \
grep 'GA-' test.aln.snp_sites.aln && \
grep '*,T' test.aln.vcf && \
grep 'AGT' test.aln.phylip

# print help options and version
RUN snp-sites -h && \
snp-sites -V
FROM ubuntu:jammy AS app

ARG STXTYPER_VER="1.0.24"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="stxtyper"
LABEL software.version="${STXTYPER_VER}"
LABEL description="Search for Shiga toxin genes within bacterial genome assemblies"
LABEL website="https://github.com/ncbi/stxtyper"
LABEL license="https://github.com/ncbi/stxtyper/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies via apt; cleanup apt garbage
# blast from ubuntu:jammy is v2.12.0 (as of 2024-09-06)
# procps is for ps command (required for nextflow)
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 ncbi-blast+ \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download pre-compiled binary
RUN mkdir /stxtyper && \ 
wget -q https://github.com/ncbi/stxtyper/releases/download/v${STXTYPER_VER}/stxtyper_v${STXTYPER_VER}_x86_64_Linux.tar.gz && \
tar -xzf stxtyper_v${STXTYPER_VER}_x86_64_Linux.tar.gz --strip-components=1 -C /stxtyper && \
rm -r stxtyper_v${STXTYPER_VER}_x86_64_Linux.tar.gz && \
ls -lh /stxtyper

# set PATH to include where stxtyper & fasta_check executables exist
ENV PATH="${PATH}:/stxtyper" \
TERM=xterm-256color 

# set final working directory as /data for passing data in/out of container
WORKDIR /data

FROM app AS test

# print version and help options & run the supplied tests
RUN tblastn -version && \
stxtyper --version && \
stxtyper --help && \
cd /stxtyper && \
bash test_stxtyper.sh

# download genome from NCBI and test stxtyper with it
# expect 1 perfect match to stx2o subtype, with COMPLETE operon designation
# https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_012224845.2/
# grep below requires both strings to be present in the same line
RUN echo "downloading test genome & running through stxtyper..." && \
wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
stxtyper -n GCA_012224845.2_ASM1222484v2_genomic.fna.gz | tee test-result.tsv && \
grep 'stx2o' test-result.tsv | grep 'COMPLETE'

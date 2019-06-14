FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="SKESA"
LABEL software.version="2.3.0"
LABEL description="Strategic Kmer Extension for Scrupulous Assemblies"
LABEL website="https://github.com/ncbi/SKESA"
LABEL lisence="https://github.com/ncbi/SKESA/blob/master/LICENSE"

MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

RUN apt-get update && apt-get install -y wget

# get skesa binary, rename it as skesa
RUN mkdir skesa &&\
  cd skesa &&\
  wget https://github.com/ncbi/SKESA/releases/download/v2.3.0/skesa.centos6.10 &&\
  mv skesa.centos6.10 skesa &&\
  chmod +x skesa &&\
  mkdir /data

ENV PATH=${PATH}:/skesa

WORKDIR /data

#### Example command to run skesa in container w PE, interleaved reads (broken into 2 lines for readability):
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/skesa:2.3.0 \
#   skesa --fastq /data/Ecoli-PE-interleaved.fastq.gz --use_paired_ends --cores 8 --contigs_out /data/Ecoli.skesa.contigs.fasta

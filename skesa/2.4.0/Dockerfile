FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL version="1.0.0"
LABEL software="SKESA"
LABEL software.version="2.4.0"
LABEL description="Strategic Kmer Extension for Scrupulous Assemblies"
LABEL website="https://github.com/ncbi/SKESA"
LABEL lisence="https://github.com/ncbi/SKESA/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y wget

# get skesa, gfa_connector, and kmercounter binaries, rename them
RUN mkdir skesa && \
  cd skesa && \
  wget https://github.com/ncbi/SKESA/releases/download/2.4.0/skesa.centos.7.7 && \
  wget https://github.com/ncbi/SKESA/releases/download/2.4.0/gfa_connector.centos7.7 && \
  wget https://github.com/ncbi/SKESA/releases/download/2.4.0/kmercounter.centos7.7 && \
  mv skesa.centos.7.7 skesa && \
  mv gfa_connector.centos7.7 gfa_connector && \
  mv kmercounter.centos7.7 kmercounter && \
  chmod +x skesa gfa_connector kmercounter && \
  mkdir /data

# set PATH, set perl locale settings for singularity compatibility
ENV PATH=${PATH}:/skesa \
  LC_ALL=C

WORKDIR /data

#### Example commands ####

##  Assemble PE, interleaved reads in your $PWD (broken into 2 lines for readability)
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/skesa:2.4.0 \
#   skesa --fastq /data/Ecoli-PE-interleaved.fastq.gz --use_paired_ends --cores 8 --contigs_out /data/Ecoli.skesa.contigs.fasta

## Example from SKESA readme, download K. pneumoniae reads from SRA and assemble
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/skesa:2.4.0 \
#   skesa --sra_run SRR1510963 --hash_count --contigs_out /data/SRR1510963_skesa.fasta

## example using PE reads that are in your PWD
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/skesa:2.4.0 \
#   skesa --cores 8 --memory 24 --reads /data/SRR11306390.sra_1.fastq /data/SRR11306390.sra_2.fastq --hash_count --contigs_out /data/SRR11306390.skesa.contigs.fasta

## View full SKESA help options
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/skesa:2.4.0 skesa -h

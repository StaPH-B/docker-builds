FROM ubuntu:jammy AS app

# not actually used, but just marking for visibility this is the version of IRMA included
ARG IRMA_VER="1.2.0"
# actually used
ARG IRMA_RELEASE_DATE="202408"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="IRMA"
LABEL software.version="${IRMA_VER}"
LABEL description="IRMA was designed for the robust assembly, variant calling, and phasing of highly variable RNA viruses. Currently IRMA is deployed with modules for influenza, ebolavirus and coronavirus."
LABEL website="https://wonder.cdc.gov/amd/flu/irma/"
LABEL license="https://wonder.cdc.gov/amd/flu/irma/disclaimer.html"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    unzip \
    wget \
    r-base \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install IRMA
RUN wget https://wonder.cdc.gov/amd/flu/irma/flu-amd-${IRMA_RELEASE_DATE}.zip &&\
    unzip flu-amd-${IRMA_RELEASE_DATE}.zip &&\
    rm -v flu-amd-${IRMA_RELEASE_DATE}.zip

ENV PATH="${PATH}:/flu-amd" \
    LC_ALL=C

CMD ["IRMA"]

WORKDIR /data

## Test ##
FROM app AS test

RUN cd /flu-amd/tests && \
    ./test_run.sh

# do custom tests in /test directory
WORKDIR /test

# setting up irma_config.sh file so tests run w/ more cpus and other settings
RUN num_cpus_actual=$(nproc) && \
  echo "DEBUG: Number of CPUs available: ${num_cpus_actual}. Setting this in irma_config.sh file..." && \
  echo "SINGLE_LOCAL_PROC=${num_cpus_actual}" > irma_config.sh && \
  # set this variable to half the value of num_cpus_actual, as per the IRMA documentation: https://wonder.cdc.gov/amd/flu/irma/configuration.html
  echo "DOUBLE_LOCAL_PROC=$((${num_cpus_actual}/2))" >> irma_config.sh && \
  # this setting is to test IRMA's feature to replace bases that don't reach 1000X coverage with Ns in the <outdir>/amended_consensus/*.fasta files
  # 1000X is obviously a high value, but this is just for testing purposes
  echo 'MIN_CONS_SUPPORT="1000"' >> irma_config.sh 

# test with H5N1 sample from USDA collected in 2024 from cattle
# SRR28752647
# SAMN41019197 https://www.ncbi.nlm.nih.gov/biosample?LinkName=nuccore_biosample&from_uid=2725951746
# used as a reference genome for 2024 cattle outbreak analysis in this repo: https://github.com/andersen-lab/avian-influenza
RUN echo "downloading test H5N1 data now..." && \
  wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR287/047/SRR28752647/SRR28752647_1.fastq.gz && \
  wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR287/047/SRR28752647/SRR28752647_2.fastq.gz && \
  IRMA FLU SRR28752647_1.fastq.gz SRR28752647_2.fastq.gz SRR28752647 --external-config irma_config.sh && \
  echo "IRMA test complete. Checking for Ns in amended_consensus/*.fa files..." && \
  grep 'N' SRR28752647/amended_consensus/*.fa
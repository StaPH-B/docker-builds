# base image
FROM ubuntu:jammy as app

ARG KMAVER="1.4.10"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="kma"
LABEL software.version="$KMAVER"
LABEL description="K-mer alignment of raw reads against a database"
LABEL website="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license.type="Apache License, V2.0"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Eetu Eklund"
LABEL maintainer2.email="eetu.eklund@maryland.gov"

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libz-dev \
  make \
  wget \
  ca-certificates \
  git && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN git clone https://bitbucket.org/genomicepidemiology/kma.git && \
  cd kma && \
  git fetch && \
  git checkout $KMAVER && \
  make && \
  mkdir data

ENV PATH="$PATH:/kma" \
    LC_ALL=C

WORKDIR data

# test stage
FROM app as test 

# set /test as working directory for test below
WORKDIR /test 

# Downloads E.coli genome and runs kma index on it
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
  gunzip GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
  kma index -i GCA_012224845.2_ASM1222484v2_genomic.fna -o /test/database

# Downloads read files and uses them for kma mapping against database; print kma version
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_1.fastq.gz && \
  wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_2.fastq.gz && \
  kma -ipe SRR6903006_1.fastq.gz SRR6903006_2.fastq.gz -o /test/test_output -t_db /test/database -tmp /tmp/ && \
  kma -v

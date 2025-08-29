FROM mambaorg/micromamba:2.3.2-ubuntu22.04 AS app

ARG SEQSERO2_VER="1.3.1"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user

LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="SeqSero2"
LABEL software.version="${SEQSERO2_VER}"
LABEL description="Salmonella serotyping from genome sequencing data"
LABEL website="https://github.com/denglab/SeqSero2"
LABEL license="https://github.com/denglab/SeqSero2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# unzip just needed for test stage. It's tiny so no harm to keep in APP stage
RUN apt-get update && apt-get install -y --no-install-recommends \
  unzip && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install your desired software into the base conda/micromamba environment, pinning the version
# clean up conda garbage
# make /data to use as a working directory
RUN micromamba install --name base -c conda-forge -c bioconda seqsero2=${SEQSERO2_VER} && \
 micromamba clean -a -f -y && \
 mkdir /data

# set the environment, add base conda/micromamba bin directory into path
# set locale settings to UTF-8
ENV PATH="/opt/conda/bin/:${PATH}" \
 LC_ALL=C.UTF-8

# setting default command to run when running the container
CMD [ "SeqSero2_package.py", "--help" ]

# set final working directory to /data
WORKDIR /data

# new base for testing
FROM app AS test

# list all tools installed via micromamba (put these in the tool-specific REAMDME.md)
RUN micromamba list -n base

# carry out test commands within /test directory
WORKDIR /test

# print help options, check dependencies, print version
RUN SeqSero2_package.py --help && \
SeqSero2_package.py --check && \
SeqSero2_package.py --version

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget -q https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
  chmod +x datasets && \
  mv -v datasets /usr/local/bin

# download an example assembly; test with SeqSero2
# Salmonella enterica serovar Infantis genome: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCA_007765495.1/
# BioSample:SAMN07684583
ARG GENBANK_ACCESSION="GCA_007765495.1"
RUN datasets download genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
    mkdir -v ${GENBANK_ACCESSION}-download && \
    unzip ${GENBANK_ACCESSION}.zip -d ${GENBANK_ACCESSION}-download && \
    rm ${GENBANK_ACCESSION}.zip && \
    mv -v ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}*.fna ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna && \
    SeqSero2_package.py \
      -i ${GENBANK_ACCESSION}-download/ncbi_dataset/data/${GENBANK_ACCESSION}/${GENBANK_ACCESSION}.genomic.fna \
      -t 4 \
      -m k \
      -d ${GENBANK_ACCESSION}-seqsero2-assembly-kmer-mode \
      -n ${GENBANK_ACCESSION} \
      -p 2 && \
    grep 'Infantis' ${GENBANK_ACCESSION}-seqsero2-assembly-kmer-mode/SeqSero_result.txt

# testing reads as input for the same Salmonella isolate
# specifically the "allele" mode which does micro assembly first using SPAdes
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_1.fastq.gz && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_2.fastq.gz && \
    SeqSero2_package.py \
      -i SRR6082043_1.fastq.gz SRR6082043_2.fastq.gz \
      -t 2 \
      -m a \
      -d SRR6082043-seqsero2-reads-allele-mode \
      -n SRR6082043 \
      -p 2 && \
    grep 'Infantis' SRR6082043-seqsero2-reads-allele-mode/SeqSero_result.txt

# Tests for various subspecies (truly testing SalmID's functionality here)
# look for various subspecies listed here in SalmID code: https://github.com/hcdenbakker/SalmID/blob/c50df40caef2fb97c178d6890961e0e527992324/salmid/core.py#L189
# SUBSPECIES I enterica. Tested above with the Infantis isolate

## SUBSPECIES II salamae


## SUBSPECIES IIIa arizonae


## SUBSPECIES IIIb diarizonae


### SUBSPECIES IV houtenae


### SUBSPECIES VI indica
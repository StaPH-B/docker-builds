FROM ubuntu:focal as app

ARG BLAST_VER="2.14.1"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="blast+"
LABEL software.version=$BLAST_VER
LABEL description="Finds matches in sequencing reads"
LABEL website="https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download"
LABEL license="https://www.ncbi.nlm.nih.gov/IEB/ToolBox/CPP_DOC/lxr/source/scripts/projects/blast/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  ca-certificates \
  libgomp1 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install and/or setup more things. Make /data for use as a working dir
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
  mkdir /data

# ENV instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="/ncbi-blast-${BLAST_VER}+/bin:$PATH" \
  LC_ALL=C

# WORKDIR sets working directory
WORKDIR /data

# default command is to pull up help options for virulencefinder
# yes, there are more tools than blastn, but it's likely the most common one used
CMD [ "blastn", "-help" ]



# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app as test

# getting all the exectubles in bin
RUN ls /ncbi-blast-*/bin/

# getting a genome
RUN mkdir db && \
  wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz -P db && \
  gunzip db/GCF_000005845.2_ASM584v2_genomic.fna.gz && \
  makeblastdb -dbtype nucl -in db/GCF_000005845.2_ASM584v2_genomic.fna

# getting a list of genes
RUN wget https://raw.githubusercontent.com/rrwick/Unicycler/main/unicycler/gene_data/dnaA.fasta

# getting some blast results
RUN tblastn -query dnaA.fasta \
  -db db/GCF_000005845.2_ASM584v2_genomic.fna \
  -outfmt '6' \
  -out blast_hits.txt && \
  head blast_hits.txt

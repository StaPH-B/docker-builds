#!/bin/bash
# This script is to test that the program BWA runs as expected

VERSION=$1

# Check version (from stderr)
bwa 2> version.txt
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if grep -q "Version: ${VERSION}" version.txt; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  bwa
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz -O R2.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/genome/MN908947.3/GCA_009858895.3_ASM985889v3_genomic.200409.fna.gz -O reference.fna.gz
gunzip reference.fna.gz

# Run program

# Construct the FM-index for the reference assembly
bwa index reference.fna 

# Align paired-end reads to an assembly with option -v: output errors and warnings
bwa mem \
  -v 2 \
  reference.fna \
  R1.fastq.gz R2.fastq.gz \
  > test.sam

# Verify output
FILE="test.sam"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "821f4f4bd08f50035f7f99c3180d1ec8a7ff028d1e743530cc7bd775ca3757b5" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

#!/bin/bash
# This script is to test that the program Pilon runs as expected

VERSION=$1

# Check version
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(pilon --version)" == "Pilon version ${VERSION} Mon Nov 26 16:04:05 2018 -0500" ]; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  pilon --version
  exit 1
fi

# Get data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/sarscov2/genome/genome.fasta
wget -nv https://github.com/nf-core/test-datasets/raw/modules/data/genomics/sarscov2/illumina/bam/test.paired_end.sorted.bam
wget -nv https://github.com/nf-core/test-datasets/raw/modules/data/genomics/sarscov2/illumina/bam/test.paired_end.sorted.bam.bai

# Run program to improve a draft assembly
 pilon \
 --genome genome.fasta \
 --bam test.paired_end.sorted.bam \
 --output test \
 --outdir results \
 --changes \
 --fix snps,indels \
 --mindepth 0.50

# Verify output
FILE="results/test.fasta"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "1ed3147464eeeb116adf1a5ae6a6edaae280a77fbf25e978b916efdfab29cb42" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

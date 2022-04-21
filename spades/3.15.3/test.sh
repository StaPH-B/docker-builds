#!/bin/bash
# This script is to test that the program SPAdes runs as expected

VERSION=$1

# Check version (from stderr)
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(spades.py -v 2>&1)" == "SPAdes genome assembler v${VERSION}" ]; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  spades.py -v
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Run program (limit to 2GB RAM)
spades.py \
  --pe1-1 R1.fastq.gz \
  --pe1-2 R2.fastq.gz \
  --memory 2 \
  -o results \
  --phred-offset 33 \
  --only-assembler

# Verify output
FILE="results/contigs.fasta"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "009d9ac0eabb6d8bd548b5f56ef74724ac5d6ffd7a47e46144679154a15b506f" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

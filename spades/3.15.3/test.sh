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

# Run SPAdes own tests
spades.py --test

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz -O R2.fastq.gz

# Run program (limit to 2GB RAM)
spades.py \
  --pe1-1 R1.fastq.gz \
  --pe1-2 R2.fastq.gz \
  --isolate \
  --memory 2 \
  --phred-offset 33 \
  -o results

# Verify output
FILE="results/contigs.fasta"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "d47d87a6838d6c2d5a24d2690357cc3f80746d1756d4b3a0c551df70b58ed295" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

#!/bin/bash
# This script is to test that the program FLASH runs as expected

FLASH_VER=$1

# Check version
FLASH_VER=${FLASH_VER:="no version set"}  # ensure output doesn't match empty value if unset
flash -v > version.txt
if grep -q "FLASH v${FLASH_VER}" version.txt ; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  cat version.txt
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Run program
flash \
  R1.fastq.gz R2.fastq.gz \
  --min-overlap=100 \
  --max-overlap=126 \
  --output-prefix=test \
  --output-directory=results

# Verify output
FILE="results/test.notCombined_1.fastq"
cat $FILE | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" | sha256sum > ${FILE}_sorted_sha256sum  # Sort and generate checksum
if grep -q "25b6dd4d3ffbdc8a4f5bd19a29deb5f820483769871bfd167c792def8413942b" ${FILE}_sorted_sha256sum ; then  # Verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum"
  exit 1
fi
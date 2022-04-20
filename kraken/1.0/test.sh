#!/bin/bash
# This script is to test that the program Kraken runs as expected

KRAKEN_VER=$1

# Check version
kraken --version > version.txt
KRAKEN_VER=${KRAKEN_VER:="no version set"}  # ensure output doesn't match empty value if unset
if grep -q "Kraken version ${KRAKEN_VER}" version.txt; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  kraken --version
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Make sure files are small enough to run in reasonable time
N_READS_TO_TEST=1000
N_LINES=$((N_READS_TO_TEST*4))
for FILE_PREFIX in R1 R2; do
  gunzip -c $FILE_PREFIX.fastq.gz | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" \
  | head -n $N_LINES | gzip -f > ${FILE_PREFIX}_head_$N_LINES.fastq.gz
done

# Run program
export KRAKEN_DEFAULT_DB=/kraken-database/minikraken_20171013_4GB
kraken --fastq-input --gzip-compressed R1_head_$N_LINES.fastq.gz R2_head_$N_LINES.fastq.gz > kraken_output.txt
kraken-report kraken_output.txt > kraken.tab

# Verify output
FILE="kraken.tab"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "d0464b787b0bdf0e823de770f55c782d62e73f6194adca54a86713df06089a6e" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum"
  exit 1
fi

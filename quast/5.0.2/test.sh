#!/bin/bash
# This script is to test that the program QUAST runs as expected

VERSION=$1

# Check version
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(quast.py --version)" == "QUAST v${VERSION}" ]; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  quast.py --version
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna

# Run program to QC an assembly
# See http://quast.sourceforge.net/docs/manual.html#sec2.3 for what command line options mean
quast.py \
  --output-dir results \
  --min-contig 100 \
  --gene-finding \
  --gene-thresholds 300 \
  --contig-thresholds 500,1000 \
  --strict-NA \
  NCTC13799.fna

# Verify output
FILE="results/report.txt"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "8d41f83b516738b8998fa3099238bb4ae740114191d386fbaabbd70e391276cf" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

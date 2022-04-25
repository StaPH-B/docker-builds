#!/bin/bash
# This script is to test that the program MLST runs as expected

VERSION=$1

# Check version
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(mlst --version)" == "mlst $VERSION" ]; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  mlst --version
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna

# Run program to scan a genome assembly against PubMLST
mlst NCTC13799.fna > mlst-results.tsv

# Verify output
FILE="mlst-results.tsv"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "65827efaf81724384185d829e0155d64a7b4236ac30ecb3ff1cc9b835ae5c169" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

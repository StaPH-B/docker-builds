#!/bin/bash
# This script is to test that the program Prokka runs as expected

VERSION=$1

# Check version (from stderr)
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(prokka --version 2>&1)" == "prokka ${VERSION}" ]; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  prokka --version
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna

# List databases prokka has installed to use
prokka --listdb

# Run program to annotate a genome assembly with option: --addgenes Add 'gene' features for each 'CDS' feature
prokka \
  --outdir results \
  --prefix test \
  --addgenes \
  NCTC13799.fna

# Verify output
FILE="results/test.gff"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "75ee8d716f94a24a8a408996b282f25a27da2e407af3d177f720538a475cda82" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

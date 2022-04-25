#!/bin/bash
# This script is to test that the program bedtools runs as expected

VERSION=$1

# Check version
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(bedtools --version)" == "bedtools v${VERSION}" ]; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  bedtools --version
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/modules/data/genomics/sarscov2/illumina/bam/test.paired_end.sorted.bam

# Run program to calculate assembly coverage with 1-based coordinates
bedtools genomecov \
    -d \
    -ibam test.paired_end.sorted.bam > coverage.txt

# Verify output
FILE="coverage.txt"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "c362573b4142d1efc06b93b2eccb1788b813188f842941d2a04acb4d380242f3" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

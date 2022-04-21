#!/bin/bash
# This script is to test that the program Kraken2 runs as expected

KRAKEN2_VER=$1

# Check version
kraken2 --version > version.txt
KRAKEN2_VER=${KRAKEN2_VER:="no version set"}  # ensure output doesn't match empty value if unset
if grep -q "Kraken version ${KRAKEN2_VER}" version.txt; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  kraken2 --version
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
export KRAKEN2_DEFAULT_DB=/kraken2-db
kraken2 \
  --gzip-compressed \
  --use-names \
  --report kraken2.tab \
  --memory-mapping \
  R1_head_$N_LINES.fastq.gz \
  R2_head_$N_LINES.fastq.gz  > kraken2_output.txt

# Verify output
FILE="kraken2.tab"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "1300129443f84d9bb3e39d2d27493a667c1c4e773d8480f3013a798e43e9f98e" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi

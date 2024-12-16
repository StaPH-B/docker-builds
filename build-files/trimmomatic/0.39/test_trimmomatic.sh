#!/bin/bash
# This script is to test that the program Trimmomatic runs as expected

TRIMMOMATIC_VER=$1

# Check version
TRIMMOMATIC_VER=${TRIMMOMATIC_VER:="no version set"}  # ensure output doesn't match empty value if unset
if [ "$(trimmomatic -version)" == "${TRIMMOMATIC_VER}" ] ; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  trimmomatic -version
  exit 1
fi

# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Run program
ADAPTERS="/Trimmomatic-0.39/adapters/TruSeq3-PE.fa"  # trimmomatic docs says these are used in HiSeq and MiSeq machines
trimmomatic \
  PE \
  -phred33 \
  R1.fastq.gz R2.fastq.gz \
  R1.paired.fq R1.unpaired.fq \
  R2.paired.fq R2.unpaired.fq \
  ILLUMINACLIP:$ADAPTERS:2:20:10:8:TRUE \
  SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50

# Verify output
FILE="R1.paired.fq"
cat $FILE | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" | sha256sum > ${FILE}_sorted_sha256sum  # Sort and generate checksum
if grep -q "d0ba742d55e975ca29fc55a97d0b7f5766558380e4f1fb618dfea7208b5c3bd9" ${FILE}_sorted_sha256sum ; then  # Verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum"
  exit 1
fi
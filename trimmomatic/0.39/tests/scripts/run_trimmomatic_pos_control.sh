#!/bin/bash
# This script runs trimmomatic to remove Illumina sequencing adaptors and quality-trim/quality-filter reads.

R1=/data/R1.fastq.gz
R2=/data/R2.fastq.gz
OUTDIR=/test_result
mkdir -p $OUTDIR

ADAPTERS="/Trimmomatic-0.39/adapters/TruSeq3-PE.fa"  # trimmomatic docs says these are used in HiSeq and MiSeq machines

echo "Running trimmomatic on test data to trim & filter reads"
trimmomatic \
  PE \
  -phred33 \
  $R1 $R2 \
  $OUTDIR/R1.paired.fq $OUTDIR/R1.unpaired.fq \
  $OUTDIR/R2.paired.fq $OUTDIR/R2.unpaired.fq \
  ILLUMINACLIP:$ADAPTERS:2:20:10:8:TRUE \
  SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50

for R in R1 R2; do
  for P in paired unpaired; do
    # Thanks: https://edwards.flinders.edu.au/sorting-fastq-files-by-their-sequence-identifiers/
    cat $OUTDIR/$R.$P.fq | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" | sha256sum > $OUTDIR/$R.$P.fq.sha256sum
  done
done
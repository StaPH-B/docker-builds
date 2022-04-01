#!/bin/bash
# This script runs FLASH to merge overlapping paired-end reads.

R1=/data/R1.fastq.gz
R2=/data/R2.fastq.gz
OUTDIR=/test_result
mkdir -p $OUTDIR

# Get read length, make minimum overlap 80% of read length
READ_LEN=$(gunzip -c "$R1" | head -n 400 \
  | awk 'NR%4==2 {if(length > x) {x=length; y=$0}} END{print length(y)}')
OVERLAP_LEN=$(echo "$READ_LEN * 0.8" | bc | sed 's/\..*//')
echo "INFO: $READ_LEN bp read length detected from raw input"

echo "Running FLASH on test data to merge overlapping paired-end reads"
flash \
  $R1 $R2 \
  --min-overlap=$OVERLAP_LEN \
  --max-overlap=$READ_LEN \
  --output-prefix=test \
  --output-directory=$OUTDIR

for F in test.extendedFrags.fastq test.notCombined_1.fastq test.notCombined_2.fastq; do
  # Thanks: https://edwards.flinders.edu.au/sorting-fastq-files-by-their-sequence-identifiers/
  cat $OUTDIR/$F | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" | sha256sum > $OUTDIR/$F.sha256sum
done

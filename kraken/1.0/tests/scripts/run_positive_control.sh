#!/bin/bash
# This script uses read files from NCBI for reference strain Escherichia coli O157:H7 CDC EDL 933.
# The input data has already had PhiX removed and quality filtered/trimmed reads.
# This script runs Kraken to taxonomically assign reads.

I=/test_data/trim_reads
O=/test_data/trim_reads
mkdir -p $O

B=SRR5481494_sub

N_READS_TO_TEST=1000
export KRAKEN_DEFAULT_DB=/kraken-database/minikraken_20171013_4GB

# Make sure files are small enough to run in reasonable time and compress input for kraken
N_LINES=$(($N_READS_TO_TEST*4))
echo "Subsampling to $N_READS_TO_TEST reads ($N_LINES lines of fastq file)"
for S in extendedFrags notCombined_1 notCombined_2; do
  gunzip -c "$I"/"$B"."$S".fastq.gz | paste - - - - | sort -k1,1 -t " " | tr "\t" "\n" \
  | head -n $N_LINES | gzip -f > "$I"/"$B"."$S"_head$N_LINES.fastq.gz
done

echo "Running Kraken on test data to taxonomically assign reads"
kraken \
  --fastq-input \
  --gzip-compressed \
  $I/"$B".notCombined_1_head$N_LINES.fastq.gz \
  $I/"$B".notCombined_2_head$N_LINES.fastq.gz \
  $I/"$B".extendedFrags_head$N_LINES.fastq.gz > $O/kraken_output.txt;
  kraken-report $O/kraken_output.txt > $O/"$B"_kraken.tab

for F in "$O"/kraken_output.txt "$O"/"$B"_kraken.tab; do
  shasum -a 256 $F >> "$O"/kraken_checksums.txt
done
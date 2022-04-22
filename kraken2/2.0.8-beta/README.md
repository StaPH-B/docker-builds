# Kraken

This image implements the taxonomic sequence classifier [Kraken2](https://github.com/DerrickWood/kraken2).
Documentation is available at https://github.com/DerrickWood/kraken2/blob/master/docs/MANUAL.markdown. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (paired-end reads)
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Specify the database to use
export KRAKEN2_DEFAULT_DB=/kraken2-db

# Run program to classify reads
kraken2 \
  --gzip-compressed \
  --use-names \
  --report kraken2.tab \
  --memory-mapping \
  R1.fastq.gz \
  R2.fastq.gz  > kraken2_output.txt
```

## Example output

The on-screen output tells you what the program did:

```
Loading database information... done.
2000 sequences (0.25 Mbp) processed in 2.899s (41.4 Kseq/m, 5.22 Mbp/m).
    1981 sequences classified (99.05%)
    19 sequences unclassified (0.95%)
```
*note: example output is actually from analyzing only the first 1000 reads in each file

The results files from this command are:
```
kraken2.tab  # per-taxon report
kraken2_output.txt  # per-read (or read-pair) classifications
```

# Kraken

This image implements the taxonomic sequence classifier [Kraken](https://github.com/DerrickWood/kraken).
Documentation is available at http://ccb.jhu.edu/software/kraken/MANUAL.html. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (paired-end reads)
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Specify the database to use
export KRAKEN_DEFAULT_DB=/kraken-database/minikraken_20171013_4GB

# Run program to classify reads
kraken \
    --fastq-input \
    --gzip-compressed \
    R1.fastq.gz \
    R2.fastq.gz > kraken_output.txt

# Generate per-taxon report
kraken-report kraken_output.txt > kraken.tab
```

## Example output

The on-screen output tells you what the program did:

```
2000 sequences (0.25 Mbp) processed in 3.665s (32.7 Kseq/m, 4.13 Mbp/m).
    1716 sequences classified (85.80%)
    284 sequences unclassified (14.20%)
```
*note: example output is actually from analyzing only the first 1000 reads in each file

The results files from this command are:
```
kraken.tab  # per-taxon report
kraken_output.txt  # per-read (or read-pair) classifications
```

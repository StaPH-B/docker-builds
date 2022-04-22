# SPAdes

This image implements the de novo genome assembler [SPAdes](https://github.com/ablab/spades).
Documentation is available at https://cab.spbu.ru/files/release3.15.4/manual.html. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (paired-end sequencing of a SARS-CoV-2 isolate)
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz -O R2.fastq.gz

# Run program in 'isolate' mode (limit to 2GB RAM)
spades.py \
  --pe1-1 R1.fastq.gz \
  --pe1-2 R2.fastq.gz \
  --isolate \
  --memory 2 \
  --phred-offset 33 \
  -o results
```

## Example output

The results files from this command are many, the most important being:
```
results/contigs.fasta  # assembled contigs
results/spades.log  # program logfile
```

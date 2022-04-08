# Seqtk container

Main tool : [Seqtk](https://github.com/lh3/seqtk)

Full documentation: https://github.com/lh3/seqtk

> Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format. It seamlessly parses both FASTA and FASTQ files which can also be optionally compressed by gzip.

# Example Usage

From github:

```
# Convert FASTQ to FASTA:

seqtk seq -a in.fq.gz > out.fa

# Extract sequences in regions contained in file reg.bed:

seqtk subseq in.fa reg.bed > out.fa
```

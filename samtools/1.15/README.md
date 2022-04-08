# samtools container

Main tool : [samtools](https://www.htslib.org/)

Full documentation: https://www.htslib.org/doc/samtools.html

> Utilities for the Sequence Alignment/Map (SAM) format

# Example Usage

```
# removing amplicons from aligned reads in bam file
samtools ampliconclip -b bed.file input.bam
```
```
# sorting a bam file
samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam
```

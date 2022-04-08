# Unicycler container

Main tool : [Unicycler](https://github.com/rrwick/Unicycler)

Additional tools:
- ncbi-blast
- pilon
- spades
- samtools
- bcftools
- miniasm

Full documentation: https://github.com/rrwick/Unicycler

Hybrid assembly of long reads (i.e. from nanopore/ONT sequencing) and Illumina short reads

# Example Usage

```
# hybrid assembly
unicycler -1 short_reads_1.fastq.gz -2 short_reads_2.fastq.gz -l long_reads.fastq.gz -o output_dir
```

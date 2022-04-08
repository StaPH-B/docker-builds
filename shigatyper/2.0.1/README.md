# ShigaTyper container

Main tool : [ShigaTyper](https://github.com/CFSAN-Biostatistics/shigatyper)

Additional tools:
- MINIMAP2
- bcftools

Full documentation: https://github.com/CFSAN-Biostatistics/shigatyper

> ShigaTyper is a quick and easy tool designed to determine Shigella serotype using Illumina (single or paired-end) or Oxford Nanopore reads with low computation requirement.

# Example Usage

```
# Paired-end reads
shigatyper.py --R1 SRX5006488_R1.fastq.gz --R2 SRX5006488_R2.fastq.gz
sample  prediction      ipaB
SRX5006488      Shigella boydii serotype 12     +

# Single-end reads
shigatyper.py --SE SRX5006488.fastq.gz
sample  prediction      ipaB
SRX5006488-se   Shigella boydii serotype 12     +

# Oxford Nanopore reads
shigatyper.py --SE SRX7050861.fastq.gz --ont
sample  prediction      ipaB
SRX7050861-ont  Shigella dysenteriae serotype 3 +
```

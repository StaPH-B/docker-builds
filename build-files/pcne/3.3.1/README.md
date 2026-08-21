# PCNE container

Main tool: [PCNE](https://github.com/riccabolla/PCNE)
  
Code repository: https://github.com/riccabolla/PCNE

Additional tools:
- R: 4.4.3
- BWA: 0.7.18
- Minimap2: 2.3
- Samtools: 1.20
- bedtools: 2.31.1

Additional libraries:
- readr: 2.1.5
- dplyr: 1.1.4
- ggplot2: 3.5.2
- purrr: 1.0.0

Basic information on how to use this tool:
- executable: pcne
- help: `-h`, `--help`
- version: `--version`
- description: A tool to estimate the copy numbers of plasmids detected in an assembled genome

Additional information:

Bollini R, Cento V. PCNE: A Tool for Plasmid Copy Number Estimation. Bioinformatics and Biology Insights. 2026;20. [doi:10.1177/11779322251410037](https://doi.org/10.1177/11779322251410037)

PCNE can use as input:

- short reads (paired-end)
- long reads
- bam file

PCNE can run a model-based correction for GC content bias via `--gc-correction `

## Example Usage
These commands generate a *.tsv* file reporting the plasmid copy number.

```bash
#short reads
pcne -c <chromosome.fasta> -p <plasmid.fasta> -r <reads_R1.fastq.gz> -R <reads_R2.fastq.gz> [-t <threads>] [-o <output_prefix>]
```

```bash
#long reads
pcne_long --c <chromosome.fasta> -p <plasmid.fasta> -r <reads.fastq.gz> [-t <threads>] [-o <output_prefix>]
```

```bash
#with multiple plasmids
pcne_long --c <chromosome.fasta> -p <plasmid_*.fasta> -r <reads.fastq.gz> [-t <threads>] [-o <output_prefix>]
```

```bash
#using bam input
pcne -c <chromosome.fasta> -p <plasmid.fasta> -b <alignment.bam> [-t <threads>] [-o output_preifx]
```

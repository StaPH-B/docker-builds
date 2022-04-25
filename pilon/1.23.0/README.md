# Pilon

This image implements the assembly improvement and strain variation detection program [Pilon](https://github.com/broadinstitute/pilon).
Documentation is available at https://github.com/broadinstitute/pilon/wiki. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (a genome assembly and indexed bam file)
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/genomics/sarscov2/genome/genome.fasta
wget -nv https://github.com/nf-core/test-datasets/raw/modules/data/genomics/sarscov2/illumina/bam/test.paired_end.sorted.bam
wget -nv https://github.com/nf-core/test-datasets/raw/modules/data/genomics/sarscov2/illumina/bam/test.paired_end.sorted.bam.bai

# Run program to improve a draft assembly
 pilon \
 --genome genome.fasta \
 --bam test.paired_end.sorted.bam \
 --output test \
 --outdir results \
 --changes \
 --fix snps,indels \
 --mindepth 0.50
```

## Example output

The on-screen output tells you what the program did:
```
Pilon version 1.23 Mon Nov 26 16:04:05 2018 -0500
Genome: genome.fasta
Fixing snps, indels
Input genome size: 29829
Processing MT192765.1:1-29829
bam test.paired_end.sorted.bam: coverage 1
Total Reads: 200, Coverage: 1, minDepth: 5
Confirmed 612 of 29829 bases (2.05%)
Corrected 1 snps; 0 ambiguous bases; corrected 0 small insertions totaling 0 bases, 0 small deletions totaling 0 bases
MT192765.1:1-29829 log:
Finished processing MT192765.1:1-29829
Writing MT192765.1:1-29829 changes to results/test.changes
Writing updated MT192765.1_pilon to results/test.fasta
Mean bam coverage: 1
Mean total coverage: 1
```
The results files from this command are:
```
test.changes  # the corrections made
test.fasta  # the corrected genome
```

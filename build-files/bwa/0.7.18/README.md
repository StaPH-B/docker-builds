# BWA container

Main tool: [bwa](https://bio-bwa.sourceforge.net/)

Code repository: https://github.com/lh3/bwa

Basic information on how to use this tool:

- executable: bwa
- description: Burrows-Wheeler Aligner

Full documentation: https://bio-bwa.sourceforge.net/

## Example Usage

```bash
# Illumina/454/IonTorrent single-end reads longer than ~70bp
bwa mem ref.fa reads.fq > aln.sam
# Illumina single-end reads shorter than ~70bp:
bwa aln ref.fa reads.fq > reads.sai
bwa samse ref.fa reads.sai reads.fq > aln-se.sam
# Illumina/454/IonTorrent paired-end reads longer than ~70bp:
bwa mem ref.fa read1.fq read2.fq > aln-pe.sam
# Illumina paired-end reads shorter than ~70bp:
bwa aln ref.fa read1.fq > read1.sai; bwa aln ref.fa read2.fq > read2.sai
bwa sampe ref.fa read1.sai read2.sai read1.fq read2.fq > aln-pe.sam
# PacBio subreads or Oxford Nanopore reads to a reference genome:
bwa mem -x pacbio ref.fa reads.fq > aln.sam
bwa mem -x ont2d ref.fa reads.fq > aln.sam
```

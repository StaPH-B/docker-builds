# Flye container

Main tool : [flye](https://github.com/fenderglass/Flye)

Full documentation: https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md

> Flye is a de novo assembler for single-molecule sequencing reads, such as those produced by PacBio and Oxford Nanopore Technologies.

## Example Usage

```bash
# sample.fastq.gz is compressed with bgzip
flye --nano-raw sample.fastq.gz --threads 12 --out-dir flye/sample
```

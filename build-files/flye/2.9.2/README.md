# Flye container

Main tool : [flye](https://github.com/fenderglass/Flye) 2.9.2

Full documentation: [https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md](https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md)

> Flye is a de novo assembler for single-molecule sequencing reads, such as those produced by PacBio and Oxford Nanopore Technologies.

Additional included tools:

- [minimap2](https://github.com/lh3/minimap2) 2.24-r1122
- python 3.8.10

## Example Usage

```bash
# sample.fastq.gz is compressed with bgzip
flye --nano-raw sample.fastq.gz --threads 12 --out-dir flye/sample
```

# raven container

Main tool : [raven](https://github.com/lbcb-sci/raven)

> Raven is a de novo genome assembler for long uncorrected reads.

# Example Usage

```
raven --polishing-rounds 2 --threads 4 --graphical-fragment-assembly sample.gfa sample.fastq > sample.fasta
```

Note : This version is built to work with CPUs. Does not support NVIDIA CUDA support.

# minibwa container

Main tool: [minibwa](https://github.com/lh3/minibwa)
  
Code repository: https://github.com/lh3/minibwa

Basic information on how to use this tool:
- executable: minibwa
- help: `--help`
- version: `version`
- description: Aligns short reads against a reference genome; it is 3x as fast as bwa-mem and 2x as fast as bwa-mem2 at comparable accuracy.

Additional information:

Minibwa is distributed under the MIT license. It also incorporates source code from the following projects:

    libsais: Apache 2 License. Copyright (c) 2021-2025 Ilya Grebnov
    mimalloc: MIT License. Copyright (c) 2018-2026 Microsoft Corporation, Daan Leijen

The master branch is optionally built on the following projects:
    QSufSort: HPND License. Copyright (c) 1999 N. Jesper Larsson
    bwtgen: GPL 2 License. Copyright (c) 2004 Wong Chi Kwong

Full documentation: https://github.com/lh3/minibwa#users-guide

## Example Usage

#### Indexing the reference genome
```bash
minibwa index -t8 ref.fa     # index with 8 threads, using 18N RAM (N is the genome size)
minibwa index ref.fa prefix  # use a different index prefix instead of ref.fa
minibwa index -l ref.fa      # use less memory at the cost of performance
minibwa index --meth ref.fa  # generate BS-seq index
```

#### Mapping to the reference genome
```bash
minibwa map -t8 ref.fa read1.fq read2.fq    # map paired-end reads and output SAM
minibwa map -ft8 ref.fa read.fa.gz          # map single-end or long reads; output PAF
minibwa map --hic ref.fa hic1.fq hic2.fq    # map Hi-C short reads
minibwa map --meth ref.fa read1.fq read2.fq # map BS-seq reads; requiring "index --meth"
```
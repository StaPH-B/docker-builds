# metaMDBG container

Main tool: [metaMDBG](https://github.com/GaetanBenoitDev/metaMDBG)
  
Code repository: https://github.com/GaetanBenoitDev/metaMDBG

Basic information on how to use this tool:
- executable: `metaMDBG`
- help: `--help`
- version: `--version`
- description: A fast and memory-efficient assembler designed for long and accurate metagenomics reads (e.g. PacBio HiFi, Nanopore R10)

Additional information:

This tool is optimized for metagenomes, but also works well on bacterial isolates samples, according to the author. The main GitHub page README.md has up-to-date benchmarks in the Results section. nanoMDBG is integrated into this tool. 

Note that the subcommands for `metaMDBG`, namely `asm` and `gfa` have `--help` commands as well.

Citations: 

* Gaetan Benoit, Sebastien Raguideau, Robert James, Adam M. Phillippy, Rayan Chikhi and Christopher Quince High-quality metagenome assembly from long accurate reads with metaMDBG, Nature Biotechnology (2023).

* Gaetan Benoit, Robert James, Sebastien Raguideau, Georgina Alabone, Tim Goodall, Rayan Chikhi and Christopher Quince High-quality metagenome assembly from nanopore reads with nanoMDBG, Nature Communications (2026).

Full documentation: https://github.com/GaetanBenoitDev/metaMDBG?tab=readme-ov-file#readme

## Example Usage

#### Nanopore assembly
```bash
metaMDBG asm --out-dir ./outputDir/ --in-ont reads.fastq.gz --threads 4
```

#### Hifi assembly
```bash
metaMDBG asm --out-dir ./outputDir/ --in-hifi reads.fastq.gz --threads 4
```

#### Multiple sample co-assembly
```bash
metaMDBG asm \
--out-dir ./outputDir/ \
--in-ont reads_A.fastq.gz reads_B.fastq.gz reads_C.fastq.gz \
--threads 4
```

#### Generating an assembly graph
```bash
metaMDBG gfa \
--assembly-dir ./assemblyDir/ \
--k 21 --contigpath --readpath --threads 4
```
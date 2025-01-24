# Canu container

Main tool : [Canu](https://github.com/marbl/canu)

Canu is a fork of the Celera Assembler, designed for high-noise single-molecule sequencing (such as the PacBio RS II/Sequel or Oxford Nanopore MinION).

## Example Usage

```bash
canu -p {sample} genomeSize={genome.length} -nanopore {input.fastq}
```

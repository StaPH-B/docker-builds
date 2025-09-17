# SKA2 container

Main tool: [SKA2](https://github.com/bacpop/ska.rust)
  
Code repository: https://github.com/bacpop/ska.rust

Basic information on how to use this tool:
- executable: ska
- help: -h, --help
- version: -V, --version
- description: SKA2 is a reimplementation of the SKA package in the rust language. Split k-mer analysis (version 2) uses exact matching of split k-mer sequences to align closely related sequences, typically small haploid genomes such as bacteria and viruses.
  
Full documentation: https://docs.rs/ska/latest/ska/

## Example Usage

```bash
# Build from two input FASTA files with a k-mer size of 31
ska build -o seqs -k 31 assemblies/seq1.fa assemblies/seq2.fa
# align
ska align --min-freq 1 --filter no-filter -o seqs seqs.skf
# map
ska map ref.fa seqs.skf -o ref_mapped.aln
```

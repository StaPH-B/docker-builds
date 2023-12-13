# dnaapler container

Main tool : [dnappler](https://github.com/gbouras13/dnaapler)

Full documentation: [https://github.com/gbouras13/dnaapler](https://github.com/gbouras13/dnaapler)

> `dnaapler` is a simple python program that takes a single nucleotide input sequence (in FASTA format), finds the desired start gene using blastx against an amino acid sequence database, checks that the start codon of this gene is found, and if so, then reorients the chromosome to begin with this gene on the forward strand.

dnaapler has several commands for chromosomes, plasmids, and more.

```
Usage: dnaapler [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help     Show this message and exit.
  -V, --version  Show the version and exit.

Commands:
  chromosome  Reorients your sequence to begin with the dnaA chromosomal...
  citation    Print the citation(s) for this tool
  custom      Reorients your sequence with a custom database
  mystery     Reorients your sequence with a random gene
  phage       Reorients your sequence to begin with the terL large...
  plasmid     Reorients your sequence to begin with the repA replication...
```

WARNING: Does not support multifasta files. Each sequence must be processed individually.

## Example Usage

```bash
# for a fasta of a chromsome sequence
dnaapler chromosome --input chromosome.fasta --output dnaapler_chr

# for a fasta of a plasmid sequence
dnaapler plasmid --input plasmid.fasta --output dnaapler_plasmid
```

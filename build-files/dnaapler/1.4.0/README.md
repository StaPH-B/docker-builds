# dnaapler container

Main tool : [dnappler](https://github.com/gbouras13/dnaapler)

## Additional dependencies

- mmseqs version 18-8cc5c

<details>
<summary>Additional tools installed via pip:</summary>


```
Package         Version
--------------- -----------
archspec        0.2.6
biopython       1.87
click           8.4.2
dnaapler        1.4.0
loguru          0.7.3
numpy           2.5.1
pandas          3.0.3
pip             24.0
pyrodigal       3.7.1
python-dateutil 2.9.0.post0
PyYAML          6.0.3
setuptools      68.1.2
six             1.17.0
wheel           0.42.0
```

</details>
</br>

Full documentation: [https://github.com/gbouras13/dnaapler](https://github.com/gbouras13/dnaapler)

> `dnaapler` is a simple python program that takes a single nucleotide input sequence (in FASTA format), finds the desired start gene using MMSeqs2, checks that the start codon of this gene is found, and if so, then reorients the chromosome to begin with this gene on the forward strand.


dnaapler has several commands for chromosomes, plasmids, and more.

```
Usage: dnaapler [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help     Show this message and exit.
  -V, --version  Show the version and exit.

Commands:
  all         Reorients contigs to begin with any of dnaA, repA, terL, or...
  archaea     Reorients your genome to begin with the archaeal COG1474...
  bulk        Reorients multiple genomes to begin with the same gene.
  chromosome  Reorients your genome to begin with the dnaA chromosomal...
  citation    Print the citation(s) for this tool.
  custom      Reorients your genome with a custom database.
  mystery     Reorients your genome with a random CDS.
  nearest     Reorients your genome to begin with the first CDS as...
  phage       Reorients your genome to begin with the terL large...
  plasmid     Reorients your genome to begin with the repA replication...
```

WARNING: Does not support multifasta files. Each sequence must be processed individually.

## Example Usage

```bash
# Reorienting for a fasta of a chromsome sequence
dnaapler chromosome --input chromosome.fasta --output dnaapler_chr

# Reorienting for a fasta of a plasmid sequence
dnaapler plasmid --input plasmid.fasta --output dnaapler_plasmid

# Reorienting Mixed Contigs
dnaapler all -i input_mixed_contigs.fasta -o output_directory_path -p my_bacteria_name
```

# ABRicate

> ABRicate: Mass screening of contigs for antimicrobial resistance or virulence genes. It comes bundled with multiple databases: NCBI, CARD, ARG-ANNOT, Resfinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF and VFDB.

Main tool : [ABRicate](https://github.com/tseemann/abricate)

Additional tools:

- any2fasta 0.8.1
- ncbi-blast+ 2.12.0
- perl 5.38.2
- bioperl 1.7.8

Additional information:

This image uses the most up-to-date databases at the time of building.

## Example Usage

```bash
# list out the available databases
abricate --list

# run using the default (NCBI) database
abricate input.fasta

# run using the vfdb database
abricate --db vfdb input.fa
```

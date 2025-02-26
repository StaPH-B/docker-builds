# Prokka container

Main tool : [Prokka](https://github.com/tseemann/prokka)

Additional tools:

- prodigal 2.6.3
- bedtools 2.29.0
- barrnap 0.9
- ncbi-blast+ 2.9.0
- tbl2asn 25.8
- hmmer 3.1b2 (February 2015)
- perl 5.26.1
- bioperl 1.7.2

Full documentation: [link to documentation](https://github.com/tseemann/prokka)

Automated prokaryotic genome annotation tool

## Example Usage

```bash
# run prokka on the provided test FASTA file (plasmid sequence)
prokka --cpus 2 --outdir asm --prefix asm test/plasmid.fna
```

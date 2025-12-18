# Prokka container

Main tool : [Prokka](https://github.com/tseemann/prokka)

Additional tools:

- prodigal 2.6.3
- bedtools 2.31.1
- barrnap 0.9
- ncbi-blast+ 2.12.0
- tbl2asn 25.3
- hmmer 3.4
- perl 5.38.2
- bioperl 1.7.8
- aragorn 1.2.41

Full documentation: [link to documentation](https://github.com/tseemann/prokka)

Automated prokaryotic genome annotation tool

## Example Usage

```bash
# run prokka on the provided test FASTA file (plasmid sequence)
prokka --cpus 2 --outdir asm --prefix asm test/plasmid.fna
```

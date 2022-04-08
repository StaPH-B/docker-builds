# Prokka container

Main tool : [Prokka](https://github.com/tseemann/prokka)

Additional tools:
- bedtools
- cpanm
- barrnap
- tbl2asn

Full documentation: https://github.com/tseemann/prokka

Automated prokaryotic genome annotation tool

# Example Usage

```
prokka \
  --mincontiglen 500 \
  --compliant \
  --locustag locus_tag \
  --cpu 16 \
  --centre staphb \
  --outdir prokka/sample \
  --prefix sample \
  --genus genus \
  --species species \
  --force sample.fasta
```

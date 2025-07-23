# Kraken2 2.1.5 container

Main tool : [Kraken2](https://github.com/DerrickWood/kraken2/)

Additional tools:

- perl 5.34.0
- ncbi-blast+ 2.12.0

- [Pre-built kraken2 databases can be found here](https://benlangmead.github.io/aws-indexes/k2)

This contains the Refeq viral 4/2/2025 database at /kraken2_db.

Full documentation: [link to documentation](https://github.com/DerrickWood/kraken2/wiki)

Kraken 2 is a fast and memory efficient tool for taxonomic assignment of metagenomics sequencing reads.

## Example Usage

```bash
# query Illumina paired-end reads against kraken2 standard 8GB database
kraken2 --report test.kraken2.1.2.salmonella.report \
  --output test.kraken2.1.2.salmonella.output \
  --paired \
  --db /kraken2_db \
  --threads 4 \
  SRR10992628_1.gz SRR10992628_2.gz 

# inspect a kraken2 database
kraken2-inspect --db ./k2_standard_8gb_20210517 --threads 4
```

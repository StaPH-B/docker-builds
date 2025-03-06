# Bracken container

Main tool: [Bracken](https://github.com/jenniferlu717/Bracken)
  
Code repository: https://github.com/jenniferlu717/Bracken

Additional tools:
- kraken2: 2.1.3
- python: 3.10.12
- perl: 5.34.0
- pigz: 2.6

Basic information on how to use this tool:
- executable: bracken
- help: -h
- version: -v
- description: Bracken is a companion program to Kraken 1, KrakenUniq, or Kraken 2 While Kraken classifies reads to multiple levels in the taxonomic tree, Bracken allows estimation of abundance at a single level using those classifications (e.g. Bracken can estimate abundance of species within a sample).

Additional information:

This container does not contain any kraken or bracken database. Please download precompiled database from [Ben Langmead's page](https://benlangmead.github.io/aws-indexes/k2). Those database files includes both kraken2 and bracken indexes.
  
Full documentation: https://ccb.jhu.edu/software/bracken/index.shtml?t=manual

## Example Usage

```bash
bracken -d database_folder -i kraken_report -o bracken_report -r 75 -l S -t 10
```
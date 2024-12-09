# KrakenUniq container

Main tool: [KrakenUniq](https://github.com/fbreitwieser/krakenuniq)
  
Code repository: https://github.com/fbreitwieser/krakenuniq

Additional tools:
- ncbi-blast+ : 2.12.0+

Basic information on how to use this tool:
- executable: krakenuniq
- help: --help
- version: --version
- description: KrakenUniq is a metagenomics classifier that combines the fast k-mer-based classification of Kraken with an efficient algorithm for assessing the coverage of unique k-mers found in each species in a dataset. 

Additional information:

KrakenUniq database can be downloaded from https://benlangmead.github.io/aws-indexes/k2
  
Full documentation: https://github.com/fbreitwieser/krakenuniq/blob/master/MANUAL.md

## Example Usage

```bash
krakenuniq --db /path/to/db --report-file report.txt --paired r1.fastq.gz r2.fastq.gz
```

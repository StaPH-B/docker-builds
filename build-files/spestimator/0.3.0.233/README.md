# Spestimator container

Main tool: [spestimator](https://github.com/erinyoung/Spestimator)
  
Code repository: https://github.com/erinyoung/Spestimator

Additional tools:
- list: blast+

Basic information on how to use this tool:
- executable: spestimator
- help: -h
- version: -v
- description: |

> Spestimator is a lightweight Python command-line tool designed to quickly identify bacterial species from input FASTA sequences (contigs or reads) and automatically retrieve their corresponding reference genomes from NCBI RefSeq.

  
Full documentation: https://github.com/erinyoung/Spestimator

## Example Usage

```bash
spestimator -i *.fna -o testing.csv --download-genomes genomes
```


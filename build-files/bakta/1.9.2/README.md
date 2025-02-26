# bakta container

Main tool: [bakta](https://github.com/oschwengers/bakta)
  
Code repository: https://github.com/oschwengers/bakta

Basic information on how to use this tool:
- executable: bakta
- help: -h
- version: -v
- description: Annotates bacterial genomes

> Bakta is a tool for the rapid & standardized annotation of bacterial genomes and plasmids from both isolates and MAGs. It provides dbxref-rich, sORF-including and taxon-independent annotations in machine-readable JSON & bioinformatics standard file formats for automated downstream analysis.

Additional information:

WARNING : Image does not contain a database. 
  
Full documentation: https://github.com/oschwengers/bakta/

## Example Usage

```bash
bakta sample.fasta --db <path to database> --threads 20 --prefix sample
```

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

This image contains the version 5.1 light database. It is located in /db/db-light and set as BAKTA_DB so that --db doesn't have to be used.

Full documentation: https://github.com/oschwengers/bakta/

Example Usage
```bash
bakta sample.fasta --threads 20 --prefix sample 
```

<!-- 
Please edit this readme with some basic information about the tool and how to use this container. 
- Include information about databases and additional files that are included.
- Keep it short - you don't need to recreate the documentation from the creators.
- Do not just copy and paste the readme or help for the tool. 
-->

# skani container

Main tool: [skani](https://github.com/bluenote-1577/skani)
  
Code repository: https://github.com/bluenote-1577/skani

Basic information on how to use this tool:
- executable: skani
- help: -h, --help
- version: -V, --version
- description: skani is a program for calculating average nucleotide identity (ANI) from DNA sequences (contigs/MAGs/genomes) for ANI > ~80%.

Additional information:

This container does not contain any database or reference genome.
  
Full documentation: https://github.com/bluenote-1577/skani/wiki

## Example Usage

Quick ANI calculation:
```bash
skani dist genome1.fa genome2.fa
```
Memory-efficient database search:
```bash
skani sketch genomes/* -o database
skani search -d database query1.fa query2.fa ...
```
All-to-all comparison:
```bash
skani triangle genomes/*
```

  
<!-- Example README
# pasty container

Main tool: [pasty](https://github.com/rpetit3/pasty)

Code repository: https://github.com/rpetit3/pasty

Additional tools:
- ncbi-blast+: 2.12.0
- python: 3.10.6

Basic information on how to use this tool:
- executable: pasty
- help: --help
- version: --version
- description: "A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies"

Additional information:  
  
Full documentation: [https://github.com/rpetit3/pasty](https://github.com/rpetit3/pasty)

## Example Usage

```bash
pasty --assembly /pasty-1.0.2/test/O1-GCF_000504045.fna.gz --prefix O1-GCF_000504045
``` 
-->

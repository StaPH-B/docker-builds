<!-- 
Please edit this readme with some basic information about the tool and how to use this container. 
- Include information about databases and additional files that are included.
- Keep it short - you don't need to recreate the documentation from the creators.
- Do not just copy and paste the readme or help for the tool. 
-->

# isPcr container

Main tool: [isPcr](https://users.soe.ucsc.edu/~kent/)
  
Code repository: https://hgwdev.gi.ucsc.edu/~kent/src/

Basic information on how to use this tool:
- executable: isPcr
- help:
- version:
- description: In-Slico PCR

Additional information:

```
usage:
   isPcr database query output   
where database is a fasta, nib, or twoBit file or a text file containing
a list of these files,  query is a text file file containing three columns: name,
forward primer, and reverse primer,  and output is where the results go.
The names 'stdin' and 'stdout' can be used as file names to make using the
program in pipes easier.
```

## Example Usage

```bash
isPcr template.fa primers.txt output
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

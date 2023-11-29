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

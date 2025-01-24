# kma container

Main tool : [kma](https://bitbucket.org/genomicepidemiology/kma/)

Code repository: https://bitbucket.org/genomicepidemiology/kma/src/master/

Basic information on how to use this tool:
- executable: kma
- help: -h
- version: -v
- description: k-mer mapping of raw reads to a redundant database

Full documentation: https://bitbucket.org/genomicepidemiology/kma/src/master/

## Example Usage

```bash
# Database needs to be indexed to use kma for mapping:
kma index -i templates.fsa.gz -o database/name

# kma mapping of paired and unpaired read files:
kma -ipe SRR13957123_*.fastq.gz -o test.output -t_db DB_name

kma -i singleEndReads.fq.gz -ipe pairedEnd_*.fq.gz -o output/name -t_db database/name -1t1`
```

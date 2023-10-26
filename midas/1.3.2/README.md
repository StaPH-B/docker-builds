# Metagenomic Intra-Species Diversity Analysis System (MIDAS) container

Main tool: [MIDAS](https://github.com/snayfach/MIDAS)

Additional tools:
- samtools v1.4
- bowtie2 v2.4.4
- hmmer v3.3.2
- vsearch v2.21.1

Full documentation: https://github.com/snayfach/MIDAS

## Note
This docker image does not contain reference database. Users should download the default database or create their own.

Default database found here: http://lighthouse.ucsf.edu/MIDAS/midas_db_v1.2.tar.gz

## Example usage
```bash
run_midas.py species /path/to/outdir -1 /path/to/reads_1.fq.gz -2 /path/to/reads_2.fq.gz -d /path/to/midas_database 
```

# sylph container

Main tool : [sylph](https://github.com/bluenote-1577/sylph)

Full documentation: https://github.com/bluenote-1577/sylph/wiki

sylph is a program that can perform ultrafast (1) ANI querying or (2) metagenomic profiling for metagenomic shotgun samples.

## Example Usage

```bash
# all fasta -> one *.syldb; fasta are assumed to be genomes
sylph sketch genome1.fa genome2.fa -o database
#EQUIVALENT: sylph sketch -g genome1.fa genome2.fa -o database

# multi-sample sketching of paired reads
sylph sketch -1 A_1.fq B_1.fq -2 A_2.fq B_2.fq -d output_read_sketch_folder

# multi-sample sketching for single end reads, fastq are assumed to be reads
sylph sketch reads.fq 
#EQUIVALENT: sylph sketch -r reads.fq

# ANI querying 
sylph query database.syldb *.sylsp -t (threads) > ani_queries.tsv

# taxonomic profiling 
sylph profile database.syldb *.sylsp -t (threads) > profiling.tsv
```
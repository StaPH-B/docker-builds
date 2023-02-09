# kma container

### Main tool : kma

kma : k-mer mapping of raw reads to a redundant database


## Example Usage

kma index -i templates.fsa.gz -o database/name

kma -ipe SRR13957123_*.fastq.gz -o test.output -t_db DB_name

kma -i singleEndReads.fq.gz -ipe pairedEnd_*.fq.gz -o output/name -t_db database/name -1t1

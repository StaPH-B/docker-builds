# emmtypingtool docker image

> emmtypingtool: Assign emm type and subtype by querying the CDC M-type specific database

Main tool : [emmtypingtool](https://github.com/phe-bioinformatics/emm-typing-tool)

Additional tools:
- python 2.7.12
- ncbi-blast+ 2.2.31
- bowtie2 2.2.9
- samtools 0.1.19
- emboss 6.6.0
- pyyaml 5.1.2
- numpy 1.16.4
- lxml 4.4.1
- biopython 1.74
- sratoolkit 3.0.2

## Example Usage

```bash
# Running emmtypingtool on /raw_reads directory containing fastq files (.fastq.gz)
emm_typing.py -m /db -i /raw_reads -o /output_directory

# Running emmtypingtool on specified fastq files (sample1)
emm_typing.py -m /db -1 sample1.R1.fastq.gz -2 sample1.R2.fastq.gz -o /output_directory
```

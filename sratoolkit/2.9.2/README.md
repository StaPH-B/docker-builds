# SRA-Toolkit container

Main tool : [SRA-Toolkit](https://github.com/ncbi/sra-tools)

Full documentation: https://hpc.nih.gov/apps/sratoolkit.html

Basically required to download files from the SRA

# Example Usage

```
# downloading paired-end fastq files for SRR4032930
fasterq-dump -A SRR4032930 --split-files
```

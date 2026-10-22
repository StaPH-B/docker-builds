# SeqFu

Main tool: [SeqFu](https://github.com/telatin/seqfu2)
  
Code repository: https://github.com/telatin/seqfu2

Basic information on how to use this tool:
- executable: `seqfu`
- help: `seqfu --help`
- version: `seqfu --version`
- description: | 
> A general-purpose program to manipulate and parse information from FASTA/FASTQ files, supporting gzipped input files. 

  
Full documentation: https://telatin.github.io/seqfu2/


# Testing SeqFU analysis
```
wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz

wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz

seqfu check \
  SRR13957123_1.fastq.gz \
  SRR13957123_2.fastq.gz

seqfu count \
  SRR13957123_1.fastq.gz \
  SRR13957123_2.fastq.gz
```


# SeqFu

Main tool: [SeqFu](https://github.com/telatin/seqfu2)
  
Code repository: https://github.com/telatin/seqfu2

Basic information on how to use this tool:
- executable: |
```
  · count [cnt]         : count FASTA/FASTQ reads, pair-end aware
  · deinterleave [dei]  : deinterleave FASTQ
  · derep [der]         : feature-rich dereplication of FASTA/FASTQ files
  · interleave [ilv]    : interleave FASTQ pair ends
  · lanes [mrl]         : merge Illumina lanes
  · list [lst]          : print sequences from a list of names
  · metadata [met]      : print a table of FASTQ reads (mapping files)
  · sort [srt]          : sort sequences by size (uniques)
  · stats [st]          : statistics on sequence lengths

  · cat                 : concatenate FASTA/FASTQ files
  · grep                : select sequences with patterns
  · head                : print first sequences
  · rc                  : reverse complement strings or files
  · tab                 : tabulate reads to TSV (and viceversa)
  · tail                : view last sequences
  · view                : view sequences with colored quality and oligo matches
```

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
  -f SRR13957123_1.fastq.gz \
  -r SRR13957123_2.fastq.gz
```


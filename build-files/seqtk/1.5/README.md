# seqtk container

Main tool: [seqtk](https://github.com/lh3/seqtk)
  
Code repository: https://github.com/lh3/seqtk

Basic information on how to use this tool:
- executable: seqtk
- help: N/A
- version: N/A
- description: Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format.


Full documentation: https://github.com/lh3/seqtk

## Example Usage

```bash
# Convert FASTQ to FASTA:
seqtk seq -a in.fq.gz > out.fa

# Reverse complement FASTA/Q:
seqtk seq -r in.fq > out.fq

# Extract sequences in regions contained in file reg.bed:
seqtk subseq in.fa reg.bed > out.fa

# Mask regions in reg.bed to lowercases:
seqtk seq -M reg.bed in.fa > out.fa
# Subsample 10000 read pairs from two large paired FASTQ files (remember to use the same random seed to keep pairing):
seqtk sample -s100 read1.fq 10000 > sub1.fq
seqtk sample -s100 read2.fq 10000 > sub2.fq

# Trim low-quality bases from both ends using the Phred algorithm:
seqtk trimfq in.fq > out.fq
```

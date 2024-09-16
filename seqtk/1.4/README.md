# seqtk container

Main tool: [seqtk](https://github.com/lh3/seqtk)
  
Code repository: https://github.com/lh3/seqtk

Basic information on how to use this tool:
- executable: seqtk
- help: N/A
- version: N/A
- description: Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format.


seqtk has several different subcomands which are listed below
```

Usage:   seqtk <command> <arguments>
Version: 1.4-r122

Command: seq       common transformation of FASTA/Q
         size      report the number sequences and bases
         comp      get the nucleotide composition of FASTA/Q
         sample    subsample sequences
         subseq    extract subsequences from FASTA/Q
         fqchk     fastq QC (base/quality summary)
         mergepe   interleave two PE FASTA/Q files
         split     split one file into multiple smaller files
         trimfq    trim FASTQ using the Phred algorithm

         hety      regional heterozygosity
         gc        identify high- or low-GC regions
         mutfa     point mutate FASTA at specified positions
         mergefa   merge two FASTA/Q files
         famask    apply a X-coded FASTA to a source FASTA
         dropse    drop unpaired from interleaved PE FASTA/Q
         rename    rename sequence names
         randbase  choose a random base from hets
         cutN      cut sequence at long N
         gap       get the gap locations
         listhet   extract the position of each het
         hpc       homopolyer-compressed sequence
         telo      identify telomere repeats in asm or long reads

```


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
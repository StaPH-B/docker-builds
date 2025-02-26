# Trimmomatic

This image implements the read-trimming software [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic).
Documentation is available at http://www.usadellab.org/cms/?page=trimmomatic. 

## Example usage
This example useage is taken from the built-in tests for this image. See [test_trimmomatic.sh](test_trimmomatic.sh).

```bash
# Get input data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Use adaptor file that comes with the software
ADAPTERS="/Trimmomatic-0.39/adapters/TruSeq3-PE.fa"  # trimmomatic docs says these are used in HiSeq and MiSeq machines

# Run trimmomatic to trim & filter reads
trimmomatic \
  PE \
  -phred33 \
  R1.fastq.gz R2.fastq.gz \
  R1.paired.fq R1.unpaired.fq \
  R2.paired.fq R2.unpaired.fq \
  ILLUMINACLIP:$ADAPTERS:2:20:10:8:TRUE \
  SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50
```

## Example output 

The on-screen output tells you what trimmomatic did and how many reads got filtered out:
```
TrimmomaticPE: Started with arguments:
 -phred33 R1.fastq.gz R2.fastq.gz R1.paired.fq R1.unpaired.fq R2.paired.fq R2.unpaired.fq ILLUMINACLIP:/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:20:10:8:TRUE SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50
Multiple cores found: Using 2 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 50000 Both Surviving: 37667 (75.33%) Forward Only Surviving: 6949 (13.90%) Reverse Only Surviving: 4543 (9.09%) Dropped: 841 (1.68%)
TrimmomaticPE: Completed successfully
```

The result files from this command are:
```
R1.paired.fq
R1.unpaired.fq
R2.paired.fq
R2.unpaired.fq
```

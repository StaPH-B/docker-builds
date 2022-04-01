# Trimmomatic

This image implements the read-trimming software [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic).
Documentation is available at http://www.usadellab.org/cms/?page=trimmomatic. 

## Example usage
This example useage is taken from the built-in tests for this image. See [run_trimmomatic_pos_control.sh](tests/scripts/run_trimmomatic_pos_control.sh).

```bash
# Input data are paired-end reads
R1=/data/R1.fastq.gz
R2=/data/R2.fastq.gz

# Set up an output directory
OUTDIR=/test_result
mkdir -p $OUTDIR

# Use adaptor file that comes with the software
ADAPTERS="/Trimmomatic-0.39/adapters/TruSeq3-PE.fa"  # trimmomatic docs says these are used in HiSeq and MiSeq machines

# Run trimmomatic to trim & filter reads
trimmomatic \
  PE \
  -phred33 \
  $R1 $R2 \
  $OUTDIR/R1.paired.fq $OUTDIR/R1.unpaired.fq \
  $OUTDIR/R2.paired.fq $OUTDIR/R2.unpaired.fq \
  ILLUMINACLIP:$ADAPTERS:2:20:10:8:TRUE \
  SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50
```

## Example output 

The on-screen output tells you what trimmomatic did and how many reads got filtered out:
```
TrimmomaticPE: Started with arguments:
-phred33 /data/R1.fastq.gz /data/R2.fastq.gz /test_result/R1.paired.fq /test_result/R1.unpaired.fq /test_result/R2.paired.fq /test_result/R2.unpaired.fq ILLUMINACLIP:/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:20:10:8:TRUE SLIDINGWINDOW:6:30 LEADING:10 TRAILING:10 MINLEN:50
Multiple cores found: Using 2 threads
Using PrefixPair: 'TACACTCTTTCCCTACACGACGCTCTTCCGATCT' and 'GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT'
ILLUMINACLIP: Using 1 prefix pairs, 0 forward/reverse sequences, 0 forward only sequences, 0 reverse only sequences
Input Read Pairs: 830228 Both Surviving: 526702 (63.44%) Forward Only Surviving: 109472 (13.19%) Reverse Only Surviving: 48718 (5.87%) Dropped: 145336 (17.51%)
TrimmomaticPE: Completed successfully
```

The result files from this command are:
```
R1.paired.fq
R1.unpaired.fq
R2.paired.fq
R2.unpaired.fq
```

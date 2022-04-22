# BWA

This image implements the Burrows-Wheeler alignment tool for short-read alignment [BWA](https://github.com/lh3/bwa).
Documentation is available at http://bio-bwa.sourceforge.net/bwa.shtml. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz -O R2.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/genome/MN908947.3/GCA_009858895.3_ASM985889v3_genomic.200409.fna.gz -O reference.fna.gz
gunzip reference.fna.gz

# Construct the FM-index for the reference assembly
bwa index reference.fna 

# Align paired-end reads to an assembly with option -v: output errors and warnings
bwa mem \
  -v 2 \
  reference.fna \
  R1.fastq.gz R2.fastq.gz \
  > test.sam
```

## Example output

The on-screen output tells you what the program did:
```
[bwa_index] Pack FASTA... 0.00 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 0.01 seconds elapse.
[bwa_index] Update BWT... 0.00 sec
[bwa_index] Pack forward-only FASTA... 0.00 sec
[bwa_index] Construct SA from BWT and Occ... 0.00 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index reference.fna
[main] Real time: 0.030 sec; CPU: 0.013 sec
[M::mem_pestat] analyzing insert size distribution for orientation FF...
[M::mem_pestat] (25, 50, 75) percentile: (629, 1546, 3485)
[M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 9197)
[M::mem_pestat] mean and std.dev: (2189.17, 2242.87)
[M::mem_pestat] low and high boundaries for proper pairs: (1, 12053)
[M::mem_pestat] analyzing insert size distribution for orientation FR...
[M::mem_pestat] (25, 50, 75) percentile: (212, 270, 338)
[M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 590)
[M::mem_pestat] mean and std.dev: (278.82, 93.04)
[M::mem_pestat] low and high boundaries for proper pairs: (1, 716)
[M::mem_pestat] skip orientation RF as there are not enough pairs
[M::mem_pestat] analyzing insert size distribution for orientation RR...
[M::mem_pestat] (25, 50, 75) percentile: (821, 3663, 6038)
[M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 16472)
[M::mem_pestat] mean and std.dev: (3951.79, 3043.12)
[M::mem_pestat] low and high boundaries for proper pairs: (1, 21689)
[M::mem_pestat] skip orientation FF
[M::mem_pestat] skip orientation RR
[main] Version: 0.7.17-r1188
[main] CMD: bwa mem -v 2 reference.fna R1.fastq.gz R2.fastq.gz
[main] Real time: 0.889 sec; CPU: 0.880 sec

The command outputs several files, including:
```
test.sam  # sequence alignment and map file
```

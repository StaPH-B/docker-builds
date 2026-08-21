# Rasusa container

Main tool: [Rasusa](https://github.com/mbhall88/rasusa)

Additional tools:
- none

Full documentation: https://github.com/mbhall88/rasusa

Randomly subsample sequencing reads or alignments to a specified coverage or target size.

### Key Usage Notes
* `rasusa` supports two main subcommands: `reads` (for FASTQ/FASTA/unaligned BAM/CRAM) and `aln` (for aligned BAM/SAM/CRAM).
* For `reads`, subsampling requires **one** of the following target metrics:
  * Coverage: `-c, --coverage` (requires `-g, --genome-size`)
  * Target bases: `-b, --bases`
  * Exact number of reads/pairs: `-n, --num`
  * Fraction of reads: `-f, --frac` or `-p, --probability`
* For `aln`, `-c, --coverage` is required to target a maximum per-position alignment depth.
* Input:
  * `reads`: FASTA, FASTQ, or unaligned SAM/BAM/CRAM (optionally compressed with gzip, bzip2, xz, or zstd). Accepts two input files for paired-end Illumina reads.
  * `aln`: Coordinate-sorted SAM, BAM, or CRAM file.

---

## Example Usage

```bash
# SARS-CoV-2 example, paired-end Illumina (subsample to specific number of read pairs)
rasusa reads \
       -n 40434 \
       -s 1 \
       -o SRR13957123_downsampled_1.fastq.gz \
       -o SRR13957123_downsampled_2.fastq.gz \
       SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz

# Salmonella enterica example, paired-end Illumina (subsample to 100x coverage given 5Mb genome size)
rasusa reads \
       --coverage 100 \
       --genome-size 5M \
       -s 1 \
       -o SRR10992628_downsampled_1.fastq.gz \
       -o SRR10992628_downsampled_2.fastq.gz \
       SRR10992628_1.fastq.gz SRR10992628_2.fastq.gz

# Fast 1-pass streaming subsampling to 10% of total reads
rasusa reads \
       -p 0.1 \
       -s 1 \
       -o sample_0.1_1.fq.gz \
       -o sample_0.1_2.fq.gz \
       reads_1.fq.gz reads_2.fq.gz

# Alignment subsampling to maximum 30x depth (stream strategy)
rasusa aln \
       --coverage 30 \
       -s 1 \
       aligned_reads.bam | samtools sort -o downsampled_30x.bam
```
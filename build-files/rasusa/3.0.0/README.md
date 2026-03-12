# Rasusa container

Main tool : [Rasusa](https://github.com/mbhall88/rasusa)

Additional tools:

- none

Full documentation: https://github.com/mbhall88/rasusa

Randomly subsample sequencing reads to a specified coverage.

Note that rasusa requires certain parameters:
* `-c`, `--coverage`, which can be supplemented by (`-b`, `--bases`), (`-n`, `--num`), and (`-f`, `--frac`) in `reads`, but is required for `aln`
* `-g`, `--genome-size`, which can be supplemented by (`-b`, `--bases`), (`-n`, `--num`), and (`-f`, `--frac`) in `reads`, and is not an argument for `aln`.
* input
    * Valid FASTA or FASTQ format for the `reads` command 
    * Valid coordinate-sorted SAM/BAM/CRAM for the `aln` command
    * Can be compressed via gzip
    * If 2 inputs are passed to `reads`, it is assumed they are paired-end reads.

Note:
Version 3.0.0 introduces a major change from versions < 3.0.0.
* deps: Subsampling results for a fixed seed will differ from versions < 3.0.0. This is caused by internal algorithmic changes in the rand crate (0.8.5 -> 0.10.0) and requires a major version bump.

## Example Usage

```bash
# sars-cov-2 example, paired-end illumina
rasusa reads \
       -n 40434 \          # downsample to specific number of reads per FASTQ file
       -s 1 \              # set seed 
       -O g \              # set output file compression format as gzip
       -o SRR13957123_downsampled_1.fastq.gz -o SRR13957123_downsampled_2.fastq.gz \
       SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz

# Salmonella enterica example, paired-end illumina
rasusa reads \
       --coverage 100 \    # use 100X coverage for downsampling
       --genome-size 5M \  # downsample to specific coverage based on genome size (5 million bases)
       -s 1 \              # set seed 
       -O g \              # set output file compression format as gzip
       -o SRR10992628_downsampled_1.fastq.gz -o SRR10992628_downsampled_2.fastq.gz \
       SRR10992628_1.fastq.gz SRR10992628_2.fastq.gz 
```

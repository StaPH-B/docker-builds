# Rasusa container

Main tool : [Rasusa](https://github.com/mbhall88/rasusa)

Additional tools:

- none

Full documentation: https://github.com/mbhall88/rasusa

Randomly subsample sequencing reads to a specified coverage

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

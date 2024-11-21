# hostile

Main tool: [hostile](https://github.com/bede/hostile)
  
Code repository: https://github.com/bede/hostile

Basic information on how to use this tool:
- executable: |
```
usage: hostile [-h] [--version] {clean,mask,fetch} ...

positional arguments:
  {clean,mask,fetch}
    clean             Remove reads aligning to an index from fastq[.gz] input files
    mask              Mask reference genome against target genome(s)
    fetch             Download and cache indexes from object storage for use with hostile clean

options:
  -h, --help          show this help message and exit
  --version           show program's version number and exit
```

- help: `hostile --help`
- version: `hostle --version`
- description: | 
> Hostile accurately removes host sequences from short and long read (meta)genomes, consuming single-read or paired fastq input.

  
Full documentation: https://github.com/bede/hostile


# Testing hostile analysis
```
# Downloading test dataset
wget https://github.com/bacterial-genomics/test-datasets/raw/assembly/test_data/test_miniburk_R1.fastq.gz --no-check-certificate
wget https://github.com/bacterial-genomics/test-datasets/raw/assembly/test_data/test_miniburk_R2.fastq.gz --no-check-certificate

# Running hostile clean on test dataset
hostile clean --index /data/test/sars-cov-2/sars-cov-2 --fastq1 test_miniburk_R1.fastq.gz --fastq2 test_miniburk_R2.fastq.gz
```
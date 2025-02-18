# hostile

Main tool: [hostile](https://github.com/bede/hostile)
  
Code repository: https://github.com/bede/hostile

Basic information on how to use this tool:
- executable: hostile
- help:--help
- version: --version
- description: | 
> Hostile accurately removes host sequences from short and long read (meta)genomes, consuming single-read or paired fastq input.

  
Full documentation: https://github.com/bede/hostile

All hostile test files and references are included at /hostile/tests


# Testing hostile analysis
```
# Downloading test dataset
wget https://github.com/bacterial-genomics/test-datasets/raw/assembly/test_data/test_miniburk_R1.fastq.gz --no-check-certificate
wget https://github.com/bacterial-genomics/test-datasets/raw/assembly/test_data/test_miniburk_R2.fastq.gz --no-check-certificate

# Running hostile clean on test dataset
hostile clean --index /hostile/test/sars-cov-2/sars-cov-2 --fastq1 test_miniburk_R1.fastq.gz --fastq2 test_miniburk_R2.fastq.gz
```
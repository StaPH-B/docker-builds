# KRAKEN2-beta container

Main tool : [KRAKEN2](https://ccb.jhu.edu/software/kraken2/)

It comes bundled with a database containing viral (including SARS-CoV-2) and human sequences downloaded from https://storage.googleapis.com/sars-cov-2/kraken2_h%2Bv_20200319.tar.gz.

# Example Usage

```
kraken2 --paired \
      --classified-out cseqs#.fq \
      --threads 48 \
      --db /kraken2-db \
      clean.R1.fastq clean.R2.fastq \
      --report kraken2_report.txt 
```

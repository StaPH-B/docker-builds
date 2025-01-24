# KRAKEN2-beta container

Main tool : [KRAKEN2](https://ccb.jhu.edu/software/kraken2/)

It comes bundled with a database containing viral (including SARS-CoV-2) and human sequences downloaded from https://storage.googleapis.com/sars-cov-2/kraken2_h%2Bv_20200319.tar.gz.

Since it comes bundled with a large database, singularity may have issues pulling this container. As a workaround, consider the `--sandbox` option or specifying a new temporary directory for the download (i.e. `export SINGULARITY_TMPDIR=/scratch`).

You can see what taxa are in the database by looking at `Taxa_in_DB.txt` file. 

# Example Usage

```
kraken2 --paired \
      --classified-out cseqs#.fq \
      --threads 48 \
      --db /kraken2-db \
      clean.R1.fastq clean.R2.fastq \
      --report kraken2_report.txt 
```

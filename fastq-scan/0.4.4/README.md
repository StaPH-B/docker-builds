# fastq-scan container

Main tool: [fastq-scan](https://github.com/rpetit3/fastq-scan)

Additional tools:
- CLI json parser [jq](https://stedolan.github.io/jq/)

Full documentation: https://github.com/rpetit3/fastq-scan

> fastq-scan reads a FASTQ from STDIN and outputs summary statistics (read lengths, per-read qualities, per-base qualities) in JSON format.

# Example Usage
Example stats for a uncompressed FASTQ:
```
cat /fastq-scan/example.fq | fastq-scan
```

Example stats for a compressed (gzip) FASTQ:
```
zcat /data/SRX0000000_R1.fastq.gz | fastq-scan"
```

Example using jq to extract the total number of reads in the FASTQ:
```
cat /fastq-scan/example.fq | fastq-scan | jq .qc_stats.read_total"
```

View full fastq-scan help options:
```
fastq-scan -h
````

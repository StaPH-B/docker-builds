# fastqc docker image

Main tool & documentation: [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

Source code: [https://github.com/s-andrews/FastQC/](https://github.com/s-andrews/FastQC)

Additional tools:

- perl 5.30.0
- java (openjdk 11.0.18)

> A tool designed to do provide some simple quality control checks on high throughput sequence data.

## Example usage

Example stats for a compressed (gzip) FASTQ:

```bash
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastqc:latest fastqc /data/SRX0000000_R1.fastq.gz
```

Output will be a QC report (`.html` and `.zip`).

View full fastqc help options:

```bash
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastqc:latest fastqc -h
```

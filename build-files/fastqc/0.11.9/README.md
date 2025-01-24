# fastqc 0.11.9 docker image

Main tool: [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

Full documentation: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

Source code: https://github.com/s-andrews/FastQC

> A tool designed to do provide some simple quality control checks on high throughput sequence data.

This docker image runs FASTQC on an input '.fastq.gz' file.

## Example usage

Example stats for a compressed (gzip) FASTQ: `$ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastqc:0.11.9 fastqc /data/SRX0000000_R1.fastq.gz`

Output will be a QC report (.html and .zip).

View full fastqc help options: `$ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastqc:0.11.9 fastqc -h `

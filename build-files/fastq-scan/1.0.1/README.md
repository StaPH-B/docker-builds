# fastq-scan 1.0.1 docker image

Main tool: [fastq-scan](https://github.com/rpetit3/fastq-scan)

In addition to fastq-scan, this docker image contains the CLI json parser [jq](https://stedolan.github.io/jq/)

## Example commands

Example stats for a uncompressed FASTQ: `$ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastq-scan:1.0.0 /bin/bash -c "cat /fastq-scan/example.fq | fastq-scan"`

Example stats for a compressed (gzip) FASTQ: `$ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastq-scan:1.0.0 /bin/bash -c "zcat /data/SRX0000000_R1.fastq.gz | fastq-scan"`

Eaxmple using jq to extract the total number of reads in the FASTQ: `$ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data fastq-scan:1.0.0 /bin/bash -c "cat /fastq-scan/example.fq | fastq-scan | jq .qc_stats.read_total"`

View full fastq-scan help options: `$ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastq-scan:1.0.0 fastq-scan -h `

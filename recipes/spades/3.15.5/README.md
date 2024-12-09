# SPAdes

Main tool: [SPAdes](https://github.com/ablab/spades)

SPAdes genome assembler

Additional tools:

* python 3.8.10

## Example commands

```bash
# Test with supplied E. coli data
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/spades:latest spades.py --test

# paired-end Illumina reads are in the $PWD
$ ls 
SRR7062227_1.fastq.gz  SRR7062227_2.fastq.gz

# assemble with your own data (broken into two lines for readability)
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/spades:latest \
  spades.py -1 /data/SRR7062227_1.fastq.gz -2 /data/SRR7062227_2.fastq.gz -t 8 --isolate -o /data/SRR7062227-spades-output/
```

View full `spades` help options: `docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/spades:latest spades.py --help`

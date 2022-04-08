# SeqSero2 container

Main tool : [SeqSero2](https://github.com/denglab/SeqSero2)

Additional tools:
- samtools
- salmID
- SPAdes
- bedtools
- sra-toolkit
- bwa
- ncbi-blast+

Full documentation: https://github.com/denglab/SeqSero2

Salmonella serotyping from genome sequencing data

# Example Usage

```
# paired-end reads
SeqSero2_package.py -t 2 -m a -b mem -i sample_R1.fastq.gz sample_R2.fastq.gz -p 4 -d seqsero2/sample -n sample

# assembled reads
SeqSero2_package.py -t 4 -m k -i sample.fasta -p 4 -d seqsero2/sample -n sample
```

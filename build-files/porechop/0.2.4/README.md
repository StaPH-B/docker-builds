# porechop container

Main tool : [porechop](https://github.com/rrwick/Porechop)

Additional tools:
- python3 3.10.6

Full documentation: https://github.com/rrwick/Porechop

> Porechop is a tool for finding and removing adapters from Oxford Nanopore reads. Adapters on the ends of reads are trimmed off, and when a read has an adapter in its middle, it is treated as chimeric and chopped into separate reads. Porechop performs thorough alignments to effectively find adapters, even at low sequence identity.

As of October 2019, porechop is unsupported, but is still useful in many settings, including removing adapters.

## Example Usage

```bash
porechop -i input_reads.fastq.gz -o output_reads.fastq.gz
```

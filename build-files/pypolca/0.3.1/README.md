# pypolca container

Main tool: [pypolca](https://github.com/gbouras13/pypolca)
  
Code repository:

Additional tools:
- samtools: 1.19
- vcftools: 0.1.16
- bwa: 0.7.17-r1188
- freebayes: 1.3.7

Basic information on how to use this tool:
- executable: pypolca
- help: pypolca -h
- version: pypolca -v
- description: Polished long-read assemblies with Illumina reads

> pypolca is a Standalone Python re-implementation of the POLCA polisher from the MaSuRCA genome assembly and analysis toolkit.
  
Full documentation: [https://github.com/rrwick/Polypolish](https://github.com/rrwick/Polypolish)

## Example Usage

```bash
pypolca run -a assembly.fasta -1 R1.fastq.gz -2 R2.fastq.gz -t 4 -o output 
```

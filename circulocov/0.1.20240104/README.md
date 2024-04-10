# CirculoCov container

Main tool: [CirculoCov](https://github.com/erinyoung/CirculoCov/)
  
Code repository:https://github.com/erinyoung/CirculoCov

Additional tools:
- minimap2: 2.26

Basic information on how to use this tool:
- executable: circulocov
- help: --help
- version: --version
- description: Coverage estimates and visualization for circular sequences.
  
Full documentation: https://github.com/erinyoung/CirculoCov/

## Example Usage

```bash
# getting coverage without visuals
circulocov -g assembly.fa -i illumina_1.fastq.gz illumina_2.fastq.gz -n nanopore.fastq.gz -p pacbio.fastq.gz -o out

# getting coverage visuals and mapped fastq files
circulocov -g assembly.fa -i illumina_1.fastq.gz illumina_2.fastq.gz -n nanopore.fastq.gz -p pacbio.fastq.gz -o out_all -a
```

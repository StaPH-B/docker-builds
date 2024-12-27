# el_gato container

Main tool: [el_gato](https://github.com/appliedbinf/el_gato)
  
Code repository: https://github.com/appliedbinf/el_gato

Additional tools:
- minimap2: 2.24-r1122
- samtools: 1.13
- ncbi-blast+: 2.12.0+
- isPCR: v33x2

Basic information on how to use this tool:
- executable: el_gato.py
- help: -h
- version: -v
- description: Epidemiology of Legionella : Genome-bAsed Typing

Additional information:

Container contains necessary database of Legionella sequence types
  
Full documentation: https://github.com/appliedbinf/el_gato

## Example Usage

```bash
# Paired-end:
el_gato.py --read1 read1.fastq.gz --read2 read2.fastq.gz --out output_folder/

# Assembly:
el_gato.py --assembly assembly_file.fna --out output_folder/
```
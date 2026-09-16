# myloasm container

Main tool: [myloasm](https://myloasm-docs.github.io/)
  
Code repository: https://github.com/bluenote-1577/myloasm

Additional tools:
- none

Basic information on how to use this tool:
- executable: `myloasm`
- help: `-h`, `--help`
- version: `-V`, `--version`
- description: Myloasm is a de novo metagenome assembler for long-read sequencing data

Additional information:
  
Full documentation: https://myloasm-docs.github.io/

## Example Usage

```bash
# Nanopore R10.4 (sup/hac basecalling)
myloasm reads1.fq reads2.fq reads3.fq -o output_directory -t 50

# PacBio HiFi
myloasm reads1.fq reads2.fq reads3.fq -o output_directory -t 50 --hifi
```

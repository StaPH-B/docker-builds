# Circlator container

Main tool : [circlator](https://sanger-pathogens.github.io/circlator/)

Additional tools:

- bwa version 0.7.17
- canu version 2.0
- nucmer version 3.1
- perl 5.34.0
- prodigal 2.6.3 (Feb, 2016)
- python 3.10.6
- samtools version 1.16.1
- spades 3.13.1

Full documentation: https://github.com/sanger-pathogens/circlator/wiki

Circlator is a genome assembly workflow, but is more commonly used for its fixstart feature - which will rotate input sequences to start with dnaA if found.

## Example Usage

```bash
circlator fixstart input.fasta output
```

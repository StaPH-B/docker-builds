# Smalt Container

## Documentation and Overview

Main Tool: [SMALT – A new mapper for DNA sequencing reads](https://www.researchgate.net/publication/266155341_SMALT_-_A_new_mapper_for_DNA_sequencing_reads)

Full documentation: https://www.sanger.ac.uk/tool/smalt-0/ 

SMALT aligns DNA sequencing reads with a reference genome.

This cointainer also contains samtools=1.15 as this was needed for a particular workflow. Also, bambamc=0.0.50 was added which allows passing of bam files to smalt see [documentation](https://sourceforge.net/projects/smalt/files/).

```
              SMALT - Sequence Mapping and Alignment Tool
                             (version: 0.7.6)
SYNOPSIS:
    smalt <task> [TASK_OPTIONS] [<index_name> <file_name_A> [<file_name_B>]]

Available tasks:
    smalt check   - checks FASTA/FASTQ input
    smalt help    - prints a brief summary of this software
    smalt index   - builds an index of k-mer words for the reference
    smalt map     - maps single or paired reads onto the reference
    smalt sample  - sample insert sizes for paired reads
    smalt version - prints version information

Help on individual tasks:
    smalt <task> -H
```

## Example Usage

```
smalt index -k 13 -s 6 PhiX174 GCF_000819615.1_ViralProj14015_genomic.fastq
```

The output of this line are `PhiX174.sma` and `PhiX174.smi`. These are found in the `tests` directory and are included for testing the docker container during building and aren't needed to run smalt. 

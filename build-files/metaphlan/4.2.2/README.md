# MetaPhlAn container

Main tool: [MetaPhlAn](https://github.com/biobakery/biobakery/wiki/metaphlan4)
  
Code repository: https://github.com/biobakery/MetaPhlAn

Basic information on how to use this tool:
- executable: metaphlan
- help: -h
- version: -v
- description: MetaPhlAn is a computational tool for species-level microbial profiling (bacteria, archaea, eukaryotes, and viruses) from metagenomic shotgun sequencing data. StrainPhlAn (available within MetaPhlAn) allows strain-level microbial population genomics.

Additional information:

Warning: running MetaPhlAn 4 requires a minimum of 25GB of memory or more.

The database can be downloaded from [Segatalab FTP](http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/) or via metaphlan with the following command:

```metaphlan --install```

Full documentation: https://github.com/biobakery/biobakery/wiki/metaphlan4

## Example Usage

```bash
metaphlan metagenome.fastq --input_type fastq -o profiled_metagenome.txt
```

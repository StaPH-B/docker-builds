# MetaPhlAn container

Main tool: [MetaPhlAn](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4.1)
  
Code repository: https://github.com/biobakery/MetaPhlAn

Basic information on how to use this tool:
- executable: metaphlan
- help: -h
- version: -v
- description: MetaPhlAn is a computational tool for species-level microbial profiling (bacteria, archaea, eukaryotes, and viruses) from metagenomic shotgun sequencing data. StrainPhlAn (available within MetaPhlAn) allows strain-level microbial population genomics.

Additional information:

The MetaPhlAn 4 database has been substantially increased (~21GB) in comparison with the previous 3.1 version. Thus, for running MetaPhlAn 4, a minimum of 25GB or memory is needed.
The database can be downloaded from [Segatalab FTP](http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/) or via metaphlan with the following command:

```metaphlan --install```

Full documentation: https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4.1

## Example Usage

```bash
metaphlan metagenome.fastq --input_type fastq -o profiled_metagenome.txt
```
# StaphSCAN container

Main tool: [StaphSCAN](https://github.com/riccabolla/StaphSCAN)
  
Code repository: https://github.com/riccabolla/StaphSCAN

Additional tools:
- Python: 3.13
- Mash: 2.3
- Blast: 2.17.0

Additional libraries:
- Biopython>=1.78
- Pandas
- Rauth
- Requests

Basic information on how to use this tool:
- executable: staphscan
- help: `-h`, `--help`
- version: `--version`
- description: A genome-based tool for Surveillance through Comprehensive Analysis and staNdardized reporting of Staphylococcus aureus.

Additional information:

Bollini, R., Cento, V. StaphSCAN: a genomic surveillance framework for Staphylococcus aureus. BMC Genomics (2026). https://doi.org/10.1186/s12864-026-13165-0

Available StaphScan Modules:
- agr
- assembly
- biofilm
- capsule
- mlst
- resistance
- sccmec
- spa
- virulence

For MLST database updates, please select this [link](https://staphscan.readthedocs.io/en/latest/installation/#mlst-database-update). It has details on registering for PubMLST, generating an API key, and the commands needed to update the MLST databases. Custom MLST database directories can also be specified with `--db_mlst`.

Full documentation: https://staphscan.readthedocs.io/en/latest/

## Example Usage
This command generates a StaphSCAN report (.tsv) for all *.fasta* files in the output directory *staphscan_output*.
```bash
staphscan -i *.fasta -o staphscan_output -m mlst,spa
```

All modules are run by default, but can be specified by comma-delimiting module names under the `-m` flag.
```bash
staphscan -i *.fasta -o staphscan_output -m mlst,spa
```

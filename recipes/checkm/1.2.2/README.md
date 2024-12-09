# CheckM container

Main tool: [CheckM](https://github.com/Ecogenomics/CheckM)
  
Code repository: https://github.com/Ecogenomics/CheckM

Additional tools:
- HHMER: 3.3.2
- prodigal: 2.6.3
- pplacer: 1.1.alpha19-0-g807f6f3

Basic information on how to use this tool:
- executable: checkm
- help: <-h>
- version: <-h>
- description: CheckM provides a set of tools for assessing the quality of genomes recovered from isolates, single cells, or metagenomes.

Additional information:

This container does not include precalculated data files that CheckM relies on</br>
Those files can be downloaded from either:
- https://data.ace.uq.edu.au/public/CheckM_databases
- https://zenodo.org/record/7401545#.Y44ymHbMJD8

The reference data must be decompress into a directory. Inform CheckM of where the files have been placed with the following command:
```
checkm data setRoot <checkm_database_dir>
```

Full documentation: https://github.com/Ecogenomics/CheckM/wiki

## Example Usage

```bash
checkm lineage_wf -t 8 -x fasta input_folder output_folder
```

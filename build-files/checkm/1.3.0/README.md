# CheckM container

Main tool: [CheckM](https://github.com/Ecogenomics/CheckM)
  
Code repository: https://github.com/Ecogenomics/CheckM

Additional tools:
- HHMER: 3.3.2+dfsg-1
- prodigal: 1:2.6.3-5

<details>

<summary>Additional tools installed via pip:</summary>

```
Package         Version
--------------- -------
backports.zstd  1.8.0
checkm-genome   1.3.0
contourpy       1.4.0
cycler          0.12.1
DendroPy        5.1.3
fonttools       4.68.0
gtdb-gplace     0.1.1
isal            1.9.1
kiwisolver      1.5.1
matplotlib      3.11.2
numpy           2.5.5
packaging       26.3
pillow          13.0.0
pip             24.0
pyparsing       3.3.3
pysam           0.24.1
python-dateutil 4.0.0
scipy           1.18.1
setuptools      84.2.1
tqdm            4.70.1
tzdata          2026.6
wheel           0.42.0
xopen           2.1.0
zlib-ng         1.1.0
```

</details>

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

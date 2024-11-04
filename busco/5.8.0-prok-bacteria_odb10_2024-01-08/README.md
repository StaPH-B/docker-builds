# Assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs (BUSCO) container

Main tool : [BUSCO](https://gitlab.com/ezlab/busco/)

Additional tools:
- BBTools 39.10
- HMMER 3.3.2
- Prodigal 2.6.3
- SEPP 4.5.5
- Python 3.10.12
- BioPython 1.83
- Perl 5.34.0
- OpenJDK 1.8.0_422

Full documentation: https://busco.ezlab.org/busco_userguide.html

This is a BUSCO docker image which has basic functions for prokaryotes only. This image contains bacteria_odb10 lineage dataset for offline use.
## Example Usage
```bash
# offline usage with bacteria lineage
busco --offline -i assembly.fasta -l /busco_downloads/lineages/bacteria_odb10 -o output -m genome
# auto lineage selection
busco -i assembly.fasta -o output -m genome --auto-lineage-prok
```

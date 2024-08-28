# Assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs (BUSCO) container

Main tool : [BUSCO](https://gitlab.com/ezlab/busco/)

Additional tools:
- BBTools 39.06
- HMMER 3.3
- Prodigal 2.6.3
- SEPP 4.5.1
- Python 3.8.10
- BioPython 1.83
- Perl 5.30.0
- OpenJDK 1.8.0_392

Full documentation: https://busco.ezlab.org/busco_userguide.html

This is a BUSCO docker image which has basic functions for prokaryotes only. This image contains bacteria_odb10 lineage dataset for offline use.
## Example Usage
```bash
# offline usage with bacteria lineage
busco --offline -i assembly.fasta -l /busco_downloads/lineages/bacteria_odb10 -o output -m genome
# auto lineage selection
busco -i assembly.fasta -o output -m genome --auto-lineage-prok
```

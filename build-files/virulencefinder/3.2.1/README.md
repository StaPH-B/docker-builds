# VirulenceFinder Docker Image

A docker image  that contains VirulenceFinder, a tool for identifying virulence factors in E. coli, Enterococcus, S. aureus, and Listeria isolates from reads or assemblies

Main tool:

- Main Code Repo: [https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/](https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/)
- VirulenceFinder database: [https://bitbucket.org/genomicepidemiology/virulencefinder_db/src/master/](https://bitbucket.org/genomicepidemiology/virulencefinder_db/src/master/)
- You may be familiar with the web version of VirulenceFinder: [https://cge.food.dtu.dk/services/VirulenceFinder/](https://cge.food.dtu.dk/services/VirulenceFinder/)

Additional tools:

- [kma](https://bitbucket.org/genomicepidemiology/kma/src/master/) version 1.5.2


Database version: 4ad9c8dd6eb4adedc99c03f46796e5f5c225b004 (after 2.0.1) made on 2025-07-04

## Usage

```bash
python -m virulencefinder -ifq sample_1.fastq.gz sample_2.fastq.gz --extended_output -o outdir
```

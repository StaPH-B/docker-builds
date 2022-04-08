# staramr container

Main tool : [staramr](https://github.com/phac-nml/staramr)

Additional tools:
- blast
- any2fasta
- mlst

Full documentation: https://github.com/phac-nml/staramr

> staramr (*AMR) scans bacterial genome contigs against the ResFinder, PointFinder, and PlasmidFinder databases (used by the ResFinder webservice and other webservices offered by the Center for Genomic Epidemiology) and compiles a summary report of detected antimicrobial resistance genes.

# Example Usage

From github page:
```
staramr search -o out --pointfinder-organism salmonella *.fasta
```

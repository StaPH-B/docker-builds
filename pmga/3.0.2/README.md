# pmga container

Main tool : [pmga](https://github.com/rpetit3/pmga)

Additional tools:
- Mash

Full documentation: https://github.com/rpetit3/pmga

[@rpetit3](https://github.com/rpetit3)'s fork of pgma

PMGA is a tool for serotyping/serogrouping all Neisseria species and Haemophilus influenzae.

In addition to `pmga`, this docker image contains the required databases built by `pmga-build`. The pre-built databases are located in `/pmga/blastdbs`.

# Example Usage

```
# Test H. influenzae genome
pmga /data/GCF_900478275.fna --blast /pmga/blastdbs

# Force H. influenzae genome (via --species)
pmga /data/GCF_900478275.fna --blast /pmga/blastdbs --species hinfluenzae
```

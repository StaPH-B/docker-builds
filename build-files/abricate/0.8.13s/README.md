# ABRicate container

Main tool : [ABRicate](https://github.com/tseemann/abricate)

It comes bundled with multiple databases: NCBI, CARD, ARG-ANNOT, Resfinder, MEGARES, EcOH, PlasmidFinder, Ecoli_VF, **SerotypeFinder**, and VFDB.

# Example Usage

```
abricate --db serotypefinder --threads {threads} --minid 80 --mincov 80 {contigs} > {abricate_results}
```

or 

```
abricate --summary {abricate_results} > {summary}
```
